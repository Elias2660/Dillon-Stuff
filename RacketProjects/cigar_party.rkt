;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname cigar_party) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;;; contract

;;; (cigar_party cigars weekend) -> Boolean
;function specification
; returns true if cigars is between 40 and 60 or 
;if weekend is true and cigars is above 40
;else return false

; inputs and outputs
;  cigars : integer
;  weekend : bool


(define cigar_party
  (lambda (cigars weekend)
    (if (and (<= cigars 60) (>= cigars 40)) true
        (if (and (and weekend true) (>= cigars 40)) true false))))

;unit tests
(check-expect (cigar_party 30  false) false) ;-> false
(check-expect (cigar_party 50  false) true) ;-> true
(check-expect (cigar_party 70  true) true) ;-> true
