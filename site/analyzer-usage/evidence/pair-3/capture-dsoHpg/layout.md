Capture: current viewport and UI state only; 0/124 visible components have source references. Geometry stable over three 100ms samples; fonts ready. This does not establish that asynchronous data or future state changes are complete.

## Repeated relationships

Peers have matching component structure; shared geometry is evidence, not a design requirement. Insets below use physical left edges, including borders.

- first-child left inset: 12/14 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1] > Div[1]).
  - Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[2]) uses 24px (24px difference). Verify intent.
  - Div (App > ReportsView[1] > Div[2] > Div[2] > Div[1] > Div[1] > Div[3]) uses 24px (24px difference). Verify intent.
- first-child left inset: 9/9 peers use 1px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[3]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[4]).
- first-child left inset: 9/9 peers use 16px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[3] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[2] > Div[2] > Div[2] > Div[4] > Div[1]).

# Layout: /reports

ReportsView
Viewport 1440x1024. View 1440x1191 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 167px down. Content ends at x=1440 y=1191. Fold at y=1024.
124 components measured. Findings: 2 broken, 0 likely wrong, 9 to check.

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

- OFF SCALE: Div (Div[1] > Div[1])
  gap 2px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)

- OFF SCALE: HorizontalLayout (Div[1] > HorizontalLayout[1])
  gap 9px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[2] > Div[1])
  padding (top) 18px is not on the theme's spacing scale (nearest --vaadin-gap-l = 16px)

- OFF SCALE: Div (Div[2] > Div[1])
  padding (bottom) 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[1] > Div[1] > Div[1])
  gap 5px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[2] > Div[1] > Div[1] > Div[2]); Div (Div[2] > Div[2] > Div[1] > Div[1] > Div[3])

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[2])
  gap 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1])
  gap 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)
  Also: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[3] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[4] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[5] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[6] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[7] > Div[1]); and 4 more

- OFF SCALE: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1] > Div[1])
  gap 1px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[2] > Div[1] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[3] > Div[1] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[4] > Div[1] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[5] > Div[1] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[6] > Div[1] > Div[1]); Div (Div[2] > Div[2] > Div[2] > Div[2] > Div[7] > Div[1] > Div[1]); and 4 more

- ORPHAN HEADING: H2 "Reports" (Div[2] > Div[1] > H2[1])
  the last thing in Div, with nothing under it

## Layout tree

