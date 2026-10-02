Capture: current viewport and UI state only; 0/103 visible components have source references. Geometry stable over three 100ms samples; fonts ready. This does not establish that asynchronous data or future state changes are complete.

## Repeated relationships

Peers have matching component structure; shared geometry is evidence, not a design requirement. Insets below use physical left edges, including borders.

- first-child left inset: 12/14 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[1] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[1] > Div[2] > Div[1] > Div[1] > Div[1] > Div[1]).
  - Div (App > ReportsView[1] > Div[2] > Div[1] > Div[1] > Div[2]) uses 8px (8px difference). Verify intent.
  - Div (App > ReportsView[1] > Div[2] > Div[1] > Div[1] > Div[3]) uses 8px (8px difference). Verify intent.
- first-child left inset: 9/9 peers use 1px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[1] > Div[2] > Div[1] > Div[3]); Div (App > ReportsView[1] > Div[2] > Div[1] > Div[2] > Div[1] > Div[4]).
- first-child left inset: 9/9 peers use 10px. Witnesses: Div (App > ReportsView[1] > Div[2] > Div[1] > Div[2] > Div[1] > Div[3] > Div[1]); Div (App > ReportsView[1] > Div[2] > Div[1] > Div[2] > Div[1] > Div[4] > Div[1]).

# Layout: /reports

ReportsView
Viewport 390x844. View 390x3659 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 2815px down. Content ends at x=390 y=3659. Fold at y=844.
103 components measured. Findings: 0 broken, 0 likely wrong, 5 to check.
Not measured: 9 hidden components inside Div. Hidden tabs and panels are not rendered, so nothing below describes them.

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

- OFF SCALE: Div (Div[2] > Div[1] > Div[1])
  gap 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)

- OFF SCALE: Div (Div[2] > Div[1] > Div[1] > Div[1])
  gap 2px is not on the theme's spacing scale (nearest --vaadin-gap-xs = 4px)
  Also: Div (Div[2] > Div[1] > Div[1] > Div[2]); Div (Div[2] > Div[1] > Div[1] > Div[3])

- OFF SCALE: VerticalLayout (Div[2] > Div[1] > Div[2] > VerticalLayout[1])
  gap 14px is not on the theme's spacing scale (nearest --vaadin-gap-m = 12px)

- OFF SCALE: Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[1] > Div[1])
  padding (right, left) 10px is not on the theme's spacing scale (nearest --vaadin-gap-s = 8px)
  Also: Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[2] > Div[1]); Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[3] > Div[1]); Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[4] > Div[1]); Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[5] > Div[1]); Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[6] > Div[1]); Div (Div[2] > Div[1] > Div[2] > Div[1] > Div[7] > Div[1]); and 4 more

- ORPHAN HEADING: H1 "Reports" (Div[2] > HorizontalLayout[1] > VerticalLayout[1] > H1[1])
  the last thing in VerticalLayout, with nothing under it

## Layout tree

