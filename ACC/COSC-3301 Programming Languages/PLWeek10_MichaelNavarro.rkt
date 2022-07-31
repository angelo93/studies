#lang racket
;-------------------- Imports --------------------
(require racket/draw)  ; graphics library
(require colors) ; colors library

;-------------------- Start Create Color Wheel --------------------
(define (create-color-wheel iterations poly hue)
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
        (send poly rotate .0698132) ; polygon rotate in radians
        (send dc draw-path poly) ; draw it again
        (create-color-wheel (- iterations 1) poly (+ hue .0111))
        )
      )
  )

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
 
(send dc draw-path myPolygon) ; draw polygon

(send myPolygon translate 35 30) ; translate   
(send dc draw-path myPolygon) ; draw

(send myPolygon scale 3 2) ; scale
(send dc draw-path myPolygon)

(send myPolygon translate 70 60) ; translate   

;-------------------- Part 2: Create Color Wheel --------------------
(create-color-wheel 90 myPolygon 0.0)

;-------------------- Save & Display --------------------
(send myTarget save-file "PLWeek10_MichaelNavarro.png" 'png) ; save image as png 
myTarget ; display image