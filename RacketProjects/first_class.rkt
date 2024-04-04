;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname first_class) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))


;; (first_class can_afford_tickets airplane_have_seats) -> bool
; can_afford_tickets: bool
; airplane_have_seats: bool


(define first_class
  (lambda (can_afford_tickets airplane_have_seats)
    (if (and can_afford_tickets airplane_have_seats)
        "you can fly first class" "you cannot fly first class")))


;unit tests
(check-expect (first_class #t #t) "you can fly first class")

(check-expect (first_class #f #t) "you cannot fly first class")

(check-expect (first_class #t #f) "you cannot fly first class")

(check-expect (first_class #f #f) "you cannot fly first class")
