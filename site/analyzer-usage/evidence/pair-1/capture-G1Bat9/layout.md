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
Viewport 390x844. View 390x3874 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 3030px down. Content ends at x=953 y=3874. Fold at y=844.
135 components measured. Findings: 2 broken, 0 likely wrong, 25 to check.
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
  content is 30px wide in a 28px box: 2px not shown

- CUT: Avatar (Div[1] > Div[2] > Avatar[1])
  content is 33px tall in a 28px box: 5px not shown

### Check - often deliberate; compare with what you intended

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[4])
  85x34px, reaches 36px past the right edge of Div (366x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[5])
  101x34px, reaches 142px past the right edge of Div (366x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[6])
  99x34px, reaches 246px past the right edge of Div (366x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[7])
  78x34px, reaches 329px past the right edge of Div (366x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[8])
  160x34px, reaches 494px past the right edge of Div (366x50px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- SCROLLS INSIDE: Anchor (Div[1] > Div[1] > Anchor[9])
  88x34px, reaches 587px past the right edge of Div (366x50px); Div scrolls it inside its own box
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
  gap 5px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

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

ReportsView  0,0 390x3874  block
  y: 0 [100] 0 [3774] 0
  ? Div  0,0 390x100  grid pad 10/12/0/12 <- off-scale spacing
    x row1 (y=10): 0 [96] 238 [32] 0
    x row2 (y=50): 0 [366] 0
    Image  12,10 96x40
    ? Div  12,50 366x50  row pad 7/12/9/12 gap5 align:center <- off-scale spacing
      x: 0 [103] 5 [79] 5 [96] 5 [85] 5 [101] 5 [99] 5 [78] 5 [160] 5 [88] -587
      Anchor  24,57 103x34  row pad 0/8/0/8 gap7 align:center
        x: 22 [63] 0
        Span "Dashboard"  55,68 63x12
      Anchor  132,57 79x34  row pad 0/8/0/8 gap7 align:center
        x: 22 [39] 0
        Span "Orders"  163,68 39x12
      Anchor  216,57 96x34  row pad 0/8/0/8 gap7 align:center
        x: 22 [56] 0
        Span "Deliveries"  247,68 56x12
      ? Anchor  317,57 85x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [45] 0
        Span "Reports"  348,68 45x12
      ? Anchor  407,57 101x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [61] 0
        Span "Employees"  438,68 61x12
      ? Anchor  513,57 99x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [59] 0
        Span "Utilisation"  544,68 59x12
      ? Anchor  617,57 78x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [38] 0
        Span "Payroll"  648,68 38x12
      ? Anchor  700,57 160x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [120] 0
        Span "Access management"  731,68 120x12
      ? Anchor  865,57 88x34  row pad 0/8/0/8 gap7 align:center <- scrolls inside parent
        x: 22 [48] 0
        Span "Settings"  896,68 48x12
    ? Div  346,10 32x40  row pad 0/2/0/2 align:center 9% of parent width <- off-scale spacing
      x: -2 [32] -2
      !! Avatar  346,14 32x32  margin -2/-2/-2/-2 <- cut off
  Div  0,100 390x3774  block
    y: 0 [76] 0 [131] 0 [3567] 0
    ? Div  0,100 390x76  col pad 9/16/10/16 justify:center <- off-scale spacing
      y: 6 [17] 2 [26] 6
      Span "Sales"  16,115 358x17
      Span "Reports"  16,134 358x26  margin 2/0/0/0
    ? Div  0,176 390x131  wrap pad 14/16/12/16 gap10 align:center <- off-scale spacing
      x row1 (y=190): 0 [358] 0
      x row2 (y=253): 0 [122] 236
      Div  16,190 358x53  row
        x: 0 [115] 0 [122] 0 [121] 0
        ? Div  16,190 115x53  col pad 0/6/0/0 gap8 justify:center <- off-scale spacing
          y: 4 [15] 8 [23] 4
          Span "2026 average sales"  16,194 108x15
          Span "168 640 €"  16,217 108x23
        ? Div  131,190 122x53  col pad 0/6/0/7 gap8 justify:center <- off-scale spacing
          y: 4 [15] 8 [23] 4
          Span "March 2026 sales"  138,194 108x15
          Span "174 610 €"  138,217 108x23
        ? Div  253,190 121x53  col pad 0/6/0/7 gap8 justify:center <- off-scale spacing
          y: 4 [15] 8 [23] 4
          Span "February 2026 sales"  260,194 108x15
          Span "127 080 €"  260,217 108x23
      Button "New report"  16,253 122x42
    ? Div  0,307 390x3567  grid pad 0/16/20/16 gap12 <- off-scale spacing
      y: 0 [309] 12 [3226] 0
      ? Div  16,307 358x309  col gap 4/14 <- off-scale spacing
        y: 0 [25] 12 [79] 13 [79] 13 [79] 9
        Span "Filters"  16,307 358x25  margin 0/0/8/0
        ? Div  16,344 358x79  col gap6 margin 0/0/9/0 <- off-scale spacing
          y: 0 [19] 6 [54] 0
          Span "Free search"  16,344 358x19
          TextField  16,369 358x54
        ? Div  16,436 358x79  col gap6 margin 0/0/9/0 <- off-scale spacing
          y: 0 [19] 6 [54] 0
          Span "Regions"  16,436 358x19
          MultiSelectComboBox  16,461 358x54
        ? Div  16,528 358x79  col gap6 margin 0/0/9/0 <- off-scale spacing
          y: 0 [19] 6 [54] 0
          Span "Date range"  16,528 358x19
          ? Div  16,553 358x54  row gap5 align:center <- off-scale spacing
            x: 0 [172] 5 [5] 5 [172] 0
            DatePicker  16,553 172x54
            Span "-"  193,570 5x20
            DatePicker  203,553 172x54
      Div  16,628 358x3226  grid gap12
        y: 0 [282] 12 [282] 12 [282] 12 [282] 12 [282] 12 [282] 12 [282] 12 [282] 12 [282] 12 [282] 12 [282] 0
        Div  16,628 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,629 356x209  block
            y: 0 [209] 0
            Image  17,629 356x209
          ? Div  17,838 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [98] 158 [68] 0
            ? Div  33,853 98x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Deutschland"  33,853 98x21
              Span "March 2026"  33,875 98x19
            Span "Unread"  289,859 68x28
        Div  16,922 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,923 356x209  block
            y: 0 [209] 0
            Image  17,923 356x209
          ? Div  17,1133 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 173 [68] 0
            ? Div  33,1147 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Czechia"  33,1147 83x21
              Span "March 2026"  33,1169 83x19
            Span "Unread"  289,1154 68x28
        Div  16,1217 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,1218 356x209  block
            y: 0 [209] 0
            Image  17,1218 356x209
          ? Div  17,1427 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 241
            ? Div  33,1442 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Sweden"  33,1442 83x21
              Span "March 2026"  33,1464 83x19
        Div  16,1511 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,1512 356x209  block
            y: 0 [209] 0
            Image  17,1512 356x209
          ? Div  17,1722 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 241
            ? Div  33,1736 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Austria"  33,1736 83x21
              Span "March 2026"  33,1758 83x19
        Div  16,1806 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,1807 356x209  block
            y: 0 [209] 0
            Image  17,1807 356x209
          ? Div  17,2016 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [83] 241
            ? Div  33,2031 83x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Finland"  33,2031 83x21
              Span "March 2026"  33,2053 83x19
        Div  16,2100 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,2101 356x209  block
            y: 0 [209] 0
            Image  17,2101 356x209
          ? Div  17,2310 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,2325 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Deutschland"  33,2325 100x21
              Span "February 2026"  33,2347 100x19
        Div  16,2394 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,2395 356x209  block
            y: 0 [209] 0
            Image  17,2395 356x209
          ? Div  17,2605 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,2619 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Czechia"  33,2619 100x21
              Span "February 2026"  33,2641 100x19
        Div  16,2689 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,2690 356x209  block
            y: 0 [209] 0
            Image  17,2690 356x209
          ? Div  17,2899 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,2914 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Norway"  33,2914 100x21
              Span "February 2026"  33,2936 100x19
        Div  16,2983 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,2984 356x209  block
            y: 0 [209] 0
            Image  17,2984 356x209
          ? Div  17,3194 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,3208 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Sweden"  33,3208 100x21
              Span "February 2026"  33,3230 100x19
        Div  16,3278 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,3279 356x209  block
            y: 0 [209] 0
            Image  17,3279 356x209
          ? Div  17,3488 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,3503 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Austria"  33,3503 100x21
              Span "February 2026"  33,3525 100x19
        Div  16,3572 358x282  block
          y: 0 [209] 0 [71] 0
          Div  17,3573 356x209  block
            y: 0 [209] 0
            Image  17,3573 356x209
          ? Div  17,3782 356x71  row pad 10/16/11/16 gap6 align:center justify:between <- off-scale spacing
            x: 0 [100] 224
            ? Div  33,3797 100x41  col gap1 <- off-scale spacing
              y: 0 [21] 1 [19] 0
              Span "Finland"  33,3797 100x21
              Span "February 2026"  33,3819 100x19

