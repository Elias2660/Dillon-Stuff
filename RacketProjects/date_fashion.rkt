;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname date_fashion) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;;  (date-fashion you date) -> integer
;    you : integer
;    date : integer

(define date-fashion
  (lambda (you date)
    (if (or (>= you 8) (>= date 8)) 2
        (if (or (<= you 2) (<= date 2)) 0 1))))
  
(date-fashion 5 10) ;-> 2
(date-fashion 5 2)  ;-> 0
(date-fashion 5 5)  ;-> 1
