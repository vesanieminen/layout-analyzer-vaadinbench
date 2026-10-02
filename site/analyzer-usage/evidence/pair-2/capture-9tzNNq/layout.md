Capture: current viewport and UI state only; 0/121 visible components have source references. Geometry stable over three 100ms samples; fonts ready. This does not establish that asynchronous data or future state changes are complete.

## Repeated relationships

Peers have matching component structure; shared geometry is evidence, not a design requirement. Insets below use physical left edges, including borders.

- first-child left inset: 2/3 peers use 25px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[2]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[3]).
  - Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[1]) uses 0px (-25px difference). Verify intent.
- first-child left inset: 11/11 peers use 1px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[2]).
- first-child left inset: 11/11 peers use 16px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]).
- heading-to-body gap: 11/11 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]).

# Layout: /reports

ReportsView
Viewport 1440x1024. View 1440x1197 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 173px down. Content ends at x=1440 y=1197. Fold at y=1024.
121 components measured. Findings: 2 broken, 0 likely wrong, 7 to check.

How to read this
- Coordinates are CSS px from the view's top-left; "x,y wxh" is the border box.
- Findings are tiered by judgement. Broken flags geometry symptoms. Likely wrong is a
  common mistake pattern. Every tier requires checking intent; Check is often deliberate.
- In the tree, !! marks a broken component, ! likely wrong, ? to check.
- Under a container, a strip lists its children along its main axis from content
  edge to content edge: "x: lead [child] gap [child] trail". A negative number
  means a child reaches past the container's edge; the findings say what happens to it.
- Every component created in project code is listed (layouts, fields, buttons,
  text). Elements inside Vaadin components are not, and a number here can still
  come from the theme rather than from project code.
- One viewport. Another width may lay out differently.

## Findings

### Broken - measured geometry; verify whether intentional

- CUT: Avatar (Div[1] > Div[2] > Avatar[1])
  content is 38px wide in a 36px box: 2px not shown

- CUT: Avatar (Div[1] > Div[2] > Avatar[1])
  content is 41px tall in a 36px box: 5px not shown

### Check - often deliberate; compare with what you intended

- UNEVEN GAPS: Span "Sales" (Div[1] > Div[1] > Span[1])
  gaps in Div run 19, 5, 2, 2, 19, 5, 2, 2, 19, 5, 2 while its gap is 2px: 17px of extra space before Span "Sales"
  Also: Button "Orders" (Div[1] > Div[1] > Button[2]); Span "Resources" (Div[1] > Div[1] > Span[2]); Button "Employees" (Div[1] > Div[1] > Button[5]); Span "Admin" (Div[1] > Div[1] > Span[3]); Button "Access management" (Div[1] > Div[1] > Button[8])
  Fix: a margin on the child, most likely; let the container gap do the spacing

- OFF SCALE: Div (Div[1] > Div[1])
  gap 2px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[1] > Div[1])
  gap 6px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[2] > Div[2] > Div[1] > Div[2]); Div (Div[2] > Div[2] > Div[2] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[1] > Div[3] > Div[1])
  gap 5px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[2])
  gap 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1])
  padding (top) 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)
  Also: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[3] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[4] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[5] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[6] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[7] > Div[1]); and 4 more

- ORPHAN HEADING: H1 "Reports" (Div[2] > Div[1] > H1[1])
  the last thing in Div, with nothing under it

## Layout tree

