Capture: current viewport and UI state only; 0/135 visible components have source references. Geometry stable over three 100ms samples; fonts ready. This does not establish that asynchronous data or future state changes are complete.

## Repeated relationships

Peers have matching component structure; shared geometry is evidence, not a design requirement. Insets below use physical left edges, including borders.

- first-child left inset: 12/15 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[1] > Div[2] > Div[1]).
  - Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[2]) uses 7px (7px difference). Verify intent.
  - Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[3]) uses 7px (7px difference). Verify intent.
  - Div (App > ReportsView[1] > Div[2] > Div[1]) uses 16px (16px difference). Verify intent.
- first-child left inset: 11/11 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[2] > Div[1]).
- first-child left inset: 9/9 peers use 1px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[3]); Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[4]).
- first-child left inset: 9/9 peers use 16px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[3] > Div[2]); Div (App > ReportsView[1] > Div[2] > Div[3] > Div[2] > Div[4] > Div[2]).

# Layout: /reports

ReportsView
Viewport 390x844. View 390x3903 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 3059px down. Content ends at x=941 y=3903. Fold at y=844.
135 components measured. Findings: 3 broken, 0 likely wrong, 25 to check.
Not measured: 6 hidden components inside Div, 1 hidden component inside Div. Hidden tabs and panels are not rendered, so nothing below describes them.

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
  content is 41px tall in a 32px box: 9px not shown

- ESCAPES: Div (Div[1] > Div[1])
  390x50px, sticks out of Div (content 366x130px) by 12px past the left edge and 12px past the right edge

### Check - often deliberate; compare with what you intended

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[4])
  85x34px, reaches 12px past the right edge of Div (390x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[5])
  101x34px, reaches 118px past the right edge of Div (390x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[6])
  99x34px, reaches 222px past the right edge of Div (390x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[7])
  78x34px, reaches 305px past the right edge of Div (390x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[8])
  160x34px, reaches 470px past the right edge of Div (390x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[9])
  88x34px, reaches 563px past the right edge of Div (390x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- OFF SCALE: Div (Div[1])
  padding (top) 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[1] > Div[1])
  gap 5px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

- OFF SCALE: Div (Div[1] > Div[1])
  padding (top) 7px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[1] > Div[1])
  padding (bottom) 9px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[1] > Div[2])
  padding (right, left) 2px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

- OFF SCALE: Div (Div[2] > Div[1])
  padding (top) 9px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[2] > Div[1])
  padding (bottom) 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[2] > Div[2])
  gap 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[2] > Div[2])
  padding (top) 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[1] > Div[1])
  padding (right) 6px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[2] > Div[1] > Div[2]); Div (Div[2] > Div[2] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[2] > Div[1] > Div[2])
  padding (left) 7px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)
  Also: Div (Div[2] > Div[2] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[3])
  padding (bottom) 20px is not on the theme's spacing scale (nearest --vaadin-gap-l = 16px)

- OFF SCALE: Div (Div[2] > Div[3] > Div[1])
  gap 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[3] > Div[1] > Div[1])
  gap 6px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[3] > Div[1] > Div[2]); Div (Div[2] > Div[3] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[3] > Div[1] > Div[3] > Div[1])
  gap 7px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

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

