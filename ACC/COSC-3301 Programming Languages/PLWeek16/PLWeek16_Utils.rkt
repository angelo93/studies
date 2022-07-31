#lang racket

;====================================================
;                Start Helper Functions
;====================================================

;-------------------- Start Get Actions --------------------

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

(define (getXTrans inPoly xscale)
  ; Convert world x coordinate to screen x coordinate
  (+ (* (getXCoordinate inPoly) xscale) 1024)
  )

(define (getYTrans inPoly yscale)
  ; Convert world y coordinate to screen y coordinate
  (+ (* (getYCoordinate inPoly) yscale) 576)
  )

(define (getHueStep hue iterations cycles)
  ; Determines step to increase hue by number of iterations and number of hue cycles to complete
  ; Doesn't work as intended? Still affects color cycling though
  (define polysPerCycle (/ iterations cycles))
  ((/ (- 1 hue) (+ polysPerCycle .001)))
  )

(define (getVectorList inPoly)
  ; Get coordinates for each vertex of polygon
  (define-values (closed_params open_params) (send inPoly get-datum))
  (car closed_params)
  )

(provide getXCoordinate getYCoordinate getXTrans getYTrans getHueStep getVectorList)

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
    (display (vector->list (fifth (car whuh))))
    (newline)
    (newline)
    )
  )
(provide printPoly)

;-------------------- Start Zoom Helpers --------------------

(define (getNewYMin min max zoom_lvl)
  (- (/ (+ min max) 2) (* zoom_lvl (/ (+ min max) 2)))
  )

(define (getNewXMin min max zoom_lvl)
  (- (/ (+ min max) 2) (* zoom_lvl (/ (+ min max) 2)))
  )
(provide getNewYMin getNewXMin)
;-------------------- Start Decision Makers --------------------
(define (scale-poly? odds)
  (if (= (random odds) 0)
      true
      false)
  )

(define (rotate-poly? odds)
  (if (= (random odds) 0)
      true
      false)
  )

(define (rotate-right? odds)
  (if (= (random odds) 0)
      true
      false)
  )

(define (translate-poly? odds)
  (if (= (random odds) 0)
      true
      false)
  )

(define (translate-vertical? odds)
  (if (= (random odds) 0)
      true
      false)
  )

(define (translate-horizontal? odds)
  (if (= (random odds) 0)
      true
      false)
  )

(define (branch-poly? odds)
  (if (= (random odds) 0)
      true
      false)
  )

(define (branch-right? odds)
  (if (= (random odds) 0)
      true
      false)
  )

(provide scale-poly? rotate-poly? rotate-right? translate-poly? translate-vertical? translate-horizontal? branch-poly? branch-right?)