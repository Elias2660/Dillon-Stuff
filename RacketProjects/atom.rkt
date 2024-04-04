#lang Racket


(define atom?
  (lambda (list)
    (not (list? list))))


(define atomic?
  (lambda (x)
    (or (not (list? x)) (empty? x))))
