"""Check experiment isolation and resolve the generated run with pinned Harbor."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shlex
import subprocess
import tempfile
import unittest

from layout_analyzer import ROOT, SUPPORTED, stage_tasks


class LayoutExperimentTests(unittest.TestCase):
    def test_summary_preserves_missing_reward_and_capture_failures(self):
        spec = importlib.util.spec_from_file_location('summary', ROOT / 'scripts/summarize-layout-experiment.py')
        summary = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(summary)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task = root / 'snapshot/tasks/flow-reports-strict'
            task.mkdir(parents=True)
            (task.parent.parent / 'manifest.json').write_text('{"mode":"full"}')
            trial = root / 'jobs/experiment/trial'
            captures = trial / 'agent/layout/one'
            captures.mkdir(parents=True)
            (captures / 'capture.json').write_text(json.dumps({
                'status': 'error', 'totalDurationMs': 2000, 'error': 'Copilot timeout',
            }))
            partial = captures.parent / 'partial'
            partial.mkdir()
            (partial / 'capture.json').write_text(json.dumps({
                'status': 'ok', 'totalDurationMs': 1000,
                'coverageWarnings': ['Visible panel missing from Copilot tree'],
            }))
            result = trial / 'result.json'
            verifier = trial / 'verifier'
            verifier.mkdir()
            (verifier / 'TEST-browser.xml').write_text('''<testsuite>
                <testcase name="filter" time="2"/>
                <testcase name="visual" time="3"><failure/></testcase>
                <testcase name="unavailable"><skipped/></testcase>
            </testsuite>''')
            result.write_text(json.dumps({
                'task_name': 'flow-reports-strict',
                'config': {'task': {'path': str(task)},
                           'agent': {'kwargs': {'reasoning_effort': 'xhigh'}}},
                'agent_execution': {'started_at': '2026-09-23T10:00:00',
                                    'finished_at': '2026-09-23T10:00:15'},
                'agent_result': {'n_input_tokens': 100, 'n_cache_tokens': 60},
                'exception_info': {'exception_type': 'AgentTimeoutError'},
            }))
            row = summary.summarize(result)
            self.assertIsNone(row['reward'])
            self.assertEqual(row['error'], 'AgentTimeoutError')
            self.assertEqual(row['successfulCaptures'], 1)
            self.assertEqual(row['captures'], 2)
            self.assertEqual(row['partialCaptures'], 1)
            self.assertEqual(row['captureErrors'], ['Copilot timeout'])
            self.assertEqual(row['captureTotalMs'], 3000)
            self.assertEqual(row['agentSeconds'], 15)
            self.assertEqual(row['inputTokensIncludingCache'], 100)
            self.assertEqual([test['status'] for test in row['browserTests']],
                             ['passed', 'failure', 'skipped'])

    def test_isolation_and_cache_invalidation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            name = SUPPORTED[0]
            task = root / 'tasks' / name
            for relative, content in {
                'environment/Dockerfile': 'FROM example\n',
                'instruction.md': 'Implement the view.\n',
                'task.toml': 'original task configuration',
                'tests/test.sh': 'original grading',
                'solution/solve.sh': 'reference solution',
                'environment/node_modules/private.txt': 'local debris',
            }.items():
                path = task / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            staged = stage_tasks([name], 'full', root)
            self.assertEqual(staged, stage_tasks([name], 'full', root))
            for relative in ('task.toml', 'tests/test.sh', 'solution/solve.sh'):
                self.assertEqual((task / relative).read_bytes(),
                                 (staged / name / relative).read_bytes())
            self.assertFalse((staged / name / 'environment/node_modules').exists())
            self.assertEqual((task / 'environment/Dockerfile').read_text(), 'FROM example\n')
            self.assertIn('layout-check', (staged / name / 'instruction.md').read_text())
            self.assertNotIn('`ui-check`', (staged / name / 'instruction.md').read_text())
            self.assertNotIn('`app-start`', (staged / name / 'instruction.md').read_text())
            self.assertIn('copilot.enable=true', (staged / name / 'environment/Dockerfile').read_text())
            manifest = json.loads((staged.parent / 'manifest.json').read_text())
            archive = staged / name / 'environment/layout-analyzer/preview.tgz'
            self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(),
                             manifest['inputs']['vaadin-layout-analyzer-preview-0.1.1.tgz'])
            (task / 'instruction.md').write_text('A changed task.\n')
            changed = stage_tasks([name], 'full', root)
            self.assertNotEqual(staged, changed)
            self.assertIn('Implement the view.\n', (staged / name / 'instruction.md').read_text())
            control = stage_tasks([name], 'control', root) / name
            self.assertEqual((control / 'instruction.md').read_text(), 'A changed task.\n')
            self.assertFalse((control / 'environment/layout-analyzer').exists())
            self.assertIn('copilot.enable=true', (control / 'environment/Dockerfile').read_text())

    def test_rejects_unsupported_tasks(self):
        with self.assertRaisesRegex(ValueError, 'unsupported'):
            stage_tasks(['flow-polymer-to-lit'], 'full')

    def test_harbor_configuration(self):
        for mode in ('control', 'geometry', 'full'):
            output = subprocess.check_output([
                'uv', 'run', 'vaadin-bench.py', '-c', 'vanilla', '-m', 'luna',
                '-t', 'flow-employee-list-strict', '-k', '1', '--layout-analyzer', mode,
                '--dry-run', '--', '--ak', 'reasoning_effort=xhigh', '-n', '9',
            ], cwd=ROOT, text=True)
            command = next(line for line in output.splitlines() if line.startswith('env '))
            config = json.loads(subprocess.check_output(
                shlex.split(command) + ['--print-config'], cwd=ROOT, text=True))
            self.assertEqual(config['n_concurrent_trials'], 1)
            self.assertEqual(config['agents'][0]['kwargs']['reasoning_effort'], 'xhigh')
            self.assertIn(f'layout-{mode}', config['job_name'])
            self.assertIn(f'/.layout-analyzer/{mode}/', config['datasets'][0]['path'])


if __name__ == '__main__':
    unittest.main()
