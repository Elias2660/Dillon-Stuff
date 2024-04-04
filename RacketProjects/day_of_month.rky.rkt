;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname day_of_month.rky) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; (xor a b) -> boolean
;    a : boolean
;    b : boolean
(define xor 
     (λ(a b)
     	 (cond ((or (and a b) (not (and a b))) false)
               (else true))))


; (divisor? n d) -> boolean
;    n : integer
;    d : integer.   Assume d is not zero.
(define divisor?
  (λ(n d)
   (cond ((= (remainder n d) 0) true)
         (else false))))


;; (leap-year? year) -> boolean
;       year : integer
(define leap-year?
  (λ(year)
     (cond ((and (divisor? year 100) (not (divisor? year 400))) false)
           ((divisor? year 4) true)
           (else false))))


;; (days-in-month m y) -> integer
;         m     : integer   Assume 1 <= m <= 12.
;         y     : integer
(define days-in-month
  (λ(m y)
     (cond ( (or (= m 4)
                 (= m 9)
                 (= m 6)
                 (= m 11)) 30)
           ( (and (= m 2) (leap-year? y)) 29)
           ( (= m 2) 28)
           (else 31))))
         
           

;; unit tests
(check-expect  (days-in-month 2 2016)  29)
(check-expect  (days-in-month 2 2100)  28)
(check-expect  (days-in-month 6 2000)  30)
(check-expect  (days-in-month 7 2016)  31)


