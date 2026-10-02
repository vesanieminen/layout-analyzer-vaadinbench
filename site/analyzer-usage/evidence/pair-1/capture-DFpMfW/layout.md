Capture: current viewport and UI state only; 0/142 visible components have source references. Geometry stable over three 100ms samples; fonts ready. This does not establish that asynchronous data or future state changes are complete.

## Repeated relationships

Peers have matching component structure; shared geometry is evidence, not a design requirement. Insets below use physical left edges, including borders.

- first-child left inset: 12/15 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[1] > Div[2] > Div[1]).
  - Div (App > ReportsView[1] > Div[2] > Div[1]) uses 24px (24px difference). Verify intent.
  - Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[2]) uses 24px (24px difference). Verify intent.
  - Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[3]) uses 24px (24px difference). Verify intent.
- first-child left inset: 3/3 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[1] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2]).
- first-child left inset: 11/11 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[2] > Div[1]).
- first-child left inset: 9/9 peers use 1px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[3]); Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[4]).
- first-child left inset: 9/9 peers use 16px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[3] > Div[2]); Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[4] > Div[2]).

# Layout: /reports

ReportsView
Viewport 1440x1024. View 1440x1201 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 177px down. Content ends at x=1440 y=1201. Fold at y=1024.
142 components measured. Findings: 2 broken, 0 likely wrong, 15 to check.

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
  content is 34px wide in a 32px box: 2px not shown

- CUT: Avatar (Div[1] > Div[2] > Avatar[1])
  content is 37px tall in a 32px box: 5px not shown

### Check - often deliberate; compare with what you intended

- UNEVEN GAPS: Div (Div[1] > Div[1] > Div[1])
  gaps in Div run 11, 4, 4, 4, 11, 4, 4, 4, 11, 4, 4 while its gap is 4px: 7px of extra space before Div
  Also: Div (Div[1] > Div[1] > Div[2]); Div (Div[1] > Div[1] > Div[3])
  Fix: a margin on the child, most likely; let the container gap do the spacing

- OFF SCALE: Div (Div[1] > Div[2])
  gap 9px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[1] > Div[2])
  padding (right, left) 2px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

- OFF SCALE: Div (Div[2] > Div[1])
  padding (top) 13px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[1])
  padding (bottom) 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[1] > Div[1])
  padding (right) 23px is not on the theme's spacing scale (nearest --vaadin-gap-xl = 24px)
  Also: Div (Div[2] > Div[2] > Div[1] > Div[2]); Div (Div[2] > Div[2] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[3])
  padding (bottom) 32px is not on the theme's spacing scale (nearest --vaadin-gap-xl = 24px)

- OFF SCALE: Div (Div[2] > Div[3] > Div[1] > Div[1])
  gap 6px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[3] > Div[1] > Div[2]); Div (Div[2] > Div[3] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[3] > Div[1] > Div[3] > Div[1])
  gap 7px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[2] > Div[3] > Div[2])
  gap 15px is not on the theme's spacing scale (nearest --vaadin-gap-l = 16px)

- OFF SCALE: Div (Div[2] > Div[3] > Div[2])
  row-gap 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[3] > Div[2] > Div[1] > Div[2])
  gap 6px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[3] > Div[2] > Div[2] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[3] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[4] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[5] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[6] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[7] > Div[2]); and 4 more

- OFF SCALE: Div (Div[2] > Div[3] > Div[2] > Div[1] > Div[2])
  padding (top) 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)
  Also: Div (Div[2] > Div[3] > Div[2] > Div[2] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[3] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[4] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[5] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[6] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[7] > Div[2]); and 4 more

- OFF SCALE: Div (Div[2] > Div[3] > Div[2] > Div[1] > Div[2])
  padding (bottom) 11px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)
  Also: Div (Div[2] > Div[3] > Div[2] > Div[2] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[3] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[4] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[5] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[6] > Div[2]); Div (Div[2] > Div[3] > Div[2] > Div[7] > Div[2]); and 4 more

- OFF SCALE: Div (Div[2] > Div[3] > Div[2] > Div[1] > Div[2] > Div[1])
  gap 1px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[3] > Div[2] > Div[2] > Div[2] > Div[1]); Div (Div[2] > Div[3] > Div[2] > Div[3] > Div[2] > Div[1]); Div (Div[2] > Div[3] > Div[2] > Div[4] > Div[2] > Div[1]); Div (Div[2] > Div[3] > Div[2] > Div[5] > Div[2] > Div[1]); Div (Div[2] > Div[3] > Div[2] > Div[6] > Div[2] > Div[1]); Div (Div[2] > Div[3] > Div[2] > Div[7] > Div[2] > Div[1]); and 4 more

