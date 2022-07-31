#lang racket
;--------------------- Start Helper Functions ---------------------
; Start testAccuracy
(define (testAcc ans)
  (if (= (abs(/ (floor(* 1000.0 ans)) 1000.0)) .001)
      1
      -1))
; End testAccuracy

; Start getAvg
(define (getAvg a b)
  (/ (+ a b) 2.0))
; End getAvg

;---------------------- Start Poly Functions ----------------------
; Start polynomial function
; 5x^2-x-8
(define (polyOne x)
  (-(-(* 5 (* x x)) x) 8))
; End polynomial function

; Start polynomial function
; 4x^2-x-2
(define (polyTwo x)
  (-(-(* 4 (* x x)) x) 2))
; End polynomial function

;-------------------- Start Bisection Function --------------------
; Start Bisection Function
(define (zeroBisection polyFunc x1 x2)
  ; find y values
  (let([y1 (polyFunc x1)]
       [y2 (polyFunc x2)]
       [midx (getAvg x1 x2)])
    (cond
      ; Case 1: f(x) is within limit, root found.
      [(= (testAcc (polyFunc midx)) 1) (display midx)]
      ; Case 2: y1 * midy < 0
      [(< (* y1 (polyFunc midx)) 0)
       (zeroBisection polyFunc x1 midx)]
      ; Case 2: y2 * midy < 0
      [(< (* y2 (polyFunc midx)) 0)
       (zeroBisection polyFunc x2 midx)]
      [else "Error"]
  )))
; End Bisection Function

(printf"A zero for 5x^2-x-8 is: ")
(zeroBisection polyOne 1 2)
(printf"\n")
(printf"A zero for 4x^2-x-2 is: ")
(zeroBisection polyTwo -1 0)
