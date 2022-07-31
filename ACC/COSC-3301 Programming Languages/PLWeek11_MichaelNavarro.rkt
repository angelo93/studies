#lang racket

;-------------------- Imports --------------------
(require racket/draw)  ; graphics library
(require colors) ; colors library

;====================================================
;                Start Helper Functions
;====================================================

;-------------------- Start Print Polygon --------------------
; Used for debugging, not used in runtime of program
(define (printPoly inPoly)
        (begin
          (define-values (whuh huh) (send inPoly get-datum))
          (display (vector->list (first (car whuh))))
          (newline)
          (display (vector->list (second (car whuh))))
          (newline)
          (display (vector->list (third (car whuh))))
          (newline)
          (display (vector->list (fourth (car whuh))))
          (newline)
          (newline)
          )
  )

(define (getXCoordinate inPoly)
  (begin
    ; Get coordinates for each vertex of polygon
    (define-values (closed_params open_params) (send inPoly get-datum))
    ; Convert first vector pair of coordinates to list and get x coordinate
    (car (vector->list (car (car closed_params))))
    )
  )

(define (getYCoordinate inPoly)
  (begin
    ; Get coordinates for each vertex of polygon
    (define-values (closed_params open_params) (send inPoly get-datum))
    ; Convert first vector pair of coordinates to list and get y coordinate
    (second (vector->list (car (car closed_params))))
    )
  )

(define (getXTrans inPoly)
  ; Convert world x coordinate to screen x coordinate
  (+ (* (getXCoordinate inPoly) .42666) 256)
  )

(define (getYTrans inPoly)
  ; Convert world y coordinate to screen y coordinate
  (+ (* (getYCoordinate inPoly) .42666) 144)
  )

;-------------------- Start Draw To Screen --------------------
(define (drawToScreen inPoly)
  (define current_xtrans 0) ; Track translation of x coordinate
  (define current_ytrans 0) ; Track translation of y coordinate

  ; Scale by a factor of .4266 to fit into screen space
  (send inPoly scale .42666 .42666) ; scale

  ; Get current translation amount, used to reverse translation later
  (set! current_xtrans (getXTrans inPoly))
  (set! current_ytrans (getYTrans inPoly))

  ; Translate polygon to fit into screen space
  (send inPoly translate (getXTrans inPoly) (getYTrans inPoly))
  
  (send dc draw-path inPoly) ; draw polygon

  ; Reverse conversion from world to screen space to get back to world space coordinates
  (send inPoly translate (* current_xtrans -1) (* current_ytrans -1))
  (send inPoly scale (/ 1 .42666) (/ 1 .42666)) ; scale
  )

;-------------------- Start Create Color Wheel --------------------
(define (create-color-wheel iterations inPoly hue)
  ; Predicate: if number of iterations goes down to 0
  (if (= iterations 0)
      ; True: Log that color wheel creation is done
      (display "Color Wheel has been created")
      ; Else: Loops remain to be done
      (let ()
        ; set color
        (send dc set-pen (hsv->color (hsv hue 1.0 1.0)) 2 'solid) ; pen color   line_width   fill_mode
        (send dc set-brush (hsv->color (hsv hue 1.0 1.0)) 'solid)  ; fill color   fill_mode
        ; rotate and draw
        (send inPoly rotate .0698132) ; polygon rotate in radians
        (drawToScreen inPoly)
        ; Recursive call
        (create-color-wheel (- iterations 1) inPoly (+ hue .0111))
        )
      )
  )

;====================================================
;                    Start Main
;====================================================

;-------------------- Start Background --------------------
(define imageWidth 512)
(define imageHeight 288)

(define myTarget (make-bitmap imageWidth imageHeight)) ; A bitmap
(define dc (new bitmap-dc% [bitmap myTarget])) ; a drawing context

(send dc set-pen "green" 2 'solid) ; pen color   line_width   fill_mode
(send dc set-brush (make-color 153 50 204) 'solid)  ; fill color   fill_mode

(send dc draw-rectangle
      0 0      ; Top-left at (0, 0), 0 pixels down from top-left
      512 288) ; 512 pixels wide and 288 pixels high

;-------------------- Part 1: Polygon Manipulation --------------------
(define myPolygon (new dc-path%)) ; create polygon
(send myPolygon move-to -14 -14) ; 1st vertex
(send myPolygon line-to 14 -14) ; 2nd vertex
(send myPolygon line-to 6 14) ; 3rd vertex
(send myPolygon line-to -6 14) ; 4th vertex
(send myPolygon close)

(send dc set-pen "red" 2 'solid) ; pen color   line_width   fill_mode
(send dc set-brush (make-color 255 235 0) 'solid)  ; fill color   fill_mode

(drawToScreen myPolygon)

(send myPolygon translate 35 30)
(drawToScreen myPolygon)

(send myPolygon scale 3 2)
(drawToScreen myPolygon)

(send myPolygon translate 70 60)  

;-------------------- Part 2: Create Color Wheel --------------------
(create-color-wheel 90 myPolygon 0.0)

;-------------------- Save & Display --------------------
(send myTarget save-file "PLWeek11_MichaelNavarro.png" 'png) ; save image as png 
myTarget ; display image