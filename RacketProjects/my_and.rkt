;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname my_and) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))


(define my_and
  (lambda (a b)
    (not (or (not a) (not b)))))

(check-expect (my_and #t #t) #t)
(check-expect (my_and #t #f) #f)
(check-expect (my_and #f #t) #f)
(check-expect (my_and #f #f) #f)