ReportsView  0,0 390x3903  block
  y: 0 [140] 0 [3763] 0
  ? Div  0,0 390x140  grid pad 10/12/0/12 <- off-scale spacing
    y: 0 [40] 0 [50] 0 [40] 0
    Image  12,10 96x40
    !! Div  0,50 390x50  row pad 7/12/9/12 gap5 align:center margin 0/-12/0/-12 <- escapes parent <- off-scale spacing
      x: 0 [103] 5 [79] 5 [96] 5 [85] 5 [101] 5 [99] 5 [78] 5 [160] 5 [88] -563
      Anchor  12,57 103x34  row pad 0/8/0/8 gap7 align:center
        x: 22 [63] 0
        Span "Dashboard"  43,68 63x12
      Anchor  120,57 79x34  row pad 0/8/0/8 gap7 align:center
        x: 22 [39] 0
        Span "Orders"  151,68 39x12
      Anchor  204,57 96x34  row pad 0/8/0/8 gap7 align:center
        x: 22 [56] 0
        Span "Deliveries"  235,68 56x12
      ? Anchor  305,57 85x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [45] 0
        Span "Reports"  336,68 45x12
      ? Anchor  395,57 101x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [61] 0
        Span "Employees"  426,68 61x12
      ? Anchor  501,57 99x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [59] 0
        Span "Utilisation"  532,68 59x12
      ? Anchor  605,57 78x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [38] 0
        Span "Payroll"  636,68 38x12
      ? Anchor  688,57 160x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [120] 0
        Span "Access management"  719,68 120x12
      ? Anchor  853,57 88x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [48] 0
        Span "Settings"  884,68 48x12
    ? Div  68,100 40x40  row pad 0/2/0/2 align:center 11% of parent width <- off-scale spacing
      x: -2 [40] -2
      !! Avatar  68,102 40x36  margin -2/-2/-2/-2 <- cut off
  Div  0,140 390x3763  block
    y: 0 [76] 0 [131] 0 [3556] 0
    ? Div  0,140 390x76  col pad 9/16/10/16 justify:center <- off-scale spacing
      y: 6 [17] 2 [26] 6
      Span "Sales"  16,155 358x17
      Span "Reports"  16,174 358x26  margin 2/0/0/0
    ? Div  0,216 390x131  wrap pad 14/16/12/16 gap10 align:center <- off-scale spacing
      x row1 (y=230): 0 [358] 0
      x row2 (y=293): 0 [122] 236
      Div  16,230 358x53  row
        x: 0 [115] 0 [122] 0 [121] 0
        ? Div  16,230 115x53  col pad 0/6/0/0 justify:center <- off-scale spacing
          y: 8 [15] 0 [23] 8
          Span "2026 average sales"  16,238 108x15
          Span "168 640 €"  16,253 108x23
        ? Div  131,230 122x53  col pad 0/6/0/7 justify:center <- off-scale spacing
          y: 8 [15] 0 [23] 8
          Span "March 2026 sales"  138,238 108x15
          Span "174 610 €"  138,253 108x23
        ? Div  253,230 121x53  col pad 0/6/0/7 justify:center <- off-scale spacing
          y: 8 [15] 0 [23] 8
          Span "February 2026 sales"  260,238 108x15
          Span "127 080 €"  260,253 108x23
      Button "New report"  16,293 122x42
    ? Div  0,347 390x3556  grid pad 0/16/20/16 gap12 <- off-scale spacing
      y: 0 [309] 12 [3215] 0
      ? Div  16,347 358x309  col gap 4/14 <- off-scale spacing
        y: 0 [25] 12 [79] 13 [79] 13 [79] 9
        Span "Filters"  16,347 358x25  margin 0/0/8/0
        ? Div  16,384 358x79  col gap6 margin 0/0/9/0 <- off-scale spacing
          y: 0 [19] 6 [54] 0
          Span "Free search"  16,384 358x19
          TextField  16,409 358x54
        ? Div  16,476 358x79  col gap6 margin 0/0/9/0 <- off-scale spacing
          y: 0 [19] 6 [54] 0
          Span "Regions"  16,476 358x19
          MultiSelectComboBox  16,501 358x54
        ? Div  16,568 358x79  col gap6 margin 0/0/9/0 <- off-scale spacing
          y: 0 [19] 6 [54] 0
          Span "Date range"  16,568 358x19
          ? Div  16,593 358x54  row gap7 align:center <- off-scale spacing
            x: 0 [170] 7 [5] 7 [170] 0
            DatePicker  16,593 170x54
            Span "-"  193,610 5x20
            DatePicker  205,593 170x54
      Div  16,668 358x3215  grid gap12
        y: 0 [281] 12 [281] 12 [281] 12 [281] 12 [281] 12 [281] 12 [281] 12 [281] 12 [281] 12 [281] 12 [281] 0
        Div  16,668 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,669 356x209  block
            y: 0 [209] 0
            Image  17,669 356x209
          ? Div  17,878 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [98] 158 [68] 0
            ? Div  33,892 98x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Deutschland"  33,892 98x21
              Span "March 2026"  33,914 98x19
            Span "Unread"  289,899 68x28
        Div  16,961 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,962 356x209  block
            y: 0 [209] 0
            Image  17,962 356x209
          ? Div  17,1172 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 173 [68] 0
            ? Div  33,1186 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Czechia"  33,1186 83x21
              Span "March 2026"  33,1208 83x19
            Span "Unread"  289,1192 68x28
        Div  16,1255 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,1256 356x209  block
            y: 0 [209] 0
            Image  17,1256 356x209
          ? Div  17,1465 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 241
            ? Div  33,1479 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Sweden"  33,1479 83x21
              Span "March 2026"  33,1501 83x19
        Div  16,1548 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,1549 356x209  block
            y: 0 [209] 0
            Image  17,1549 356x209
          ? Div  17,1759 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 241
            ? Div  33,1773 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Austria"  33,1773 83x21
              Span "March 2026"  33,1795 83x19
        Div  16,1842 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,1843 356x209  block
            y: 0 [209] 0
            Image  17,1843 356x209
          ? Div  17,2052 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 241
            ? Div  33,2066 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Finland"  33,2066 83x21
              Span "March 2026"  33,2088 83x19
        Div  16,2135 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,2136 356x209  block
            y: 0 [209] 0
            Image  17,2136 356x209
          ? Div  17,2345 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,2359 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Deutschland"  33,2359 100x21
              Span "February 2026"  33,2381 100x19
        Div  16,2428 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,2429 356x209  block
            y: 0 [209] 0
            Image  17,2429 356x209
          ? Div  17,2639 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,2653 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Czechia"  33,2653 100x21
              Span "February 2026"  33,2675 100x19
        Div  16,2722 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,2723 356x209  block
            y: 0 [209] 0
            Image  17,2723 356x209
          ? Div  17,2932 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,2946 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Norway"  33,2946 100x21
              Span "February 2026"  33,2968 100x19
        Div  16,3015 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,3016 356x209  block
            y: 0 [209] 0
            Image  17,3016 356x209
          ? Div  17,3226 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,3240 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Sweden"  33,3240 100x21
              Span "February 2026"  33,3262 100x19
        Div  16,3309 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,3310 356x209  block
            y: 0 [209] 0
            Image  17,3310 356x209
          ? Div  17,3519 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,3533 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Austria"  33,3533 100x21
              Span "February 2026"  33,3555 100x19
        Div  16,3602 358x281  block
          y: 0 [209] 0 [70] 0
          Div  17,3603 356x209  block
            y: 0 [209] 0
            Image  17,3603 356x209
          ? Div  17,3812 356x70  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,3826 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Finland"  33,3826 100x21
              Span "February 2026"  33,3848 100x19

