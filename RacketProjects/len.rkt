#lang Racket

(define atomic?
  (lambda (thing)
    (not (list? thing))))



(define len
  (lambda (list number)
    (cond ((empty? list) 0)
          ((atomic? list) (len (cdr list) (+ number 1)))
          (not (atomic? list) (len (cdr list) number)))))
    
    
     