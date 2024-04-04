#lang Racket
;CONTRACT
;(sum_range lower_number higher_number) -» int
;lower_number: interger that is smaller than the one in highest number
;highest_number: integer that is larger than the one in smaller number
;output: int


;DESCRIPTION
;returns the sum of the range of ints from lowest number to highest number



;DEFINITION
;function
(define sum_range
  (lambda (lower_number highest_number)
    (if (= lower_number highest_number)
        lower_number
        (+ highest_number (sum_range lower_number (- highest_number 1))))))

;definition for ckeck_expect function
(define check_expect
  (lambda (expression expected_value)
    (if (equal? expression expected_value)
        "test passed"
        "test failed"
        )))

;unit tests
(check_expect (sum_range 1 3) 6)
(check_expect (sum_range 2 3) 5)
(check_expect (sum_range 3 3) 3)
