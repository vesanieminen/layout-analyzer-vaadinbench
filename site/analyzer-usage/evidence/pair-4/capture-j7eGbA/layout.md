Capture: current viewport and UI state only; 0/121 visible components have source references. Geometry stable over three 100ms samples; fonts ready. This does not establish that asynchronous data or future state changes are complete.

## Repeated relationships

Peers have matching component structure; shared geometry is evidence, not a design requirement. Insets below use physical left edges, including borders.

- first-child left inset: 12/14 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[1] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[1] > Div[2] > Div[1] > Div[1] > Div[1] > Div[1]).
  - Div (App > ReportsView[1] > Div[2] > Div[1] > Div[1] > Div[2]) uses 22px (22px difference). Verify intent.
  - Div (App > ReportsView[1] > Div[2] > Div[1] > Div[1] > Div[3]) uses 24px (24px difference). Verify intent.
- first-child left inset: 9/9 peers use 1px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[1] > Div[2] > Div[1] > Div[3]); Div (App > ReportsView[1] > Div[2] > Div[1] > Div[2] > Div[1] > Div[4]).
- first-child left inset: 9/9 peers use 16px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[1] > Div[2] > Div[1] > Div[3] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[1] > Div[2] > Div[1] > Div[4] > Div[1]).

# Layout: /reports

ReportsView
Viewport 1440x1024. View 1440x1024 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls in neither axis. Content ends at x=1440 y=1164. Fold at y=1024.
Content reaches 140px past the view's bottom edge while the page does not scroll: something scrolls or clips it inside (see findings).
121 components measured. Findings: 2 broken, 0 likely wrong, 8 to check.
Not measured: 1 hidden component inside Div. Hidden tabs and panels are not rendered, so nothing below describes them.

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
  content is 42px wide in a 40px box: 2px not shown

- CUT: Avatar (Div[1] > HorizontalLayout[1] > Avatar[1])
  content is 46px tall in a 40px box: 6px not shown

### Check - often deliberate; compare with what you intended

- SCROLLS INSIDE: Div (Div[2] > Div[1])
  1168x1098px, reaches 164px past the bottom of Div (1168x1024px); Div scrolls it inside its own box
  Fix: if the whole content should be visible: let the container grow (drop its fixed height, or setWidthFull instead of setSizeFull on the view)

- OFF SCALE: Div (Div[1])
  padding (top) 22px is not on the theme's spacing scale (nearest --vaadin-gap-xl = 24px)

- OFF SCALE: Div (Div[2] > Div[1] > Div[1] > Div[1])
  gap 2px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[1] > Div[1] > Div[2]); Div (Div[2] > Div[1] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[1] > Div[1] > Div[2])
  padding (left) 22px is not on the theme's spacing scale (nearest --vaadin-gap-xl = 24px)

- OFF SCALE: Div (Div[2] > Div[1] > Div[2] > Div[1])
  row-gap 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[1] > Div[1])
  padding (top, bottom) 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)
  Also: Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[2] > Div[1]); Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[3] > Div[1]); Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[4] > Div[1]); Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[5] > Div[1]); Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[6] > Div[1]); Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[7] > Div[1]); and 4 more

- EMPTY: Div (Div[1] > Div[1])
  contains nothing and takes 240x348px

- ORPHAN HEADING: H1 "Reports" (Div[2] > HorizontalLayout[1] > VerticalLayout[1] > H1[1])
  the last thing in VerticalLayout, with nothing under it

## Layout tree

