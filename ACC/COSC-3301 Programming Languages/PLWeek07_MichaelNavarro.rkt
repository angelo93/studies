#lang racket
;--------------------- Start Helper Functions ---------------------

; Start getMean
; Gets the mean of an array of numbers
(define (getMean nums)
  ; Convert to decimal point number.
  ; Conversion not needed, but decimal numbers are more readable to me when debugging.
  (exact->inexact (/ (apply + nums) (length nums)))
  )
; End getMean

;-------------------- Start Quicksort Function --------------------

; Start Quicksort
(define (myQuicksort num_list)
  ; If the list is empty mean gets assigned 0, fixes division by zero error
  (let ([mean (if (null? num_list) 0 (getMean num_list))])
    (cond
      ; Case 1: If list is null, return an empty list and start popping off the stack
      [(null? num_list) '()]
      ; Case 2a: If the first number is equal to the mean, then any and all numbers left are the same, return rest
      ; Case 2b: By extension, if the length of the list is one, also return rest.
      ;          This is because a number divided by 1 is itself.
      [(= (first num_list) mean) num_list]
      ; Case 3: Still iterating through list recursively
      [else
       (append (myQuicksort (filter (lambda (num) (< num mean)) num_list))
               ; The "=" is needed so that when filtering, we don't lose numbers that equal the mean
               (myQuicksort (filter (lambda (num) (>= num mean)) num_list)))]))
  )
; End Quicksort

;-------------------- Start Tests --------------------

; Test with HW list
(printf"Assignment Test\n")
(printf"Expected: ")
(sort '(20 13 74 5 12 9 22 95 22 6 101 72 3 53 33 21 96) <)
(printf"Result  : ")
(myQuicksort '(20 13 74 5 12 9 22 95 22 6 101 72 3 53 33 21 96))

; Test with random list and multiple duplicates
(printf"\nExtra Test\n")
(printf"Expected: ")
(sort '(308 389 155 141 309 169 325 45 72 294 404 406 138 11 395 177 45 309) <)
(printf"Result  : ")
(myQuicksort '(308 389 155 141 309 169 325 45 72 294 404 406 138 11 395 177 45 309))