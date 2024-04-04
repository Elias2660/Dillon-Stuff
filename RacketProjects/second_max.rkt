#lang racket


(define second_max
  (lambda (a b c d e) (max (min a b) (min a c) (min a d) (min a e)
                           (min b c) (min b d) (min b e)
                           (min c d) (min d e)
                           (min d e)
    )))