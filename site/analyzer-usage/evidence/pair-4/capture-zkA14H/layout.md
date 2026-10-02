Capture: current viewport and UI state only; 0/114 visible components have source references. Geometry stable over three 100ms samples; fonts ready. This does not establish that asynchronous data or future state changes are complete.

## Repeated relationships

Peers have matching component structure; shared geometry is evidence, not a design requirement. Insets below use physical left edges, including borders.

- first-child left inset: 12/14 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[1] > Div[1] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2] > Div[1] > Div[1] > Div[1] > Div[1]).
  - Div (App > ReportsView[1] > Div[1] > Div[1] > Div[1] > Div[2]) uses 8px (8px difference). Verify intent.
  - Div (App > ReportsView[1] > Div[1] > Div[1] > Div[1] > Div[3]) uses 8px (8px difference). Verify intent.
- first-child left inset: 9/9 peers use 1px. Witnesses: Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2] > Div[1] > Div[3]); Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2] > Div[1] > Div[4]).
- first-child left inset: 9/9 peers use 10px. Witnesses: Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2] > Div[1] > Div[3] > Div[1]); Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2] > Div[1] > Div[4] > Div[1]).

# Layout: /reports

ReportsView
Viewport 390x844. View 390x4133 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 3289px down. Content ends at x=390 y=4133. Fold at y=844.
114 components measured. Findings: 0 broken, 0 likely wrong, 9 to check.
Not measured: 5 hidden components inside VerticalLayout. Hidden tabs and panels are not rendered, so nothing below describes them.

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

### Check - often deliberate; compare with what you intended

- FORM EMPTY CELL: Image (VerticalLayout[1] > Image[1])
  row 1 (y=12px) fills 1 of 1 columns at this width: a 92px cell is empty beside Image, because SideNav starts a new row
  Fix: if not deliberate: move another single-column field up beside it, or make the following field single-column

- OFF SCALE: VerticalLayout (VerticalLayout[1])
  gap 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: HorizontalLayout (Div[1] > HorizontalLayout[1])
  padding (right, left) 18px is not on the theme's spacing scale (nearest --vaadin-gap-l = 16px)

- OFF SCALE: Div (Div[1] > Div[1])
  padding 18px is not on the theme's spacing scale (nearest --vaadin-gap-l = 16px)

- OFF SCALE: Div (Div[1] > Div[1] > Div[1])
  gap 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[1] > Div[1] > Div[1] > Div[1])
  gap 2px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[1] > Div[1] > Div[1] > Div[2]); Div (Div[1] > Div[1] > Div[1] > Div[3])

- OFF SCALE: VerticalLayout (Div[1] > Div[1] > Div[2] > VerticalLayout[1])
  gap 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[1] > Div[1] > Div[2] > Div[1] > Div[1] > Div[1])
  padding (right, left) 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)
  Also: Div (Div[1] > Div[1] > Div[2] > Div[1] > Div[2] > Div[1]); Div (Div[1] > Div[1] > Div[2] > Div[1] > Div[3] > Div[1]); Div (Div[1] > Div[1] > Div[2] > Div[1] > Div[4] > Div[1]); Div (Div[1] > Div[1] > Div[2] > Div[1] > Div[5] > Div[1]); Div (Div[1] > Div[1] > Div[2] > Div[1] > Div[6] > Div[1]); Div (Div[1] > Div[1] > Div[2] > Div[1] > Div[7] > Div[1]); and 4 more

- ORPHAN HEADING: H1 "Reports" (Div[1] > HorizontalLayout[1] > VerticalLayout[1] > H1[1])
  the last thing in VerticalLayout, with nothing under it

## Layout tree

