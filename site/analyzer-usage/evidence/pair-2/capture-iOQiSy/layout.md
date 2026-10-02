Capture: current viewport and UI state only; 0/100 visible components have source references. Geometry stable over three 100ms samples; fonts ready. This does not establish that asynchronous data or future state changes are complete.

## Repeated relationships

Peers have matching component structure; shared geometry is evidence, not a design requirement. Insets below use physical left edges, including borders.

- first-child left inset: 2/3 peers use 9px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[2]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[3]).
  - Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[1]) uses 0px (-9px difference). Verify intent.
- first-child left inset: 11/11 peers use 1px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[2]).
- first-child left inset: 11/11 peers use 12px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]).
- heading-to-body gap: 11/11 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]).

# Layout: /reports

ReportsView
Viewport 390x844. View 390x3302 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 2458px down. Content ends at x=390 y=3302. Fold at y=844.
100 components measured. Findings: 2 broken, 0 likely wrong, 10 to check.
Not measured: 11 hidden components inside Div, 2 hidden components inside Div. Hidden tabs and panels are not rendered, so nothing below describes them.

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

- NEAR MISS: Span "Unread" (Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1] > Span[1])
  right edge is +2px from the x=359 its 22 siblings and neighbours share
  Also: Span "Unread" (Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Span[1])

- SET VARIANCE: Div (Div[2] > Div[2] > Div[1] > Div[1] > Div[1])
  width 110px while 2 sibling divs in Div are 122px

- OFF SCALE: Div (Div[1] > Div[1])
  gap 2px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

- OFF SCALE: Div (Div[2] > Div[1])
  padding (right, left) 18px is not on the theme's spacing scale (nearest --vaadin-gap-l = 16px)

- OFF SCALE: Div (Div[2] > Div[2])
  padding 18px is not on the theme's spacing scale (nearest --vaadin-gap-l = 16px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[1] > Div[1])
  gap 6px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[2] > Div[2] > Div[1] > Div[2])

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[1] > Div[3] > Div[1])
  gap 5px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[2])
  gap 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1])
  padding (top, bottom) 11px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)
  Also: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[3] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[4] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[5] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[6] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[7] > Div[1]); and 4 more

- ORPHAN HEADING: H1 "Reports" (Div[2] > Div[1] > H1[1])
  the last thing in Div, with nothing under it

## Layout tree

