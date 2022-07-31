#lang racket
; Start Basel Function
(define (basel x)
  ; if x less than 2
  (if (< x 2)
      ; return 1.0/x**
      (/ 1.0 (* x x))
      ;else: 1.0/x*x + 1.0/(x - 1.0)**
      (+ (/ 1.0 (* x x)) (basel (- x 1.0)))))
; End Basel Function

(basel 100)