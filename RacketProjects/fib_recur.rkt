#lang Racket


;; (fibI n) -> integer
;   n : integer
(define fibI
    (lambda (number)
      (if (or (= number 1) (= number 2))
          1
          (fib_iter (- number 2) 1 1))))

 (define fib_iter
   (lambda (number  last second_last)
     (if (= number 0)
         last
         (fib_iter (- number 1) (+ second_last last) last))))
   


      
        ; Your definition here
        ; Note: you’ll need a helper function called fib-iter


(fibI 1)
(fibI 2)
(fibI 3)
(fibI 4)
(fibI 5)
(fibI 6)
(fibI 7)
(fibI 8)
(fibI 9)