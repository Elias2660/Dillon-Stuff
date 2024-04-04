#lang Racket

;; (my_odd? n) -> bool, true if odd, false if even
; n: non-zero integer


(define my_odd?
  (lambda (n) (not (= (round (/ n 2)) (/ n 2)))))
  
  

(my_odd? 3)

(my_odd? 2)

(my_odd? -3)
