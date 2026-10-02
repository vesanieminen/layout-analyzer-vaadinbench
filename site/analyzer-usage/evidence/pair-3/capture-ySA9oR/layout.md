Capture: current viewport and UI state only; 0/107 visible components have source references. Geometry stable over three 100ms samples; fonts ready. This does not establish that asynchronous data or future state changes are complete.

## Repeated relationships

Peers have matching component structure; shared geometry is evidence, not a design requirement. Insets below use physical left edges, including borders.

- first-child left inset: 12/14 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1] > Div[1]).
  - Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[2]) uses 8px (8px difference). Verify intent.
  - Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[3]) uses 8px (8px difference). Verify intent.
- first-child left inset: 9/9 peers use 1px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[3]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[4]).
- first-child left inset: 9/9 peers use 10px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[3] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[4] > Div[1]).

# Layout: /reports

ReportsView
Viewport 390x844. View 390x3778 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 2934px down. Content ends at x=390 y=3762. Fold at y=844.
107 components measured. Findings: 2 broken, 0 likely wrong, 10 to check.
Not measured: 1 hidden component inside Anchor, 13 hidden components inside Div, 1 hidden component inside Anchor, 1 hidden component inside Anchor, 1 hidden component inside HorizontalLayout. Hidden tabs and panels are not rendered, so nothing below describes them.

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

- CUT: Avatar (Div[1] > HorizontalLayout[1] > Avatar[1])
  content is 38px wide in a 36px box: 2px not shown

- CUT: Avatar (Div[1] > HorizontalLayout[1] > Avatar[1])
  content is 41px tall in a 36px box: 5px not shown

### Check - often deliberate; compare with what you intended

- NEAR MISS: HorizontalLayout (Div[1] > HorizontalLayout[1])
  top edge is +2px from the y=10 its 7 siblings and neighbours share

- OFF SCALE: Div (Div[1])
  padding (top, bottom) 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[1])
  padding (right, left) 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: HorizontalLayout (Div[1] > HorizontalLayout[1])
  gap 9px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[1] > Div[1] > Div[1])
  gap 5px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[2] > Div[1] > Div[1] > Div[2]); Div (Div[2] > Div[2] > Div[1] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[2] > Div[2])
  gap 20px is not on the theme's spacing scale (nearest --vaadin-gap-l = 16px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1])
  gap 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)
  Also: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[3] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[4] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[5] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[6] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[7] > Div[1]); and 4 more

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1])
  padding 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)
  Also: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[3] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[4] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[5] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[6] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[7] > Div[1]); and 4 more

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1] > Div[1])
  gap 1px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[3] > Div[1] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[4] > Div[1] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[5] > Div[1] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[6] > Div[1] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[7] > Div[1] > Div[1]); and 4 more

- ORPHAN HEADING: H2 "Reports" (Div[2] > Div[1] > H2[1])
  the last thing in Div, with nothing under it

## Layout tree