## Layout tree

ReportsView  0,0 1440x1201  row align:start
  x: 0 [272] 0 [1168] 0
  Div  0,0 272x1024  col pad 24/16/16/16
    y: 0 [56] 20 [509] 355 [44] 0
    Image  24,24 138x56  margin 0/0/20/8
    Div  16,100 240x509  col gap4
      y: 0 [40] 11 [28] 4 [40] 4 [40] 4 [40] 11 [28] 4 [40] 4 [40] 4 [40] 11 [28] 4 [40] 4 [40] 0
      Anchor  16,100 240x40  row pad 0/11/0/11 gap15 align:center
        x: 35 [78] 103
        Span "Dashboard"  63,113 78x15
      ? Div  16,151 240x28  block margin 7/0/0/0 <- uneven gaps
        y: 0 [28] 0
        Span "Sales"  16,151 240x28
      Anchor  16,183 240x40  row pad 0/11/0/11 gap15 align:center
        x: 35 [49] 132
        Span "Orders"  63,196 49x15
      Anchor  16,227 240x40  row pad 0/11/0/11 gap15 align:center
        x: 35 [71] 110
        Span "Deliveries"  63,240 71x15
      Anchor  16,271 240x40  row pad 0/11/0/11 gap15 align:center
        x: 35 [55] 126
        Span "Reports"  63,284 55x15
      ? Div  16,322 240x28  block margin 7/0/0/0 <- uneven gaps
        y: 0 [28] 0
        Span "Resources"  16,322 240x28
      Anchor  16,354 240x40  row pad 0/11/0/11 gap15 align:center
        x: 35 [77] 104
        Span "Employees"  63,367 77x15
      Anchor  16,398 240x40  row pad 0/11/0/11 gap15 align:center
        x: 35 [73] 108
        Span "Utilisation"  63,411 73x15
      Anchor  16,442 240x40  row pad 0/11/0/11 gap15 align:center
        x: 35 [49] 132
        Span "Payroll"  63,455 49x15
      ? Div  16,493 240x28  block margin 7/0/0/0 <- uneven gaps
        y: 0 [28] 0
        Span "Admin"  16,493 240x28
      Anchor  16,525 240x40  row pad 0/11/0/11 gap15 align:center
        x: 35 [148] 33
        Span "Access management"  63,538 148x15
      Anchor  16,569 240x40  row pad 0/11/0/11 gap15 align:center
        x: 35 [58] 123
        Span "Settings"  63,582 58x15
    ? Div  16,964 240x44  row pad 0/2/0/2 gap9 align:center margin 355/0/0/0 <- off-scale spacing
      x: -2 [36] 7 [136] 59
      !! Avatar  16,968 36x36  margin -2/-2/-2/-2 <- cut off
      Span "Firstname Lastname"  59,976 136x20
  Div  272,0 1168x1201  block
    y: 0 [90] 0 [88] 24 [999] 0
    ? Div  272,0 1168x90  col pad 13/24/14/24 justify:center <- off-scale spacing
      y: 5 [20] 5 [28] 5
      Span "Sales"  296,18 1120x20
      Span "Reports"  296,43 1120x28  margin 5/0/0/0
    Div  272,90 1168x88  row pad 24/24/0/24 align:center
      x: 0 [744] 233 [143] 0
      Div  296,114 744x64  row
        x: 0 [248] 0 [248] 0 [248] 0
        ? Div  296,114 248x64  col pad 0/23/0/0 justify:center <- off-scale spacing
          y: 3 [23] 0 [36] 3
          Span "2026 average sales"  296,117 224x23
          Span "168 640 €"  296,140 224x36
        ? Div  544,114 248x64  col pad 0/23/0/24 justify:center <- off-scale spacing
          y: 3 [23] 0 [36] 3
          Span "March 2026 sales"  568,117 200x23
          Span "174 610 €"  568,140 200x36
        ? Div  792,114 248x64  col pad 0/23/0/24 justify:center <- off-scale spacing
          y: 3 [23] 0 [36] 3
          Span "February 2026 sales"  816,117 201x23
          Span "127 080 €"  816,140 201x36
      Button "New report"  1273,122 143x48  margin 0/0/0/233
    ? Div  272,202 1168x999  grid pad 0/24/32/24 gap24 margin 24/0/0/0 <- off-scale spacing
      x: 0 [300] 24 [796] 0
      Div  296,202 300x344  col 27% of parent width
        y: 0 [25] 16 [93] 8 [93] 8 [93] 8
        Span "Filters"  296,202 300x25  margin 0/0/16/0
        ? Div  296,243 300x93  col gap6 margin 0/0/8/0 <- off-scale spacing
          y: 0 [19] 6 [68] 0
          Span "Free search"  296,243 300x19
          TextField  296,268 300x68
        ? Div  296,344 300x93  col gap6 margin 0/0/8/0 <- off-scale spacing
          y: 0 [19] 6 [68] 0
          Span "Regions"  296,344 300x19
          MultiSelectComboBox  296,369 300x68
        ? Div  296,445 300x93  col gap6 margin 0/0/8/0 <- off-scale spacing
          y: 0 [19] 6 [68] 0
          Span "Date range"  296,445 300x19
          ? Div  296,470 300x68  row gap7 align:center <- off-scale spacing
            x: 0 [141] 7 [5] 7 [141] 0
            DatePicker  296,470 141x68
            Span "-"  444,494 5x20
            DatePicker  456,470 141x68
      ? Div  620,202 796x967  grid gap 14/15 71% of parent width <- off-scale spacing
        x row1 (y=202): 0 [255] 15 [255] 15 [255] 0
        x row2 (y=447): 0 [255] 15 [255] 15 [255] 0
        x row3 (y=693): 0 [255] 15 [255] 15 [255] 0
        x row4 (y=938): 0 [255] 15 [255] 270
        Div  620,202 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  621,203 253x159  block
            y: 0 [159] 0
            Image  621,203 253x159
          ? Div  621,362 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [98] 55 [68] 0
            ? Div  637,376 98x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Deutschland"  637,376 98x21
              Span "March 2026"  637,398 98x19
            Span "Unread"  790,383 68x28
        Div  890,202 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  891,203 253x159  block
            y: 0 [159] 0
            Image  891,203 253x159
          ? Div  891,362 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 70 [68] 0
            ? Div  907,376 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Czechia"  907,376 83x21
              Span "March 2026"  907,398 83x19
            Span "Unread"  1061,383 68x28
        Div  1161,202 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  1162,203 253x159  block
            y: 0 [159] 0
            Image  1162,203 253x159
          ? Div  1162,362 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 138
            ? Div  1178,376 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Sweden"  1178,376 83x21
              Span "March 2026"  1178,398 83x19
        Div  620,447 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  621,448 253x159  block
            y: 0 [159] 0
            Image  621,448 253x159
          ? Div  621,608 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 138
            ? Div  637,622 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Austria"  637,622 83x21
              Span "March 2026"  637,644 83x19
        Div  890,447 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  891,448 253x159  block
            y: 0 [159] 0
            Image  891,448 253x159
          ? Div  891,608 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 138
            ? Div  907,622 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Finland"  907,622 83x21
              Span "March 2026"  907,644 83x19
        Div  1161,447 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  1162,448 253x159  block
            y: 0 [159] 0
            Image  1162,448 253x159
          ? Div  1162,608 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  1178,622 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Deutschland"  1178,622 100x21
              Span "February 2026"  1178,644 100x19
        Div  620,693 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  621,694 253x159  block
            y: 0 [159] 0
            Image  621,694 253x159
          ? Div  621,853 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  637,867 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Czechia"  637,867 100x21
              Span "February 2026"  637,889 100x19
        Div  890,693 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  891,694 253x159  block
            y: 0 [159] 0
            Image  891,694 253x159
          ? Div  891,853 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  907,867 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Norway"  907,867 100x21
              Span "February 2026"  907,889 100x19
        Div  1161,693 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  1162,694 253x159  block
            y: 0 [159] 0
            Image  1162,694 253x159
          ? Div  1162,853 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  1178,867 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Sweden"  1178,867 100x21
              Span "February 2026"  1178,889 100x19
        Div  620,938 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  621,939 253x159  block
            y: 0 [159] 0
            Image  621,939 253x159
          ? Div  621,1098 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  637,1112 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Austria"  637,1112 100x21
              Span "February 2026"  637,1134 100x19
        Div  890,938 255x231  block 32% of parent width
          y: 0 [159] 0 [70] 0
          Div  891,939 253x159  block
            y: 0 [159] 0
            Image  891,939 253x159
          ? Div  891,1098 253x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  907,1112 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Finland"  907,1112 100x21
              Span "February 2026"  907,1134 100x19

