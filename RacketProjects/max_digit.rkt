#lang Racket

(define any_even_digit?
  (lambda (number)
    (if (<= number 10)
        (even? number)
        (or (even? (remainder number 10)) (any_even_digit? (/ (- number (remainder number 10)) 10)))
        )))



(any_even_digit? 235); -> true
(any_even_digit? 113355); -> false


;trace_diagram
(any_even_digit? 2349)
(or (even? 9) (any_even_digit? 234))
(or (even? 9) (or (even? 4) (any_even_digit? 23)))
(or (even? 9) (or (even? 4) (or (even? 3) (any_even_digit? 2))))
(or (even? 9) (or (even? 4) (or (even? 3) (even? 2))))
(or (even? 9) (or (even? 4) (or #f #t)))
(or (even? 9) (or #t #t))
(or #t #t)
#t

;used recursive function because the trace diagram gets bigger, the function is inside the function