ReportsView  0,0 390x3778  block
  y: 0 [60] 0 [3718] 0
  ? Div  0,0 390x60  row pad 10/14/10/14 gap8 align:center <- off-scale spacing
    x: 0 [96] 8 [214] 8 [36] 0
    Image  14,10 96x40
    Div  118,10 214x40  row gap4
      x: 0 [38] 4 [38] 4 [38] 4 [92] -4
      Anchor  118,10 38x38  row pad 0/8/0/8 gap7 align:center margin 0/0/2/0
      Anchor  160,10 38x38  row pad 0/8/0/8 gap7 align:center margin 0/0/2/0
      Anchor  202,10 38x38  row pad 0/8/0/8 gap7 align:center margin 0/0/2/0
      Anchor "#nav-reports"  244,10 92x38  row pad 0/8/0/8 gap7 align:center margin 0/0/2/0
        x: 27 [47] 0
        Span "Reports"  280,19 47x20
    ? HorizontalLayout  340,12 36x36  row gap9 align:center <- near miss <- off-scale spacing
      x: -2 [40] -2
      !! Avatar  338,10 40x40  w=36px h=36px margin -2/-2/-2/-2 <- cut off
  Div  0,60 390x3718  block
    y: 0 [78] 0 [3640] 0
    Div  0,60 390x78  block pad 12/16/12/16
      y: 0 [22] 2 [30] -1
      Span "Sales"  16,72 358x22
      ? H2 "Reports"  16,96 358x30  margin 2/0/0/0 <- nothing under it
    Div  0,138 390x3640  block pad16
      y: 0 [131] 22 [3455] 0
      Div  16,154 358x131  block gap24 margin 0/0/22/0
        y: 0 [73] 16 [42] 0
        Div  16,154 358x73  grid margin 0/0/16/0
          x: 0 [119] 0 [119] 0 [119] 0
          ? Div  16,154 119x73  col pad 0/8/0/0 gap5 33% of parent width <- off-scale spacing
            y: 0 [20] 5 [28] 20
            Span "2026 average sales"  16,154 111x20
            Span "168 640 €"  16,179 111x28
          ? Div  135,154 119x73  col pad 0/8/0/8 gap5 33% of parent width <- off-scale spacing
            y: 0 [20] 5 [28] 20
            Span "March 2026 sales"  143,154 103x20
            Span "174 610 €"  143,179 103x28
          ? Div  255,154 119x73  col pad 0/8/0/8 gap5 33% of parent width <- off-scale spacing
            y: 0 [40] 5 [28] 0
            Span "February 2026 sales"  263,154 103x40
            Span "127 080 €"  263,199 103x28
        Button "New report"  16,243 137x42
      ? Div  16,307 358x3455  col gap20 align:start <- off-scale spacing
        y: 0 [286] 20 [3149] 0
        Div  16,307 358x286  col gap16
          y: 0 [26] 16 [72] 16 [72] 16 [68] 0
          H3 "Filters"  16,307 358x26
          TextField "Free search"  16,349 358x72  w=100%
          MultiSelectComboBox "Regions"  16,437 358x72  w=100%
          Div  16,525 358x68  grid gap 0/4
            x row1 (y=525): 0 [358] 0
            x row2 (y=545): 0 [169] 4 [12] 4 [169] 0
            Span "Date range"  16,525 358x20
            DatePicker  16,545 169x48
            Span "–"  189,545 12x48
            DatePicker  205,545 169x48
        Div  16,613 358x3149  grid gap12
          y: 0 [275] 12 [275] 12 [275] 12 [275] 12 [275] 12 [275] 12 [275] 12 [275] 12 [275] 12 [275] 12 [275] 0
          Div  16,613 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,614 356x209
            ? Div  17,823 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [87] 195 [54] 0
              ? Div  27,835 87x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Deutschland"  27,835 87x20
                Span "March 2026"  27,856 87x19
              Span "Unread"  309,844 54x22  margin 0/0/0/185
          Div  16,900 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,901 356x209
            ? Div  17,1111 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [73] 209 [54] 0
              ? Div  27,1123 73x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Czechia"  27,1123 73x20
                Span "March 2026"  27,1144 73x19
              Span "Unread"  309,1132 54x22  margin 0/0/0/199
          Div  16,1188 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,1189 356x209
            ? Div  17,1398 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [73] 263
              ? Div  27,1410 73x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Sweden"  27,1410 73x20
                Span "March 2026"  27,1431 73x19
          Div  16,1475 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,1476 356x209
            ? Div  17,1686 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [73] 263
              ? Div  27,1698 73x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Austria"  27,1698 73x20
                Span "March 2026"  27,1719 73x19
          Div  16,1763 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,1764 356x209
            ? Div  17,1973 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [73] 263
              ? Div  27,1985 73x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Finland"  27,1985 73x20
                Span "March 2026"  27,2006 73x19
          Div  16,2050 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,2051 356x209
            ? Div  17,2260 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [89] 247
              ? Div  27,2272 89x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Deutschland"  27,2272 89x20
                Span "February 2026"  27,2293 89x19
          Div  16,2337 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,2338 356x209
            ? Div  17,2548 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [89] 247
              ? Div  27,2560 89x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Czechia"  27,2560 89x20
                Span "February 2026"  27,2581 89x19
          Div  16,2625 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,2626 356x209
            ? Div  17,2835 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [89] 247
              ? Div  27,2847 89x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Norway"  27,2847 89x20
                Span "February 2026"  27,2868 89x19
          Div  16,2912 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,2913 356x209
            ? Div  17,3123 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [89] 247
              ? Div  27,3135 89x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Sweden"  27,3135 89x20
                Span "February 2026"  27,3156 89x19
          Div  16,3200 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,3201 356x209
            ? Div  17,3410 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [89] 247
              ? Div  27,3422 89x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Austria"  27,3422 89x20
                Span "February 2026"  27,3443 89x19
          Div  16,3487 358x275  block
            y: 0 [209] 0 [64] 0
            Image  17,3488 356x209
            ? Div  17,3697 356x64  row pad10 gap10 align:center <- off-scale spacing
              x: 0 [89] 247
              ? Div  27,3709 89x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Finland"  27,3709 89x20
                Span "February 2026"  27,3730 89x19