ReportsView  0,0 390x3659  block
  y: 0 [68] 0 [3591] 0
  Div  0,0 390x68  row pad 12/16/12/16 gap12 align:center justify:between
    x: 0 [92] 160 [106] 0
    Image  16,15 92x37  margin 0/148/0/0
    Anchor  268,15 106x38  row pad 8/12/8/12 gap8 align:center
      x: 26 [54] 0
      Span "Reports"  307,24 54x20
  Div  0,68 390x3591  col
    y: 0 [78] 0 [3513] 0
    HorizontalLayout  0,68 390x78  row pad 0/16/0/16 align:center
      x: 0 [358] 0
      VerticalLayout  16,81 358x51  col align:start justify:center w=100%
        y: 0 [22] 0 [29] 0
        Span "Sales"  16,81 39x22
        ? H1 "Reports"  16,103 86x29  <- nothing under it
    Div  0,146 390x3513  block pad16
      y: 0 [126] 20 [3335] 0
      ? Div  16,162 358x126  grid gap10 margin 0/0/20/0 <- off-scale spacing
        x row1 (y=162): 0 [174] 10 [174] 0
        x row2 (y=230): 0 [174] 61 [123] 0
        ? Div  16,162 174x58  col pad 0/8/0/0 gap2 justify:center 49% of parent width <- off-scale spacing
          y: 6 [17] 2 [27] 6
          Span "2026 average sales"  16,168 165x17
          Span "168 640 €"  16,187 165x27
        ? Div  200,162 174x58  col pad 0/8/0/8 gap2 justify:center 49% of parent width <- off-scale spacing
          y: 6 [17] 2 [27] 6
          Span "March 2026 sales"  208,168 157x17
          Span "174 610 €"  208,187 157x27
        ? Div  16,230 174x58  col pad 0/8/0/8 gap2 justify:center 49% of parent width <- off-scale spacing
          y: 6 [17] 2 [27] 6
          Span "February 2026 sales"  24,236 158x17
          Span "127 080 €"  24,255 158x27
        Button "New report"  251,238 123x42
      Div  16,308 358x3335  grid gap16
        y: 0 [292] 16 [3027] 0
        ? VerticalLayout  16,308 358x292  col gap 0/14 align:start w=100% <- off-scale spacing
          y: 0 [25] 17 [19] 5 [48] 17 [19] 5 [48] 17 [19] 5 [48] 0
          H2 "Filters"  16,308 56x25  margin 0/0/17/0
          Span "Free search"  16,350 78x19  margin 0/0/5/0
          TextField  16,374 358x48  w=100% margin 0/0/17/0
          Span "Regions"  16,439 54x19  margin 0/0/5/0
          MultiSelectComboBox  16,463 358x48  w=100% margin 0/0/17/0
          Span "Date range"  16,528 75x19  margin 0/0/5/0
          HorizontalLayout  16,552 358x48  grid
            x: 0 [173] 4 [5] 4 [173] 0
            DatePicker  16,552 173x48
            Span "-"  193,566 5x20
            DatePicker  201,552 173x48
        Div  16,616 358x3027  grid gap12
          y: 0 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 0
          Div  16,616 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,617 356x200
            ? Div  17,817 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 196 [51] 0
              Div  27,830 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Deutschland"  27,830 89x20
                Span "March 2026"  27,850 89x17
              Span "Unread"  312,836 51x25
          Div  16,892 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,893 356x200
            ? Div  17,1094 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 212 [51] 0
              Div  27,1106 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Czechia"  27,1106 73x20
                Span "March 2026"  27,1126 73x17
              Span "Unread"  312,1112 51x25
          Div  16,1169 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,1170 356x200
            ? Div  17,1370 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 263
              Div  27,1382 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Sweden"  27,1382 73x20
                Span "March 2026"  27,1402 73x17
          Div  16,1445 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,1446 356x200
            ? Div  17,1646 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 263
              Div  27,1659 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Austria"  27,1659 73x20
                Span "March 2026"  27,1679 73x17
          Div  16,1721 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,1722 356x200
            ? Div  17,1922 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 263
              Div  27,1935 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Finland"  27,1935 73x20
                Span "March 2026"  27,1955 73x17
          Div  16,1997 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,1998 356x200
            ? Div  17,2199 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,2211 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Deutschland"  27,2211 89x20
                Span "February 2026"  27,2231 89x17
          Div  16,2274 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,2275 356x200
            ? Div  17,2475 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,2487 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Czechia"  27,2487 89x20
                Span "February 2026"  27,2507 89x17
          Div  16,2550 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,2551 356x200
            ? Div  17,2751 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,2764 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Norway"  27,2764 89x20
                Span "February 2026"  27,2784 89x17
          Div  16,2826 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,2827 356x200
            ? Div  17,3027 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,3040 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Sweden"  27,3040 89x20
                Span "February 2026"  27,3060 89x17
          Div  16,3102 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,3103 356x200
            ? Div  17,3304 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,3316 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Austria"  27,3316 89x20
                Span "February 2026"  27,3336 89x17
          Div  16,3379 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,3380 356x200
            ? Div  17,3580 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,3592 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Finland"  27,3592 89x20
                Span "February 2026"  27,3612 89x17

