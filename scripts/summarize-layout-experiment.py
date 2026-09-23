#!/usr/bin/env python3
"""Export per-trial outcomes and capture costs; never pool different tasks/arms."""
import argparse
from datetime import datetime
import json
from pathlib import Path


def read(path):
    return json.loads(path.read_text()) if path.is_file() else {}


def summarize(path):
    result = read(path)
    config = result.get('config') or read(path.parent / 'config.json')
    task = Path(config.get('task', {}).get('path', ''))
    manifest = read(task.parent.parent / 'manifest.json')
    if manifest.get('mode') not in ('control', 'geometry', 'full'):
        return None
    captures = [read(p) for p in sorted((path.parent / 'agent/layout').rglob('capture.json'))]
    timing = result.get('agent_execution') or {}
    seconds = None
    if timing.get('started_at') and timing.get('finished_at'):
        seconds = round((datetime.fromisoformat(timing['finished_at']) -
                         datetime.fromisoformat(timing['started_at'])).total_seconds(), 2)
    tokens = result.get('agent_result') or {}
    design = read(path.parent / 'verifier/design-evaluation.json')
    return {
        'job': path.parent.parent.name, 'trial': path.parent.name,
        'task': result['task_name'], 'taskChecksum': result.get('task_checksum'),
        'mode': manifest['mode'], 'manifest': str(task.parent.parent / 'manifest.json'),
        'model': config.get('agent', {}).get('model_name'),
        'effort': config.get('agent', {}).get('kwargs', {}).get('reasoning_effort'),
        'finished': result.get('finished_at'),
        'error': (result.get('exception_info') or {}).get('exception_type'),
        'reward': ((result.get('verifier_result') or {}).get('rewards') or {}).get('reward'),
        'agentSeconds': seconds,
        'inputTokensIncludingCache': tokens.get('n_input_tokens'),
        'cachedTokens': tokens.get('n_cache_tokens'), 'outputTokens': tokens.get('n_output_tokens'),
        'captures': len(captures),
        'successfulCaptures': sum(c.get('status') == 'ok' for c in captures),
        'partialCaptures': sum(bool(c.get('coverageWarnings')) for c in captures),
        'capturesWithoutCoverageCheck': sum(c.get('status') == 'ok' and 'readyElementInTree' not in c
                                           for c in captures),
        'captureTotalMs': sum(c.get('totalDurationMs', 0) for c in captures),
        'reportChars': sum(c.get('reportChars', 0) for c in captures),
        'captureErrors': [c.get('error') for c in captures if c.get('status') != 'ok'],
        'designChecks': design.get('design'), 'visualChecks': design.get('visual'),
        'designFailures': design.get('failures'),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('jobs', type=Path)
    args = parser.parse_args()
    rows = []
    for path in sorted(args.jobs.rglob('result.json')):
        if 'task_name' not in read(path):
            continue
        row = summarize(path)
        if row:
            rows.append(row)
    if not rows:
        parser.error('No completed layout experiment trial records with available manifests')
    print(json.dumps(rows, indent=2))


if __name__ == '__main__':
    main()
