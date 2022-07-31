#lang racket

;-------------------- Imports --------------------
(require racket/draw)  ; graphics library
(require colors) ; colors library

(require "PLWeek14_Utils.rkt")
(require "PLWeek14_Controls.rkt")

(random-seed 42)

;====================================================
;                Start Helper Functions
;====================================================

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

;====================================================
;                Start Loop Logic
;====================================================

;-------------------- Start Setters --------------------
(define (scale-poly inPolyOne inPolyTwo)
  (cond
    [(scale-poly? SCALE_ODDS)
     (send inPolyOne scale SCALE_STEP SCALE_STEP)
     (send inPolyTwo scale SCALE_STEP SCALE_STEP)
     ]
    )
  )

;-------------------- Start Translate Poly --------------------
(define (move-poly inPolyOne inPolyTwo)
  (cond
    [(translate-poly? TRANSLATE_ODDS)
     (cond
       [(and (translate-vertical? TRANSLATE_VERT_ODDS) (translate-horizontal? TRANSLATE_HORZ_ODDS))
        (send inPolyOne translate XTRANSLATE_STEP YTRANSLATE_STEP)
        (send inPolyTwo translate (* XTRANSLATE_STEP -1) (* YTRANSLATE_STEP -1))
        ]
       [(translate-horizontal? TRANSLATE_HORZ_ODDS)
        (send inPolyOne translate XTRANSLATE_STEP 0)
        (send inPolyTwo translate (* XTRANSLATE_STEP -1) 0)
        ]
       [(translate-vertical? TRANSLATE_VERT_ODDS)
        (send inPolyOne translate 0 YTRANSLATE_STEP)
        (send inPolyTwo translate 0 (* YTRANSLATE_STEP -1))
        ]
       )
     ])
  )

;-------------------- Start Rotate Poly --------------------
(define (rotate-poly inPolyOne inPolyTwo rotateStep)
  (cond
    [(rotate-poly? ROTATE_ODDS)
     (cond
       [(rotate-right? ROTATE_RIGHT_ODDS)
        (send inPolyOne rotate rotateStep)
        (send inPolyTwo rotate (* rotateStep -1))]
       [else
        (send inPolyTwo rotate rotateStep)
        (send inPolyOne rotate (* rotateStep -1))]
       )
     ]
    )
  )

