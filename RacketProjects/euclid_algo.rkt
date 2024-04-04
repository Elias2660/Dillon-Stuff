#lang Racket


(define euclid_algo
  (lambda (number_1 number_2)
    (cond ((= number_1 0) number_2)
          ((= number_2 0) number_1)
          ((> number_1 number_2) (euclid_algo number_2 (remainder number_1 number_2)))
          ((< number_1 number_2) (euclid_algo number_1 (remainder number_2 number_1)))
          )))
                                              
        
(euclid_algo 102 68) 