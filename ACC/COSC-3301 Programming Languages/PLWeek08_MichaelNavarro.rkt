#lang racket
(define (insertIntoBT binary_tree num)
  (cond
    ; Case 1: End found 
    []
    ; Case 2: num <= current leaf, go left
    []
    ; Case 3: num > current leaf, go right
    []
    ))

(define sorted_tree '(6 (3 (2) (5)) (7 () (9))))
(define empty_tree '())

(insert empty_tree 10)
(insert sorted_tree 2)