;-------------------- Start Branch Polygons --------------------
(define (branch-poly inPolyOne inPolyTwo hue)
 
  (define polyOneCopy (new dc-path%)) ; create polygon
  (send polyOne move-to (first (vector->list (first (getVectorList inPolyOne)))) (second (vector->list (first (getVectorList inPolyOne))))) ; 1st vertex
  (send polyOne line-to (first (vector->list (second (getVectorList inPolyOne)))) (second (vector->list (second (getVectorList inPolyOne))))) ; 2nd vertex
  (send polyOne line-to (first (vector->list (third (getVectorList inPolyOne)))) (second (vector->list (third (getVectorList inPolyOne))))) ; 3rd vertex
  (send polyOne line-to (first (vector->list (fourth (getVectorList inPolyOne)))) (second (vector->list (fourth (getVectorList inPolyOne))))) ; 4th vertex
  (send polyOne line-to (first (vector->list (fifth (getVectorList inPolyOne)))) (second (vector->list (fifth (getVectorList inPolyOne))))) ; 5th vertex
  (send polyOne close)

  (define polyTwoCopy (new dc-path%)) ; create polygon
  (send polyOne move-to (first (vector->list (first (getVectorList inPolyTwo)))) (second (vector->list (first (getVectorList inPolyTwo))))) ; 1st vertex
  (send polyOne line-to (first (vector->list (second (getVectorList inPolyTwo)))) (second (vector->list (second (getVectorList inPolyTwo))))) ; 2nd vertex
  (send polyOne line-to (first (vector->list (third (getVectorList inPolyTwo)))) (second (vector->list (third (getVectorList inPolyTwo))))) ; 3rd vertex
  (send polyOne line-to (first (vector->list (fourth (getVectorList inPolyTwo)))) (second (vector->list (fourth (getVectorList inPolyTwo))))) ; 4th vertex
  (send polyOne line-to (first (vector->list (fifth (getVectorList inPolyTwo)))) (second (vector->list (fifth (getVectorList inPolyTwo))))) ; 5th vertex
  (send polyOne close)

  (cond
    [(branch-right? BRANCH_RIGHT_ODDS)
     (send inPolyOne rotate (* BRANCH_ANGLE -1))
     (send inPolyTwo rotate BRANCH_ANGLE)
     ]
    [else
     (send inPolyOne rotate BRANCH_ANGLE)
     (send inPolyTwo rotate (* BRANCH_ANGLE -1))
     ]
    )
  
  ; set color
  (send dc set-pen (hsv->color (hsv hue .65 1.0)) 2 'solid)  ; pen color   line_width   fill_mode
  (send dc set-brush (hsv->color (hsv hue .65 1.0)) 'solid)  ; fill color   fill_mode
     
  (drawToScreen inPolyOne)
  (drawToScreen inPolyTwo)
  
  (drawLoop polyOne polyTwo BRANCH_LENGTH hue)
  )

;-------------------- Start Main Draw Loop --------------------

(define (drawLoop inPolyOne inPolyTwo iterations hue)
  ; Reset Hue if getting close to limit of 1.0
  (if (>= hue HUE_MAX)
      (set! hue HUE_MIN)
      '())
  
  (define ROTATE_STEP (/ ROTATE_RADIANS (+ iterations .01)))
  (define HUE_STEP (/ (- 1 hue) (+ (/ iterations COLOR_CYCLES) .01)))
   
  (cond
    [(<= iterations 0)
     '()
     ]
    [else
     ; Decide if need to move
     (move-poly inPolyOne inPolyTwo)
     ; Decide if need to rotate
     (rotate-poly inPolyOne inPolyTwo ROTATE_STEP)
     ; Decide if need additionaly scaling
     (scale-poly inPolyOne inPolyTwo)

     ; Decide if going to branch
     (cond
       [(branch-poly? BRANCH_ODDS)
        (branch-poly inPolyOne inPolyTwo hue)
        (set! iterations (- iterations (* BRANCH_LENGTH 2)))
        ]
       )
     
     ; set color
     (send dc set-pen (hsv->color (hsv hue .65 1.0)) 2 'solid)  ; pen color   line_width   fill_mode
     (send dc set-brush (hsv->color (hsv hue .65 1.0)) 'solid)  ; fill color   fill_mode

     ; Draw polygons, comment one or the other for different effects
     (drawToScreen inPolyOne)
     (drawToScreen inPolyTwo)

     (drawLoop inPolyOne inPolyTwo (- iterations 1) (+ hue HUE_STEP))
     ]
    )
  )

;====================================================
;                    Start Main
;====================================================

;-------------------- Start Background --------------------
(define imageWidth 2048)
(define imageHeight 1152)

(define myTarget (make-bitmap imageWidth imageHeight)) ; A bitmap
(define dc (new bitmap-dc% [bitmap myTarget])) ; a drawing context

(send dc set-pen (make-color 25 25 65) 2 'solid) ; pen color   line_width   fill_mode
(send dc set-brush (make-color 25 25 65) 'solid)  ; fill color   fill_mode

(send dc draw-rectangle
      0 0      ; Top-left at (0, 0), 0 pixels down from top-left
      2048 1152)

;-------------------- Part 1: Setup --------------------
(define polyOne (new dc-path%))  ; create polygon
(send polyOne move-to 220 0)     ; 1st vertex
(send polyOne line-to 140 -160)  ; 2nd vertex
(send polyOne line-to -140 -160) ; 3rd vertex
(send polyOne line-to -220 0)    ; 4th vertex
(send polyOne line-to 0 360)     ; 5th vertex
(send polyOne close)

(define polyTwo (new dc-path%)) ; create polygon
(send polyTwo move-to -220 0)   ; 1st vertex
(send polyTwo line-to -140 160) ; 2nd vertex
(send polyTwo line-to 140 160)  ; 3rd vertex
(send polyTwo line-to 220 0)    ; 4th vertex
(send polyTwo line-to 0 -360)   ; 5th vertex
(send polyTwo close)

(send polyOne translate 0 -833)
(send polyTwo translate 0 833)

(drawLoop polyOne polyTwo ITERATIONS 0.0)

;-------------------- Save & Display --------------------
(send myTarget save-file "PLWeek14_MichaelNavarro.png" 'png) ; save image as png 
myTarget ; display image