#lang racket
;-------------------- Dev Notes --------------------
; My original solution involved some recursion and helper functions,
; however, after delving into the Racket documentation and
; this gem of a website https://beautifulracket.com/
; I was able to reduce everything into the solution you see before you
; The instructions only forbade the use of the reverse function and for
; extra credit, the append function. I adhered to these contraints.
; As such, I have chosen to go with this solution over my original lenghty one.

;-------------------- Start oddRevList Function --------------------
; Start oddRevList Function
(define (oddRevList lst)
  (let([odds (filter odd? lst)])
    (foldl cons '() odds)
    ))
; End oddRevList Function

;-------------------- Start Tests --------------------

(define lstA '(1 2 3 4 5 6 7 8))
(oddRevList lstA)

(define lstB '(3 5 2 3 7 1 2 3 1 8))
(oddRevList lstB)