Capture: current viewport and UI state only; 0/103 visible components have source references. Geometry stable over three 100ms samples; fonts ready. This does not establish that asynchronous data or future state changes are complete.

## Repeated relationships

Peers have matching component structure; shared geometry is evidence, not a design requirement. Insets below use physical left edges, including borders.

- first-child left inset: 12/14 peers use 0px. Witnesses: Div (App > ReportsView[1] > Div[1] > Div[1] > Div[1] > Div[1]); Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2] > Div[1] > Div[1] > Div[1] > Div[1]).
  - Div (App > ReportsView[1] > Div[1] > Div[1] > Div[1] > Div[2]) uses 8px (8px difference). Verify intent.
  - Div (App > ReportsView[1] > Div[1] > Div[1] > Div[1] > Div[3]) uses 8px (8px difference). Verify intent.
- first-child left inset: 9/9 peers use 1px. Witnesses: Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2] > Div[1] > Div[3]); Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2] > Div[1] > Div[4]).
- first-child left inset: 9/9 peers use 10px. Witnesses: Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2] > Div[1] > Div[3] > Div[1]); Div (App > ReportsView[1] > Div[1] > Div[1] > Div[2] > Div[1] > Div[4] > Div[1]).

# Layout: /reports

ReportsView
Viewport 390x844. View 390x3702 at x=0 y=0; 0px free on its left, 0px on its right.
Page scrolls 2858px down. Content ends at x=390 y=3702. Fold at y=844.
103 components measured. Findings: 0 broken, 0 likely wrong, 5 to check.
Not measured: 9 hidden components inside VerticalLayout. Hidden tabs and panels are not rendered, so nothing below describes them.

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

ReportsView  0,0 390x3702  block
  y: 0 [111] 0 [3591] 0
  VerticalLayout  0,0 390x111  col pad 12/16/12/16 gap12 align:center justify:between w=100%
    y: 0 [37] 12 [38] 0
    Image  16,12 92x37  margin 0/266/0/0
    Anchor  142,61 106x38  row pad 8/12/8/12 gap8 align:center
      x: 26 [54] 0
      Span "Reports"  181,70 54x20
  Div  0,111 390x3591  col
    y: 0 [78] 0 [3513] 0
    HorizontalLayout  0,111 390x78  row pad 0/16/0/16 align:center
      x: 0 [358] 0
      VerticalLayout  16,124 358x51  col align:start justify:center w=100%
        y: 0 [22] 0 [29] 0
        Span "Sales"  16,124 39x22
        ? H1 "Reports"  16,146 86x29  <- nothing under it
    Div  0,189 390x3513  block pad16
      y: 0 [126] 20 [3335] 0
      ? Div  16,205 358x126  grid gap10 margin 0/0/20/0 <- off-scale spacing
        x row1 (y=205): 0 [174] 10 [174] 0
        x row2 (y=273): 0 [174] 61 [123] 0
        ? Div  16,205 174x58  col pad 0/8/0/0 gap2 justify:center 49% of parent width <- off-scale spacing
          y: 6 [17] 2 [27] 6
          Span "2026 average sales"  16,211 165x17
          Span "168 640 €"  16,230 165x27
        ? Div  200,205 174x58  col pad 0/8/0/8 gap2 justify:center 49% of parent width <- off-scale spacing
          y: 6 [17] 2 [27] 6
          Span "March 2026 sales"  208,211 157x17
          Span "174 610 €"  208,230 157x27
        ? Div  16,273 174x58  col pad 0/8/0/8 gap2 justify:center 49% of parent width <- off-scale spacing
          y: 6 [17] 2 [27] 6
          Span "February 2026 sales"  24,279 158x17
          Span "127 080 €"  24,298 158x27
        Button "New report"  251,281 123x42
      Div  16,351 358x3335  grid gap16
        y: 0 [292] 16 [3027] 0
        ? VerticalLayout  16,351 358x292  col gap 0/14 align:start w=100% <- off-scale spacing
          y: 0 [25] 17 [19] 5 [48] 17 [19] 5 [48] 17 [19] 5 [48] 0
          H2 "Filters"  16,351 56x25  margin 0/0/17/0
          Span "Free search"  16,393 78x19  margin 0/0/5/0
          TextField  16,417 358x48  w=100% margin 0/0/17/0
          Span "Regions"  16,482 54x19  margin 0/0/5/0
          MultiSelectComboBox  16,506 358x48  w=100% margin 0/0/17/0
          Span "Date range"  16,571 75x19  margin 0/0/5/0
          HorizontalLayout  16,595 358x48  grid
            x: 0 [173] 4 [5] 4 [173] 0
            DatePicker  16,595 173x48
            Span "-"  193,609 5x20
            DatePicker  201,595 173x48
        Div  16,659 358x3027  grid gap12
          y: 0 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 12 [264] 0
          Div  16,659 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,660 356x200
            ? Div  17,861 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 196 [51] 0
              Div  27,873 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Deutschland"  27,873 89x20
                Span "March 2026"  27,893 89x17
              Span "Unread"  312,879 51x25
          Div  16,936 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,937 356x200
            ? Div  17,1137 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 212 [51] 0
              Div  27,1149 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Czechia"  27,1149 73x20
                Span "March 2026"  27,1169 73x17
              Span "Unread"  312,1155 51x25
          Div  16,1212 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,1213 356x200
            ? Div  17,1413 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 263
              Div  27,1426 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Sweden"  27,1426 73x20
                Span "March 2026"  27,1446 73x17
          Div  16,1488 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,1489 356x200
            ? Div  17,1689 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 263
              Div  27,1702 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Austria"  27,1702 73x20
                Span "March 2026"  27,1722 73x17
          Div  16,1764 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,1765 356x200
            ? Div  17,1966 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [73] 263
              Div  27,1978 73x37  col
                y: 0 [20] 0 [17] 0
                Span "Finland"  27,1978 73x20
                Span "March 2026"  27,1998 73x17
          Div  16,2041 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,2042 356x200
            ? Div  17,2242 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,2254 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Deutschland"  27,2254 89x20
                Span "February 2026"  27,2274 89x17
          Div  16,2317 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,2318 356x200
            ? Div  17,2518 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,2531 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Czechia"  27,2531 89x20
                Span "February 2026"  27,2551 89x17
          Div  16,2593 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,2594 356x200
            ? Div  17,2794 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,2807 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Norway"  27,2807 89x20
                Span "February 2026"  27,2827 89x17
          Div  16,2869 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,2870 356x200
            ? Div  17,3071 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,3083 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Sweden"  27,3083 89x20
                Span "February 2026"  27,3103 89x17
          Div  16,3146 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,3147 356x200
            ? Div  17,3347 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,3359 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Austria"  27,3359 89x20
                Span "February 2026"  27,3379 89x17
          Div  16,3422 358x264  block
            y: 0 [200] 0 [62] 0
            Image  17,3423 356x200
            ? Div  17,3623 356x62  row pad 8/10/8/10 gap8 align:center justify:between <- off-scale spacing
              x: 0 [89] 247
              Div  27,3636 89x37  col
                y: 0 [20] 0 [17] 0
                Span "Finland"  27,3636 89x20
                Span "February 2026"  27,3656 89x17