ReportsView  0,0 1440x1024  row
  x: 0 [272] 0 [1168] 0
  ? Div  0,0 272x1024  col pad 22/16/16/16 <- off-scale spacing
    y: 0 [58] 24 [40] 17 [18] 9 [128] 17 [18] 9 [128] 17 [18] 9 [84] 0 [348] 0 [44] 0
    Image  16,22 144x58  margin 0/0/24/0
    SideNav  16,104 240x40  block gap4
      y: 0 [40] 0
      SideNavItem "Dashboard"  16,104 240x40
    Span "Sales"  18,161 236x18  margin 17/2/9/2
    SideNav  16,188 240x128  block gap4
      y: 0 [40] 4 [40] 4 [40] 0
      SideNavItem "Orders"  16,188 240x40
      SideNavItem "Deliveries"  16,232 240x40
      SideNavItem "Reports"  16,276 240x40
    Span "Resources"  18,333 236x18  margin 17/2/9/2
    SideNav  16,360 240x128  block gap4
      y: 0 [40] 4 [40] 4 [40] 0
      SideNavItem "Employees"  16,360 240x40
      SideNavItem "Utilisation"  16,404 240x40
      SideNavItem "Payroll"  16,448 240x40
    Span "Admin"  18,505 236x18  margin 17/2/9/2
    SideNav  16,532 240x84  block gap4
      y: 0 [40] 4 [40] 0
      SideNavItem "Access management"  16,532 240x40
      SideNavItem "Settings"  16,576 240x40
    ? Div  16,616 240x348  <- empty
    HorizontalLayout  16,964 240x44  row gap8 align:center
      x: 0 [44] 8 [188] 0
      !! Avatar  16,964 44x44  <- cut off
      Button "Firstname Lastname"  68,975 188x22
  Div  272,0 1168x1024  col scrolls
    y: 0 [90] 0 [1098] -164
    HorizontalLayout  272,0 1168x90  row pad 0/24/0/24 align:center
      x: 0 [1120] 0
      VerticalLayout  296,19 1120x51  col align:start justify:center w=100%
        y: 0 [22] 0 [29] 0
        Span "Sales"  296,19 39x22
        ? H1 "Reports"  296,41 86x29  <- nothing under it
    ? Div  272,90 1168x1098  block pad24 <- scrolls inside parent
      y: 0 [66] 22 [962] 0
      Div  296,114 1120x66  grid margin 0/0/22/0
        x: 0 [226] 0 [248] 0 [504] 0 [142] 0
        ? Div  296,114 226x66  col pad 0/24/0/0 gap2 justify:center 20% of parent width <- off-scale spacing
          y: 3 [22] 2 [36] 3
          Span "2026 average sales"  296,117 201x22
          Span "168 640 €"  296,141 201x36
        ? Div  522,114 248x66  col pad 0/24/0/22 gap2 justify:center 22% of parent width <- off-scale spacing
          y: 3 [22] 2 [36] 3
          Span "March 2026 sales"  544,117 201x22
          Span "174 610 €"  544,141 201x36
        ? Div  770,114 504x66  col pad 0/24/0/24 gap2 justify:center 45% of parent width <- off-scale spacing
          y: 3 [22] 2 [36] 3
          Span "February 2026 sales"  794,117 456x22
          Span "127 080 €"  794,141 456x36
        Button "New report"  1274,123 142x48
      Div  296,202 1120x962  grid gap24
        x: 0 [300] 24 [796] 0
        VerticalLayout  296,202 300x292  col align:start w=100% 27% of parent width
          ... 10 components inside, none flagged
        ? Div  620,202 796x962  grid gap 14/16 71% of parent width <- off-scale spacing
          x row1 (y=202): 0 [255] 16 [255] 16 [255] 0
          x row2 (y=446): 0 [255] 16 [255] 16 [255] 0
          x row3 (y=690): 0 [255] 16 [255] 16 [255] 0
          x row4 (y=934): 0 [255] 16 [255] 271
          Div  620,202 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  621,203 253x158
            ? Div  621,361 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [101] 52 [68] 0
              Div  637,375 101x42  col
                y: 0 [22] 0 [20] 0
                Span "Deutschland"  637,375 101x22
                Span "March 2026"  637,397 101x20
              Span "Unread"  790,382 68x27
          Div  891,202 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  892,203 253x158
            ? Div  892,361 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [83] 70 [68] 0
              Div  908,375 83x42  col
                y: 0 [22] 0 [20] 0
                Span "Czechia"  908,375 83x22
                Span "March 2026"  908,397 83x20
              Span "Unread"  1060,382 68x27
          Div  1161,202 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  1162,203 253x158
            ? Div  1162,361 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [83] 138
              Div  1178,375 83x42  col
                y: 0 [22] 0 [20] 0
                Span "Sweden"  1178,375 83x22
                Span "March 2026"  1178,397 83x20
          Div  620,446 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  621,447 253x158
            ? Div  621,605 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [83] 138
              Div  637,619 83x42  col
                y: 0 [22] 0 [20] 0
                Span "Austria"  637,619 83x22
                Span "March 2026"  637,641 83x20
          Div  891,446 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  892,447 253x158
            ? Div  892,605 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [83] 138
              Div  908,619 83x42  col
                y: 0 [22] 0 [20] 0
                Span "Finland"  908,619 83x22
                Span "March 2026"  908,641 83x20
          Div  1161,446 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  1162,447 253x158
            ? Div  1162,605 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [102] 119
              Div  1178,619 102x42  col
                y: 0 [22] 0 [20] 0
                Span "Deutschland"  1178,619 102x22
                Span "February 2026"  1178,641 102x20
          Div  620,690 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  621,691 253x158
            ? Div  621,849 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [102] 119
              Div  637,863 102x42  col
                y: 0 [22] 0 [20] 0
                Span "Czechia"  637,863 102x22
                Span "February 2026"  637,885 102x20
          Div  891,690 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  892,691 253x158
            ? Div  892,849 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [102] 119
              Div  908,863 102x42  col
                y: 0 [22] 0 [20] 0
                Span "Norway"  908,863 102x22
                Span "February 2026"  908,885 102x20
          Div  1161,690 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  1162,691 253x158
            ? Div  1162,849 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [102] 119
              Div  1178,863 102x42  col
                y: 0 [22] 0 [20] 0
                Span "Sweden"  1178,863 102x22
                Span "February 2026"  1178,885 102x20
          Div  620,934 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  621,935 253x158
            ? Div  621,1093 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [102] 119
              Div  637,1107 102x42  col
                y: 0 [22] 0 [20] 0
                Span "Austria"  637,1107 102x22
                Span "February 2026"  637,1129 102x20
          Div  891,934 255x230  block 32% of parent width
            y: 0 [158] 0 [70] 0
            Image  892,935 253x158
            ? Div  892,1093 253x70  row pad 10/16/10/16 gap8 align:center justify:between <- off-scale spacing
              x: 0 [102] 119
              Div  908,1107 102x42  col
                y: 0 [22] 0 [20] 0
                Span "Finland"  908,1107 102x22
                Span "February 2026"  908,1129 102x20