ReportsView  0,0 1440x1197  block
  y: 0 [1197] 0
  Div  0,0 272x1024  col pad 24/16/12/16 19% of parent width
    y: 0 [56] 16 [514] 358 [44] 0
    Image  24,24 138x56  margin 0/8/16/8
    ? Div  16,96 240x514  col gap2 <- off-scale spacing
      y: 0 [40] 19 [24] 5 [40] 2 [40] 2 [40] 19 [24] 5 [40] 2 [40] 2 [40] 19 [24] 5 [40] 2 [40] 0
      Button "Dashboard"  16,96 240x40  block pad 6/12/6/8 gap 0/8
        y: 0 [20] 6
        Icon  25,103 20x20
      ? Span "Sales"  16,155 240x24  margin 17/0/3/0 <- uneven gaps
      ? Button "Orders"  16,184 240x40  block pad 6/12/6/8 gap 0/8 <- uneven gaps
        y: 0 [20] 6
        Icon  25,191 20x20
      Button "Deliveries"  16,226 240x40  block pad 6/12/6/8 gap 0/8
        y: 0 [20] 6
        Icon  25,233 20x20
      Button "Reports"  16,268 240x40  block pad 6/12/6/8 gap 0/8
        y: 0 [20] 6
        Icon  25,275 20x20
      ? Span "Resources"  16,327 240x24  margin 17/0/3/0 <- uneven gaps
      ? Button "Employees"  16,356 240x40  block pad 6/12/6/8 gap 0/8 <- uneven gaps
        y: 0 [20] 6
        Icon  25,363 20x20
      Button "Utilisation"  16,398 240x40  block pad 6/12/6/8 gap 0/8
        y: 0 [20] 6
        Icon  25,405 20x20
      Button "Payroll"  16,440 240x40  block pad 6/12/6/8 gap 0/8
        y: 0 [20] 6
        Icon  25,447 20x20
      ? Span "Admin"  16,499 240x24  margin 17/0/3/0 <- uneven gaps
      ? Button "Access management"  16,528 240x40  block pad 6/12/6/8 gap 0/8 <- uneven gaps
        y: 0 [20] 6
        Icon  25,535 20x20
      Button "Settings"  16,570 240x40  block pad 6/12/6/8 gap 0/8
        y: 0 [20] 6
        Icon  25,577 20x20
    Div  16,968 240x44  row pad 8/0/0/0 gap8 align:center margin 358/0/0/0
      x: -2 [40] 6 [136] 46 [14] 0
      !! Avatar  14,974 40x40  margin -2/-2/-2/-2 <- cut off
      Span "Firstname Lastname"  60,984 136x20
      Icon  242,987 14x14  margin 0/0/0/38
  Div  272,0 1168x1197  block 81% of parent width margin 0/0/0/272
    y: 0 [90] 0 [1107] 0
    Div  272,0 1168x90  col pad 0/24/0/24 gap4 justify:center
      y: 17 [21] 4 [30] 17
      Span "Sales"  296,17 1120x21
      ? H1 "Reports"  296,42 1120x30  <- nothing under it
    Div  272,90 1168x1107  block pad24
      y: 0 [65] 24 [970] 0
      Div  296,114 1120x65  row gap24 align:center justify:between
        ... 12 components inside, none flagged
      Div  296,203 1120x970  grid gap24 margin 24/0/0/0
        x: 0 [300] 24 [796] 0
        Div  296,203 300x376  block 27% of parent width
          y: 0 [24] 14 [94] 16 [102] 16 [94] 16
          H2 "Filters"  296,203 300x24  margin 0/0/14/0
          ? Div  296,241 300x94  col gap6 margin 0/0/16/0 <- off-scale spacing
            y: 0 [20] 6 [68] 0
            Span "Free search"  296,241 300x20
            TextField  296,267 300x68  block
              y: 34 [20] 14
              Icon  309,301 20x20
          ? Div  296,351 300x102  col gap6 margin 0/0/16/0 <- off-scale spacing
            y: 0 [20] 6 [76] 0
            Span "Regions"  296,351 300x20
            MultiSelectComboBox  296,377 300x76
          ? Div  296,469 300x94  col gap6 margin 0/0/16/0 <- off-scale spacing
            y: 0 [20] 6 [68] 0
            Span "Date range"  296,469 300x20
            ? Div  296,495 300x68  grid gap5 <- off-scale spacing
              x: 0 [140] 5 [10] 5 [140] 0
              DatePicker  296,495 140x68
              Span "–"  441,519 10x20
              DatePicker  456,495 140x68
        ? Div  620,203 796x970  grid gap14 71% of parent width <- off-scale spacing
          x row1 (y=203): 0 [256] 14 [256] 14 [256] 0
          x row2 (y=449): 0 [256] 14 [256] 14 [256] 0
          x row3 (y=695): 0 [256] 14 [256] 14 [256] 0
          x row4 (y=941): 0 [256] 14 [256] 270
          Div  620,203 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  621,204 254x160
            ? Div  621,364 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Deutschland"  637,378 222x22
              Paragraph "March 2026"  637,400 222x21
              Span "Unread"  791,386 68x28
          Div  890,203 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  891,204 254x160
            ? Div  891,364 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Czechia"  907,378 222x22
              Paragraph "March 2026"  907,400 222x21
              Span "Unread"  1061,386 68x28
          Div  1160,203 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  1161,204 254x160
            ? Div  1161,364 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Sweden"  1177,378 222x22
              Paragraph "March 2026"  1177,400 222x21
          Div  620,449 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  621,450 254x160
            ? Div  621,610 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Austria"  637,624 222x22
              Paragraph "March 2026"  637,646 222x21
          Div  890,449 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  891,450 254x160
            ? Div  891,610 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Finland"  907,624 222x22
              Paragraph "March 2026"  907,646 222x21
          Div  1160,449 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  1161,450 254x160
            ? Div  1161,610 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Deutschland"  1177,624 222x22
              Paragraph "February 2026"  1177,646 222x21
          Div  620,695 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  621,696 254x160
            ? Div  621,856 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Czechia"  637,870 222x22
              Paragraph "February 2026"  637,892 222x21
          Div  890,695 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  891,696 254x160
            ? Div  891,856 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Norway"  907,870 222x22
              Paragraph "February 2026"  907,892 222x21
          Div  1160,695 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  1161,696 254x160
            ? Div  1161,856 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Sweden"  1177,870 222x22
              Paragraph "February 2026"  1177,892 222x21
          Div  620,941 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  621,942 254x160
            ? Div  621,1102 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Austria"  637,1116 222x22
              Paragraph "February 2026"  637,1138 222x21
          Div  890,941 256x232  block 32% of parent width
            y: 0 [160] 0 [70] 0
            Image  891,942 254x160
            ? Div  891,1102 254x70  block pad 14/16/12/16 <- off-scale spacing
              y: 0 [22] 0 [21] 1
              H2 "Finland"  907,1116 222x22
              Paragraph "February 2026"  907,1138 222x21

