;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname test_1) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define rrp (lambda (l w h)
              (+ (* l w)
                 (* l (sqrt (+ (expt (/ w 2) 2 ) (expt h 2))))
                 (* w (sqrt (+ (expt (/ l 2) 2)
                               (expt h 2)))))
              ))
