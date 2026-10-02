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
Viewport 1440x1024. View 1440x1212 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 188px down. Content ends at x=1440 y=1212. Fold at y=1024.
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
  padding (top) 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[1])
  padding (bottom) 13px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[1] > Div[1])
  padding (right) 23px is not on the theme's spacing scale (nearest --vaadin-gap-xl = 24px)
  Also: Div (Div[2] > Div[2] > Div[1] > Div[2]); Div (Div[2] > Div[2] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[3])
  padding (bottom) 32px is not on the theme's spacing scale (nearest --vaadin-gap-xl = 24px)

- OFF SCALE: Div (Div[2] > Div[3] > Div[1] > Div[1])
  gap 6px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[3] > Div[1] > Div[2]); Div (Div[2] > Div[3] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[3] > Div[1] > Div[3] > Div[1])
  gap 5px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

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

ReportsView  0,0 1440x1212  row align:start
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
  Div  272,0 1168x1212  block
    y: 0 [90] 0 [91] 24 [1007] 0
    ? Div  272,0 1168x90  col pad 14/24/13/24 justify:center <- off-scale spacing
      y: 4 [20] 7 [28] 4
      Span "Sales"  296,18 1120x20
      Span "Reports"  296,45 1120x28  margin 7/0/0/0
    Div  272,90 1168x91  row pad 24/24/0/24 align:center
      x: 0 [744] 233 [143] 0
      Div  296,114 744x67  row
        x: 0 [248] 0 [248] 0 [248] 0
        ? Div  296,114 248x67  col pad 0/23/0/0 gap8 justify:center <- off-scale spacing
          y: 0 [23] 8 [36] 0
          Span "2026 average sales"  296,114 224x23
          Span "168 640 €"  296,145 224x36
        ? Div  544,114 248x67  col pad 0/23/0/24 gap8 justify:center <- off-scale spacing
          y: 0 [23] 8 [36] 0
          Span "March 2026 sales"  568,114 200x23
          Span "174 610 €"  568,145 200x36
        ? Div  792,114 248x67  col pad 0/23/0/24 gap8 justify:center <- off-scale spacing
          y: 0 [23] 8 [36] 0
          Span "February 2026 sales"  816,114 201x23
          Span "127 080 €"  816,145 201x36
      Button "New report"  1273,124 143x48  margin 0/0/0/233
    ? Div  272,205 1168x1007  grid pad 0/24/32/24 gap24 margin 24/0/0/0 <- off-scale spacing
      x: 0 [300] 24 [796] 0
      Div  296,205 300x304  col 27% of parent width
        y: 0 [25] 18 [79] 8 [79] 8 [79] 8
        Span "Filters"  296,205 300x25  margin 0/0/18/0
        ? Div  296,248 300x79  col gap6 margin 0/0/8/0 <- off-scale spacing
          y: 0 [19] 6 [54] 0
          Span "Free search"  296,248 300x19
          TextField  296,273 300x54
        ? Div  296,335 300x79  col gap6 margin 0/0/8/0 <- off-scale spacing
          y: 0 [19] 6 [54] 0
          Span "Regions"  296,335 300x19
          MultiSelectComboBox  296,360 300x54
        ? Div  296,422 300x79  col gap6 margin 0/0/8/0 <- off-scale spacing
          y: 0 [19] 6 [54] 0
          Span "Date range"  296,422 300x19
          ? Div  296,447 300x54  row gap5 align:center <- off-scale spacing
            x: 0 [143] 5 [5] 5 [143] 0
            DatePicker  296,447 143x54
            Span "-"  444,464 5x20
            DatePicker  454,447 143x54
      ? Div  620,205 796x975  grid gap 14/15 71% of parent width <- off-scale spacing
        x row1 (y=205): 0 [255] 15 [255] 15 [255] 0
        x row2 (y=452): 0 [255] 15 [255] 15 [255] 0
        x row3 (y=700): 0 [255] 15 [255] 15 [255] 0
        x row4 (y=947): 0 [255] 15 [255] 270
        Div  620,205 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  621,206 253x160  block
            y: 0 [160] 0
            Image  621,206 253x160
          ? Div  621,366 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [98] 55 [68] 0
            ? Div  637,381 98x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Deutschland"  637,381 98x21
              Span "March 2026"  637,403 98x19
            Span "Unread"  790,387 68x28
        Div  890,205 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  891,206 253x160  block
            y: 0 [160] 0
            Image  891,206 253x160
          ? Div  891,366 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 70 [68] 0
            ? Div  907,381 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Czechia"  907,381 83x21
              Span "March 2026"  907,403 83x19
            Span "Unread"  1061,387 68x28
        Div  1161,205 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  1162,206 253x160  block
            y: 0 [160] 0
            Image  1162,206 253x160
          ? Div  1162,366 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 138
            ? Div  1178,381 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Sweden"  1178,381 83x21
              Span "March 2026"  1178,403 83x19
        Div  620,452 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  621,453 253x160  block
            y: 0 [160] 0
            Image  621,453 253x160
          ? Div  621,614 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 138
            ? Div  637,628 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Austria"  637,628 83x21
              Span "March 2026"  637,650 83x19
        Div  890,452 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  891,453 253x160  block
            y: 0 [160] 0
            Image  891,453 253x160
          ? Div  891,614 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 138
            ? Div  907,628 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Finland"  907,628 83x21
              Span "March 2026"  907,650 83x19
        Div  1161,452 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  1162,453 253x160  block
            y: 0 [160] 0
            Image  1162,453 253x160
          ? Div  1162,614 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  1178,628 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Deutschland"  1178,628 100x21
              Span "February 2026"  1178,650 100x19
        Div  620,700 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  621,701 253x160  block
            y: 0 [160] 0
            Image  621,701 253x160
          ? Div  621,861 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  637,875 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Czechia"  637,875 100x21
              Span "February 2026"  637,897 100x19
        Div  890,700 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  891,701 253x160  block
            y: 0 [160] 0
            Image  891,701 253x160
          ? Div  891,861 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  907,875 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Norway"  907,875 100x21
              Span "February 2026"  907,897 100x19
        Div  1161,700 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  1162,701 253x160  block
            y: 0 [160] 0
            Image  1162,701 253x160
          ? Div  1162,861 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  1178,875 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Sweden"  1178,875 100x21
              Span "February 2026"  1178,897 100x19
        Div  620,947 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  621,948 253x160  block
            y: 0 [160] 0
            Image  621,948 253x160
          ? Div  621,1108 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  637,1123 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Austria"  637,1123 100x21
              Span "February 2026"  637,1145 100x19
        Div  890,947 255x233  block 32% of parent width
          y: 0 [160] 0 [71] 0
          Div  891,948 253x160  block
            y: 0 [160] 0
            Image  891,948 253x160
          ? Div  891,1108 253x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 121
            ? Div  907,1123 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Finland"  907,1123 100x21
              Span "February 2026"  907,1145 100x19

