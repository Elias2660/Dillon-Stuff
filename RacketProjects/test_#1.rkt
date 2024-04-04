;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname test_#1) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;break the equaiton down to three parts

(define my_first
  (lambda (l w) (* l w))) 

;break down the two fat square roots to 4 parts

(define second_root
  (lambda (h w)
    (sqrt (+ (expt (/ w 2) 2) (expt h 2)))))


(define my_second
  (lambda (l w h) (* l (second_root h w))))

(define third_root
  (lambda (l h)
    (sqrt (+ (expt (/ l 2) 2) (expt h 2)))))

(define my_third
  (lambda (l w h)
    (* w (third_root l h))))

;put it all down together

(define rrp
  (lambda (l w h)
    (+ (my_first l w)
       (my_second l w h)
       (my_third l w h))))

;test cases

(check-within (rrp 5 3 7) 73 .1)

(check-within (rrp 7 9 1) 128 .05)

(check-within (rrp 6 8 2) 103.6 .1)


