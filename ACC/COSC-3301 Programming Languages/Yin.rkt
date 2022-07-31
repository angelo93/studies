#lang racket

(require 2htdp/image)

(define (swoosh image s)
    (cond
      [(zero? s) image]
      [else (swoosh
             (overlay/align "center" "top"
                            (circle (* s 1/2) "solid" "white")
                            (rotate 4 image))
             (- s 1))]))

(swoosh (circle 100 "solid" "black")
          94)