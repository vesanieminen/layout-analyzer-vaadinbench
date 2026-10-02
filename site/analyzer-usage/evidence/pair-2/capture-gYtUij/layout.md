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
Viewport 390x844. View 390x3368 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 2524px down. Content ends at x=390 y=3368. Fold at y=844.
100 components measured. Findings: 2 broken, 0 likely wrong, 11 to check.
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

- CLIPPED: Span "February 2026 sales" (Div[2] > Div[2] > Div[1] > Div[1] > Div[3] > Span[1])
  content is 103px wide in a 101px box: 2px not shown

- NEAR MISS: Span "Unread" (Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1] > Span[1])
  right edge is +2px from the x=359 its 22 siblings and neighbours share
  Also: Span "Unread" (Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Span[1])

- NEAR MISS: Div (Div[1] > Div[2])
  top edge is +2px from the y=11 its 4 siblings and neighbours share

- OFF SCALE: Div (Div[1] > Div[1])
  gap 2px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

- OFF SCALE: Div (Div[2] > Div[1])
  padding (right, left) 18px is not on the theme's spacing scale (nearest --vaadin-gap-l = 16px)

- OFF SCALE: Div (Div[2] > Div[2])
  padding 18px is not on the theme's spacing scale (nearest --vaadin-gap-l = 16px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[1] > Div[1])
  gap 6px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[2] > Div[2] > Div[1] > Div[2]); Div (Div[2] > Div[2] > Div[2] > Div[1] > Div[3])

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

ReportsView  0,0 390x3368  block
  y: 0 [62] 0 [3306] 0
  Div  0,0 390x62  row pad 8/16/8/16 align:center justify:between
    x: 0 [98] 94 [130] 0 [36] 0
    Image  16,11 98x40
    ? Div  208,11 130x40  block pad 0/12/0/12 gap2 margin 0/0/0/94 <- off-scale spacing
      y: 0 [40] 0
      Button "Reports"  220,11 106x40  block pad 6/12/6/8 gap 0/8
        y: 0 [20] 6
        Icon  229,18 20x20
    ? Div  338,13 36x36  row gap8 align:center <- near miss
      x: -2 [40] -2
      !! Avatar  336,11 40x40  margin -2/-2/-2/-2 <- cut off
  Div  0,62 390x3306  block
    y: 0 [78] 0 [3228] 0
    ? Div  0,62 390x78  col pad 0/18/0/18 gap4 justify:center <- off-scale spacing
      y: 11 [21] 4 [30] 11
      Span "Sales"  18,73 354x21
      ? H1 "Reports"  18,98 354x30  <- nothing under it
    ? Div  0,140 390x3228  block pad18 <- off-scale spacing
      y: 0 [118] 20 [3054] 0
      Div  18,158 354x118  wrap gap12 justify:between
        x row1 (y=158): 0 [354] 0
        x row2 (y=228): 217 [137] 0
        Div  18,158 354x58  grid
          x: 0 [118] 0 [118] 0 [118] 0
          Div  18,158 118x58  col pad 0/8/0/0 gap4 justify:center 33% of parent width
            y: 7 [16] 4 [24] 7
            Span "2026 average sales"  18,165 110x16
            Span "168 640 €"  18,185 110x24
          Div  136,158 118x58  col pad 0/8/0/8 gap4 justify:center 33% of parent width
            y: 7 [16] 4 [24] 7
            Span "March 2026 sales"  145,165 101x16
            Span "174 610 €"  145,185 101x24
          Div  254,158 118x58  col pad 0/8/0/8 gap4 justify:center 33% of parent width
            y: 7 [16] 4 [24] 7
            ? Span "February 2026 sales"  263,165 101x16  <- clipped
            Span "127 080 €"  263,185 101x24
        Button "New report"  235,228 137x48  row pad 6/12/6/8 gap 0/8 align:center justify:center margin 0/0/0/217 theme=tertiary-inline
          x: 0 [20] 95
          Icon  244,242 20x20
      Div  18,296 354x3054  grid gap16 margin 20/0/0/0
        y: 0 [368] 16 [2670] 0
        Div  18,296 354x368  grid gap 0/12
          y: 0 [24] 14 [94] 16 [94] 16 [94] 16
          H2 "Filters"  18,296 354x24  margin 0/0/14/0
          ? Div  18,334 354x94  col gap6 margin 0/0/16/0 <- off-scale spacing
            y: 0 [20] 6 [68] 0
            Span "Free search"  18,334 354x20
            TextField  18,360 354x68  block
              y: 34 [20] 14
              Icon  31,394 20x20
          ? Div  18,444 354x94  col gap6 margin 0/0/16/0 <- off-scale spacing
            y: 0 [20] 6 [68] 0
            Span "Regions"  18,444 354x20
            MultiSelectComboBox  18,470 354x68
          ? Div  18,554 354x94  col gap6 margin 0/0/16/0 <- off-scale spacing
            y: 0 [20] 6 [68] 0
            Span "Date range"  18,554 354x20
            ? Div  18,580 354x68  grid gap5 <- off-scale spacing
              x: 0 [167] 5 [10] 5 [167] 0
              DatePicker  18,580 167x68
              Span "–"  190,604 10x20
              DatePicker  205,580 167x68
        ? Div  18,680 354x2670  grid gap14 <- off-scale spacing
          y: 0 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 14 [230] 0
          Div  18,680 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,681 352x160
            ? Div  19,841 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Deutschland"  31,852 328x22
              Paragraph "March 2026"  31,874 328x21
              ? Span "Unread"  310,849 51x24  <- near miss
          Div  18,924 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,925 352x160
            ? Div  19,1085 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Czechia"  31,1096 328x22
              Paragraph "March 2026"  31,1118 328x21
              ? Span "Unread"  310,1093 51x24  <- near miss
          Div  18,1168 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,1169 352x160
            ? Div  19,1329 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Sweden"  31,1340 328x22
              Paragraph "March 2026"  31,1362 328x21
          Div  18,1412 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,1413 352x160
            ? Div  19,1573 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Austria"  31,1584 328x22
              Paragraph "March 2026"  31,1606 328x21
          Div  18,1656 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,1657 352x160
            ? Div  19,1817 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Finland"  31,1828 328x22
              Paragraph "March 2026"  31,1850 328x21
          Div  18,1900 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,1901 352x160
            ? Div  19,2061 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Deutschland"  31,2072 328x22
              Paragraph "February 2026"  31,2094 328x21
          Div  18,2144 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,2145 352x160
            ? Div  19,2305 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Czechia"  31,2316 328x22
              Paragraph "February 2026"  31,2338 328x21
          Div  18,2388 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,2389 352x160
            ? Div  19,2549 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Norway"  31,2560 328x22
              Paragraph "February 2026"  31,2582 328x21
          Div  18,2632 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,2633 352x160
            ? Div  19,2793 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Sweden"  31,2804 328x22
              Paragraph "February 2026"  31,2826 328x21
          Div  18,2876 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,2877 352x160
            ? Div  19,3037 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Austria"  31,3048 328x22
              Paragraph "February 2026"  31,3070 328x21
          Div  18,3120 354x230  block
            y: 0 [160] 0 [68] 0
            Image  19,3121 352x160
            ? Div  19,3281 352x68  block pad 11/12/11/12 <- off-scale spacing
              y: 0 [22] 0 [21] 3
              H2 "Finland"  31,3292 328x22
              Paragraph "February 2026"  31,3314 328x21

