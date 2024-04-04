#lang Racket

;Write the function (insertL a b L) that creates a list by inserting b to the left of the first occurrence of a in L.

(define copy-list
  (λ (L)
    (if (empty? L); base case where we ask if list is empty
        L         ; return list
        ; (cons x L) -> adds x to the front of list L
        (cons (car L) (copy-list (cdr L)))))) ; use cons

;(copy-list '(a b c))

(define insertL
  (λ (a b L)
    (if (empty? L)
        L
        (if (equal? (car L) a)
            (cons b (cons (car L) (insertL a b (cdr L))))
            (cons (car L) (insertL a b (cdr L)))))))

;Test Cases:
(insertL 'cat 'hat '(bat sat cat mat)) 
;-> (insertL '(bat sat cat mat))
;  =(cons 'bat (insertL '(sat cat mat))
;  =(cons 'bat (cons 'sat (insertL '(cat mat))))
;  =(cons 'bat (cons 'sat (cons 'hat (cons 'cat (insertL '(mat)))))
;  =(cons 'bat (cons 'sat (cons 'hat (cons 'cat (cons 'mat (insertL '()))))))
;  =(cons 'bat (cons 'sat (cons 'hat (cons 'cat (cons 'mat '()))))))
(insertL 6 5 '(1 2 3 4))
;-> '(1 2 3 4)