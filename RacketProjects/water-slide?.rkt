;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname water-slide?) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; (water-slide? height age) -> String
; height: positive integer
; age: positive integer

(define water-slide?
  (lambda (height age)
    (if (or (>= age 14) (>= height 48)) "can ride" "cannot ride")))

; tests
(water-slide? 48 14) ;->"can ride"
(water-slide? 48 13) ;->"can ride"
(water-slide? 47 14) ;->"can ride"
(water-slide? 47 13) ;->"cannot ride"