ReportsView  0,0 390x3302  block
  y: 0 [62] 0 [3240] 0
  Div  0,0 390x62  row pad 8/16/8/16 align:center justify:between
    x: 0 [98] 92 [128] 0 [40] 0
    Image  16,11 98x40
    ? Div  206,11 128x40  block pad 0/12/0/12 gap2 margin 0/0/0/92 <- off-scale spacing
      y: 0 [40] 0
      Button "Reports"  218,11 104x40  block pad 0/10/0/8 gap 0/8
        y: 0 [20] 18
        Icon  227,12 20x20
    Div  334,11 40x40  row gap8 align:center
      x: 0 [40] 0
      !! Avatar  334,11 40x40  <- cut off
  Div  0,62 390x3240  block
    y: 0 [78] 0 [3162] 0
    ? Div  0,62 390x78  col pad 0/18/0/18 gap4 justify:center <- off-scale spacing
      y: 11 [21] 4 [30] 11
      Span "Sales"  18,73 354x21
      ? H1 "Reports"  18,98 354x30  <- nothing under it
    ? Div  0,140 390x3162  block pad18 <- off-scale spacing
      y: 0 [118] 20 [2988] 0
      Div  18,158 354x118  wrap gap12 justify:between
        x row1 (y=158): 0 [354] 0
        x row2 (y=228): 213 [141] 0
        Div  18,158 354x58  grid
          x: 0 [110] 0 [122] 0 [122] 0
          ? Div  18,158 110x58  col pad 0/8/0/0 gap4 justify:center 31% of parent width <- differs from siblings
            y: 8 [15] 4 [24] 8
            Span "2026 average sales"  18,166 102x15
            Span "168 640 €"  18,185 102x24
          Div  128,158 122x58  col pad 0/8/0/8 gap4 justify:center 34% of parent width
            y: 8 [15] 4 [24] 8
            Span "March 2026 sales"  137,166 105x15
            Span "174 610 €"  137,185 105x24
          Div  250,158 122x58  col pad 0/8/0/8 gap4 justify:center 34% of parent width
            y: 8 [15] 4 [24] 8
            Span "February 2026 sales"  259,166 105x15
            Span "127 080 €"  259,185 105x24
        Button "New report"  231,228 141x48  row pad 0/16/0/8 gap 0/8 align:center justify:center margin 0/0/0/213 theme=tertiary-inline
          x: 0 [20] 95
          Icon  240,242 20x20
      Div  18,296 354x2988  grid gap16 margin 20/0/0/0
        y: 0 [302] 16 [2670] 0
        Div  18,296 354x302  grid gap 0/12
          y: 0 [24] 14 [74] 16 [74] 16 [68] 16
          H2 "Filters"  18,296 354x24  margin 0/0/14/0
          ? Div  18,334 354x74  col gap6 margin 0/0/16/0 <- off-scale spacing
            y: 0 [20] 6 [48] 0
            Span "Free search"  18,334 354x20
            TextField  18,360 354x48  block
              y: 14 [20] 14
              Icon  31,374 20x20
          ? Div  18,424 354x74  col gap6 margin 0/0/16/0 <- off-scale spacing
            y: 0 [20] 6 [48] 0
            Span "Regions"  18,424 354x20
            MultiSelectComboBox  18,450 354x48
          Div  18,514 354x68  col margin 0/0/16/0
            y: 0 [20] 0 [48] 0
            Span "Date range"  18,514 354x20
            ? Div  18,534 354x48  grid gap5 <- off-scale spacing
              x: 0 [170] 5 [4] 5 [170] 0
              DatePicker  18,534 170x48
              Span "–"  193,548 4x20
              DatePicker  202,534 170x48
        ? Div  18,614 354x2670  grid gap14 <- off-scale spacing
          y: 0 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 0
          Div  18,614 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,615 352x160
            ? Div  19,775 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Deutschland"  31,786 328x22
              Paragraph "March 2026"  31,808 328x21
              ? Span "Unread"  310,783 51x24  <- near miss
          Div  18,858 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,859 352x160
            ? Div  19,1019 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Czechia"  31,1030 328x22
              Paragraph "March 2026"  31,1052 328x21
              ? Span "Unread"  310,1027 51x24  <- near miss
          Div  18,1102 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,1103 352x160
            ? Div  19,1263 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Sweden"  31,1274 328x22
              Paragraph "March 2026"  31,1296 328x21
          Div  18,1346 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,1347 352x160
            ? Div  19,1507 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Austria"  31,1518 328x22
              Paragraph "March 2026"  31,1540 328x21
          Div  18,1590 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,1591 352x160
            ? Div  19,1751 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Finland"  31,1762 328x22
              Paragraph "March 2026"  31,1784 328x21
          Div  18,1834 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,1835 352x160
            ? Div  19,1995 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Deutschland"  31,2006 328x22
              Paragraph "February 2026"  31,2028 328x21
          Div  18,2078 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,2079 352x160
            ? Div  19,2239 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Czechia"  31,2250 328x22
              Paragraph "February 2026"  31,2272 328x21
          Div  18,2322 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,2323 352x160
            ? Div  19,2483 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Norway"  31,2494 328x22
              Paragraph "February 2026"  31,2516 328x21
          Div  18,2566 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,2567 352x160
            ? Div  19,2727 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Sweden"  31,2738 328x22
              Paragraph "February 2026"  31,2760 328x21
          Div  18,2810 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,2811 352x160
            ? Div  19,2971 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Austria"  31,2982 328x22
              Paragraph "February 2026"  31,3004 328x21
          Div  18,3054 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,3055 352x160
            ? Div  19,3215 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Finland"  31,3226 328x22
              Paragraph "February 2026"  31,3248 328x21

