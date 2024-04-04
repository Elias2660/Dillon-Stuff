;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname my_sqrt) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;elias xu

(define distance ;distance function
  (lambda (x y)
    (abs (- x y))))

(define ε ;ε is actually epsilon i searched up and copied the epsilon symbol on google
  (lambda (x guess decimal_places)
    (< (distance (expt guess 2) x) (/ 1 (expt 10 decimal_places)))))

(define better_guess ;better_guess function, snake case rules lol
  (lambda (x guess)
    (/ (+ guess (/ x guess)) 2)))



(define my_sqrt ;my sqrt function
    (lambda (x guess decimal_places)
        (if (ε x guess decimal_places)
            guess
            (my_sqrt   x (better_guess x guess) decimal_places))))


;unit tests
(check-within (my_sqrt 16 1 3) 4 0.001)
(check-within (my_sqrt 25 1 4) 5 0.0001)
(check-within (my_sqrt 100 1 4) 10 0.0001)
(check-within (my_sqrt 234 1 4) (sqrt 234) 0.0001)
(check-within (my_sqrt 4 1 2) 2 0.01)



                