ReportsView  0,0 390x4133  block
  y: 0 [563] 0 [3570] 0
  ? VerticalLayout  0,0 390x563  wrap pad 12/16/12/16 gap 8/14 align:center w=100% <- off-scale spacing
    x row1 (y=12): 0 [92] 266
    x row2 (y=57): 0 [358] 0
    x row3 (y=115): 0 [358] 0
    x row4 (y=281): 0 [358] 0
    x row5 (y=447): 0 [358] 0
    ? Image  16,12 92x37  margin 0/8/0/0 <- empty cell after
    SideNav  16,57 358x50  col gap4
      y: 0 [50] 0
      SideNavItem "Dashboard"  16,57 358x50
    SideNav  16,115 358x158  col gap4
      y: 0 [50] 4 [50] 4 [50] 0
      SideNavItem "Orders"  16,115 358x50
      SideNavItem "Deliveries"  16,169 358x50
      SideNavItem "Reports"  16,223 358x50
    SideNav  16,281 358x158  col gap4
      y: 0 [50] 4 [50] 4 [50] 0
      SideNavItem "Employees"  16,281 358x50
      SideNavItem "Utilisation"  16,335 358x50
      SideNavItem "Payroll"  16,389 358x50
    SideNav  16,447 358x104  col gap4
      y: 0 [50] 4 [50] 0
      SideNavItem "Access management"  16,447 358x50
      SideNavItem "Settings"  16,501 358x50
  Div  0,563 390x3570  col
    y: 0 [78] 0 [3492] 0
    ? HorizontalLayout  0,563 390x78  row pad 0/18/0/18 align:center <- off-scale spacing
      x: 0 [354] 0
      VerticalLayout  18,576 354x51  col align:start justify:center w=100%
        y: 0 [22] 0 [29] 0
        Span "Sales"  18,576 39x22
        ? H1 "Reports"  18,598 86x29  <- nothing under it
    ? Div  0,641 390x3492  block pad18 <- off-scale spacing
      y: 0 [126] 20 [3310] 0
      ? Div  18,659 354x126  grid gap10 margin 0/0/20/0 <- off-scale spacing
        x row1 (y=659): 0 [172] 10 [172] 0
        x row2 (y=727): 0 [172] 59 [123] 0
        ? Div  18,659 172x58  col pad 0/8/0/0 gap2 justify:center 49% of parent width <- off-scale spacing
          y: 6 [17] 2 [27] 6
          Span "2026 average sales"  18,665 163x17
          Span "168 640 €"  18,684 163x27
        ? Div  200,659 172x58  col pad 0/8/0/8 gap2 justify:center 49% of parent width <- off-scale spacing
          y: 6 [17] 2 [27] 6
          Span "March 2026 sales"  208,665 155x17
          Span "174 610 €"  208,684 155x27
        ? Div  18,727 172x58  col pad 0/8/0/8 gap2 justify:center 49% of parent width <- off-scale spacing
          y: 6 [17] 2 [27] 6
          Span "February 2026 sales"  26,733 156x17
          Span "127 080 €"  26,752 156x27
        Button "New report"  249,735 123x42
      Div  18,805 354x3310  grid gap16
        y: 0 [292] 16 [3002] 0
        ? VerticalLayout  18,805 354x292  col gap 0/14 align:start w=100% <- off-scale spacing
          y: 0 [25] 17 [19] 5 [48] 17 [19] 5 [48] 17 [19] 5 [48] 0
          H2 "Filters"  18,805 56x25  margin 0/0/17/0
          Span "Free search"  18,847 78x19  margin 0/0/5/0
          TextField  18,871 354x48  w=100% margin 0/0/17/0
          Span "Regions"  18,936 54x19  margin 0/0/5/0
          MultiSelectComboBox  18,960 354x48  w=100% margin 0/0/17/0
          Span "Date range"  18,1025 75x19  margin 0/0/5/0
          HorizontalLayout  18,1049 354x48  grid
            x: 0 [171] 4 [5] 4 [171] 0
            DatePicker  18,1049 171x48
            Span "-"  193,1063 5x20
            DatePicker  201,1049 171x48
        Div  18,1113 354x3002  grid gap12
          y: 0 [262] 12 [262] 12 [262] 12 [262] 12 [262] 12 [262] 12 [262] 12 [262] 12 [262] 12 [262] 12 [262] 0
          Div  18,1113 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,1114 352x198
            ? Div  19,1312 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 192 [51] 0
              Div  29,1325 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Deutschland"  29,1325 89x20
                Span "March 2026"  29,1345 89x17
              Span "Unread"  310,1331 51x25
          Div  18,1387 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,1388 352x198
            ? Div  19,1586 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 208 [51] 0
              Div  29,1599 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Czechia"  29,1599 73x20
                Span "March 2026"  29,1619 73x17
              Span "Unread"  310,1605 51x25
          Div  18,1661 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,1662 352x198
            ? Div  19,1860 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 259
              Div  29,1873 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Sweden"  29,1873 73x20
                Span "March 2026"  29,1893 73x17
          Div  18,1935 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,1936 352x198
            ? Div  19,2134 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 259
              Div  29,2147 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Austria"  29,2147 73x20
                Span "March 2026"  29,2167 73x17
          Div  18,2209 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,2210 352x198
            ? Div  19,2408 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 259
              Div  29,2421 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Finland"  29,2421 73x20
                Span "March 2026"  29,2441 73x17
          Div  18,2483 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,2484 352x198
            ? Div  19,2682 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 243
              Div  29,2695 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Deutschland"  29,2695 89x20
                Span "February 2026"  29,2715 89x17
          Div  18,2757 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,2758 352x198
            ? Div  19,2956 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 243
              Div  29,2969 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Czechia"  29,2969 89x20
                Span "February 2026"  29,2989 89x17
          Div  18,3031 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,3032 352x198
            ? Div  19,3230 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 243
              Div  29,3243 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Norway"  29,3243 89x20
                Span "February 2026"  29,3263 89x17
          Div  18,3305 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,3306 352x198
            ? Div  19,3504 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 243
              Div  29,3517 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Sweden"  29,3517 89x20
                Span "February 2026"  29,3537 89x17
          Div  18,3579 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,3580 352x198
            ? Div  19,3778 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 243
              Div  29,3791 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Austria"  29,3791 89x20
                Span "February 2026"  29,3811 89x17
          Div  18,3853 354x262  block
            y: 0 [198] 0 [62] 0
            Image  19,3854 352x198
            ? Div  19,4052 352x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 243
              Div  29,4065 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Finland"  29,4065 89x20
                Span "February 2026"  29,4085 89x17