ReportsView  0,0 1440x1191  row
  x: 0 [272] 0 [1168] 0
  Div  0,0 272x1191  col pad 24/16/16/16
    y: 0 [56] 20 [532] 499 [44] 0
    Image  24,24 138x56  margin 0/8/20/8
    ? Div  16,100 240x532  col gap2 <- off-scale spacing
      y: 0 [40] 20 [20] 10 [40] 4 [40] 4 [40] 20 [20] 10 [40] 4 [40] 4 [40] 20 [20] 10 [40] 4 [40] 2
      Anchor  16,100 240x40  row pad 0/10/0/10 gap16 align:center margin 0/0/2/0
        x: 36 [85] 97
        Span "Dashboard"  63,110 85x20
      Div "Sales"  16,160 240x20  margin 16/0/8/0
      Anchor  16,190 240x40  row pad 0/10/0/10 gap16 align:center margin 0/0/2/0
        x: 36 [54] 128
        Span "Orders"  63,200 54x20
      Anchor  16,234 240x40  row pad 0/10/0/10 gap16 align:center margin 0/0/2/0
        x: 36 [74] 108
        Span "Deliveries"  63,244 74x20
      Anchor "#nav-reports"  16,278 240x40  row pad 0/10/0/10 gap16 align:center margin 0/0/2/0
        x: 36 [60] 122
        Span "Reports"  63,288 60x20
      Div "Resources"  16,338 240x20  margin 16/0/8/0
      Anchor  16,368 240x40  row pad 0/10/0/10 gap16 align:center margin 0/0/2/0
        x: 36 [82] 100
        Span "Employees"  63,378 82x20
      Anchor  16,412 240x40  row pad 0/10/0/10 gap16 align:center margin 0/0/2/0
        x: 36 [77] 105
        Span "Utilisation"  63,422 77x20
      Anchor  16,456 240x40  row pad 0/10/0/10 gap16 align:center margin 0/0/2/0
        x: 36 [52] 130
        Span "Payroll"  63,466 52x20
      Div "Admin"  16,516 240x20  margin 16/0/8/0
      Anchor  16,546 240x40  row pad 0/10/0/10 gap16 align:center margin 0/0/2/0
        x: 36 [157] 25
        Span "Access management"  63,556 157x20
      Anchor  16,590 240x40  row pad 0/10/0/10 gap16 align:center margin 0/0/2/0
        x: 36 [62] 120
        Span "Settings"  63,600 62x20
    ? HorizontalLayout  16,1131 240x44  row pad 8/0/0/0 gap9 align:center margin 499/0/0/0 <- off-scale spacing
      x: -2 [40] 7 [136] 59
      !! Avatar  14,1137 40x40  w=36px h=36px margin -2/-2/-2/-2 <- cut off
      Span "Firstname Lastname"  61,1147 136x20
  Div  272,0 1168x1191  block
    y: 0 [90] 0 [1101] 0
    ? Div  272,0 1168x90  block pad 18/24/14/24 <- off-scale spacing
      y: 0 [22] 2 [30] 3
      Span "Sales"  296,18 1120x22
      ? H2 "Reports"  296,42 1120x30  margin 2/0/0/0 <- nothing under it
    Div  272,90 1168x1101  block pad24
      y: 0 [64] 24 [965] 0
      Div  296,114 1120x64  row gap24 align:center margin 0/0/24/0
        x: 0 [959] 24 [137] 0
        Div  296,116 959x61  grid
          x: 0 [320] 0 [320] 0 [320] 0
          ? Div  296,116 320x61  col pad 0/24/0/0 gap5 33% of parent width <- off-scale spacing
            y: 0 [20] 5 [36] 0
            Span "2026 average sales"  296,116 295x20
            Span "168 640 €"  296,141 295x36
          ? Div  616,116 320x61  col pad 0/24/0/24 gap5 33% of parent width <- off-scale spacing
            y: 0 [20] 5 [36] 0
            Span "March 2026 sales"  640,116 271x20
            Span "174 610 €"  640,141 271x36
          ? Div  935,116 320x61  col pad 0/24/0/24 gap5 33% of parent width <- off-scale spacing
            y: 0 [20] 5 [36] 0
            Span "February 2026 sales"  959,116 272x20
            Span "127 080 €"  959,141 272x36
        Button "New report"  1279,122 137x48
      Div  296,202 1120x965  grid gap24
        x: 0 [300] 24 [796] 0
        Div  296,202 300x292  col gap16 27% of parent width
          ... 8 components inside, none flagged
        ? Div  620,202 796x965  grid gap14 71% of parent width <- off-scale spacing
          x row1 (y=202): 0 [256] 14 [256] 14 [256] 0
          x row2 (y=447): 0 [256] 14 [256] 14 [256] 0
          x row3 (y=692): 0 [256] 14 [256] 14 [256] 0
          x row4 (y=936): 0 [256] 14 [256] 270
          Div  620,202 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  621,203 254x159
            ? Div  621,362 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [98] 56 [68] 0
              ? Div  637,377 98x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Deutschland"  637,377 98x20
                Span "March 2026"  637,398 98x19
              Span "Unread"  791,384 68x26  margin 0/0/0/46
          Div  890,202 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  891,203 254x159
            ? Div  891,362 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [83] 71 [68] 0
              ? Div  907,377 83x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Czechia"  907,377 83x20
                Span "March 2026"  907,398 83x19
              Span "Unread"  1061,384 68x26  margin 0/0/0/61
          Div  1160,202 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  1161,203 254x159
            ? Div  1161,362 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [83] 139
              ? Div  1177,377 83x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Sweden"  1177,377 83x20
                Span "March 2026"  1177,398 83x19
          Div  620,447 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  621,448 254x159
            ? Div  621,607 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [83] 139
              ? Div  637,622 83x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Austria"  637,622 83x20
                Span "March 2026"  637,643 83x19
          Div  890,447 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  891,448 254x159
            ? Div  891,607 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [83] 139
              ? Div  907,622 83x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Finland"  907,622 83x20
                Span "March 2026"  907,643 83x19
          Div  1160,447 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  1161,448 254x159
            ? Div  1161,607 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [100] 122
              ? Div  1177,622 100x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Deutschland"  1177,622 100x20
                Span "February 2026"  1177,643 100x19
          Div  620,692 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  621,693 254x159
            ? Div  621,851 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [100] 122
              ? Div  637,866 100x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Czechia"  637,866 100x20
                Span "February 2026"  637,887 100x19
          Div  890,692 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  891,693 254x159
            ? Div  891,851 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [100] 122
              ? Div  907,866 100x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Norway"  907,866 100x20
                Span "February 2026"  907,887 100x19
          Div  1160,692 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  1161,693 254x159
            ? Div  1161,851 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [100] 122
              ? Div  1177,866 100x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Sweden"  1177,866 100x20
                Span "February 2026"  1177,887 100x19
          Div  620,936 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  621,937 254x159
            ? Div  621,1096 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [100] 122
              ? Div  637,1111 100x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Austria"  637,1111 100x20
                Span "February 2026"  637,1132 100x19
          Div  890,936 256x231  block 32% of parent width
            y: 0 [159] 0 [70] 0
            Image  891,937 254x159
            ? Div  891,1096 254x70  row pad 12/16/12/16 gap10 align:center <- off-scale spacing
              x: 0 [100] 122
              ? Div  907,1111 100x40  col gap1 <- off-scale spacing
                y: 0 [20] 1 [19] 0
                Span "Finland"  907,1111 100x20
                Span "February 2026"  907,1132 100x19

