#lang racket

;====================================================
;                Start Controls
;====================================================
; General Rules
; *_ODDS: Higher number --> less likely to happen
;       : If set to 1, will always happen

(define ITERATIONS 50000)  ; Number of polygons to make (ITERATIONS * 2)
(provide ITERATIONS)

(define HUE_MIN 0.0)
(define HUE_MAX 0.9)
(define COLOR_CYCLES 16.8) ; How many complete color hue cycles (I don't actually think it works how I think it does)
(provide COLOR_CYCLES HUE_MIN HUE_MAX)

(define SCALE_STEP .9999) ; The closer to 1 and the more 9s there are, the bigger each new child polygon is.
(define SCALE_ODDS 1)     ; Whether to scale or not
(define XSCALE .42666)
(define YSCALE .42666)
(provide SCALE_STEP SCALE_ODDS XSCALE YSCALE)

(define TRANSLATE_ODDS 10)       ; Whether to translate
(define XTRANSLATE_STEP 10)       ; How many pixels to move horizontally
(define YTRANSLATE_STEP 1)       ; How many pixels to move vertically
(define TRANSLATE_VERT_ODDS 10)  ; Whether to do a vertical translate
(define TRANSLATE_HORZ_ODDS 5)   ; Whether to do a horizontal translate
(provide XTRANSLATE_STEP YTRANSLATE_STEP TRANSLATE_ODDS TRANSLATE_VERT_ODDS TRANSLATE_HORZ_ODDS)

(define ROTATE_ODDS 4)        ; Whether to rotate or not
(define ROTATE_RIGHT_ODDS 6)  ; Rotate right, if not, rotate left 
(define ROTATE_RADIANS 1000000)    ; Multiples of 6.283188 equate to one full circle
(provide ROTATE_ODDS ROTATE_RIGHT_ODDS ROTATE_RADIANS)

(define BRANCH_ODDS 5000)     ; Whether to branch or not, should be kept in the thousands
(define BRANCH_RIGHT_ODDS 2)  ; Whether to branch to the right
(define BRANCH_LENGTH 150)    ; The number of iterations (polygons) per branch
(define BRANCH_ANGLE 1.58)     ; Angle at which to branch in radians
(provide BRANCH_ODDS BRANCH_RIGHT_ODDS BRANCH_LENGTH BRANCH_ANGLE)
