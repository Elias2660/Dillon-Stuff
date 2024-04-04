;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname gauss_sum) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define sum_explicit
  (lambda (highest_term)
    (/ (* highest_term (+ highest_term 1)) 2)))


(define sum
  (lambda (n)
    (if (= n 1)
        1
        (+ n (sum (- n 1))))))