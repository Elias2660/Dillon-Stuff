#lang Racket

(define bunny_ears
  (lambda (bunny_number)
    (cond ((= bunny_number 0) 0)
          ((= (remainder bunny_number 2) 0) (+ 3 (bunny_ears (- bunny_number 1))))
          (else (+ 2 (bunny_ears (- bunny_number 1))))
          )))
          
          
 (bunny_ears 0)
 (bunny_ears 1)
 (bunny_ears 2)