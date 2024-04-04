;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname factorial) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define !
  (lambda (n)
    (if (= n 1)
       1
       (* n (! (- n 1))))))

;unit tests
(check-expect (! 3) 6)
(check-expect (! 4) 24)
(check-expect (! 5) 120)
(check-expect (! 2) 2)
(check-expect (! 1) 1)