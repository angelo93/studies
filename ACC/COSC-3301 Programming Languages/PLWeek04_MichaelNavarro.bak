#lang racket
;-------------------- Start Leibniz Series V1 --------------------
;Finds the sign for nth iteration
(define (findSign i)
  ; Predicate: If even number
  (if (= 0 (modulo i 2))
      1 ; If True: return 1
      -1 ; If : false return -1
      ))
; End findSign

; Evaluates Leibniz to 100 terms
(define (leibnizV1 x)
  ; Predicate: if on the 100th term
  (if (= 100.0 x)
      ; Sign is checked in case hard coded stopping point is odd
      (* (findSign x) (/ 1 (+ (* x 2) 1)))
      ; else add current quitient with proceeding quitient
      (+ (* (findSign x) (/ 1 (+ (* x 2) 1))) (leibnizV1 (+ x 1.0)))
      ))
; end leibnizV1

;-------------------- End Leibniz Series V1 --------------------

;-------------------- Start Leibniz Series V2 --------------------
;Finds the sign for nth iteration


; Evaluates Leibniz to 100 terms
(define (leibnizV2 x)
  ; Predicate: if on the 100th term
  (if (= 100.0 x)
      ; Sign is checked in case hard coded stopping point is odd
      (* ((lambda (i) (if (= 0 (modulo i 2))
                       1 -1))x) (/ 1 (+ (* x 2) 1)))
      ; else add current quitient with proceeding quitient
      (+ (* ((lambda (i) (if (= 0 (modulo i 2))
                             1 -1))x) (/ 1 (+ (* x 2) 1))) (leibnizV2 (+ x 1.0)))
      ))
; end leibnizV1

;-------------------- End Leibniz Series V2 --------------------

; Test starting variables
(define startV1 0)
(define startV2 0)

; Test function calls
(leibnizV1 startV1)
(leibnizV2 startV2)

