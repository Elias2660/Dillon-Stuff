;;This section of code defines all of the global variables.
;;created by seth fenton, elias xu, and dannyar akhmedov
globals [border
  on_x
  on_y
  box_height
  box_width
answer_word
  current_row_number
  current_row_contents
  entered
  running
]
breed [tletters tletter]

;;This is basically the code to the setup button and allows you to start playing wordle.
;;code is intended for the obeserver
;;Created by elias xu and seth fenton
to start_game
  clear-all
  create_world
  t_create_boxes
  choose_word
  create_empty current_row_number


end


;;This lets you pick the word that you’ll be trying to guess and makes it into a list of strings
;;intended for observer
;;created by seth fenton and elias xu
to choose_word
  ;;select the word randomly
  set answer_word one-of ["HELLO"
    "SHIQUE" "SLIPS" "TRIPS" "FALLS" "FLAMES"
    "ARSON" "DEATH" "STUFF" "ELIAS" "SETHS" "LBOZO"
    "MAKER" "SHOOT" "SCRIBE" "DONUT" "MUNCH" "PLANT"
    "SHEEPS" "MATEY" "ARMED" "ITEMS" "SWORD"]
  ;;split the word up
  set answer_word string_list answer_word
end

;;This is also part of the setup command and creates the optimal world size conditions for wordle
;;intended for patches and observer
;;created by seth fenton, dannyar akhmedov, and elias xu
to create_world
  resize-world -200 200 -280 280
  set border 10
  set-patch-size 1
  set current_row_number 6
  let wletter 0
  set guess ""
  set running True

end

;;This one’s pretty self explanatory but it makes the wordle boxes
;;intended for setup function, intended for observer
;;created by elias xu
to t_create_boxes


  ;create a 6x5 box that match the dimensions of the world
  set on_x max-pxcor - border

  ;create box height and width
  ;;loops and creates 5 x 6 spread of boxes
  set box_height round((world-height - (border * 7)) / 6) - 1
  set box_width round((world-width - (border * 6)) / 5)

  while [on_x >= (min-pxcor + border + box_width)] [
    set on_y max-pycor - border
    while [on_y >= (min-pycor + border + box_height)] [

      create_box on_x on_y

      set on_y (on_y - (border + box_height))



    ]
    set on_x (on_x - (border + box_width))
  ]
end





;:This and render allows the major processes of the game to run properly and appear on the world screen
;;observer procedure
;;created by elias xu
to run_game
  ;;if the end condition has not started, keep the game runding
  if running = True
   [render]
end


;;This just makes the letter upper case and makes the row automatically change when a guess is made.
;;observer procedure
;;create by elias xu
to render
  ;;split up the guess
  let change_list string_list guess
  let wletter 0

  let min_list_length min list length(change_list) 5

  ;render the first five letters of the word on the screen
   while [wletter < min_list_length ] [
     let new_letter  uppercase(item wletter change_list)
     switch_letter (wletter + 1) current_row_number new_letter
     set wletter wletter + 1
    ]


  ;if the length of the word in the guess box is less than 5
  ;fill the rest of the spaces with blanks
  let r_num length(change_list)

  if r_num < 5 [
    while [r_num < 5] [
      switch_letter (r_num + 1) current_row_number ""
      set r_num r_num + 1
    ]
  ]

end


;;This code checks if the answers are right and reports it to the rest of the code.
;;observer function
;;created by elias xu
to check
  ;code is very cluncky, but it works
  let wletter 0
  let ans_list []
  let num_green 0

  ;add letters from the lowest row being checked to ans_list
  while [wletter < 5] [
    if get_letter (wletter + 1) current_row_number != ""
    [set ans_list insert-item wletter ans_list (get_letter (wletter + 1) current_row_number)]
    set wletter wletter + 1
  ]


  ;check each letter, marking the letters colors depending on the word
  ;observer function
  ;created by elias xu
  set wletter 0
  if length ans_list = 5 [
    while [wletter <= 4] [
      let cur_letter uppercase(item wletter ans_list)
      ifelse cur_letter = item wletter answer_word
      [set_color (wletter + 1) current_row_number correct_color
        set num_green num_green + 1
      ]
      [ifelse member? cur_letter answer_word
        [set_color (wletter + 1) current_row_number warmer_color]
        [set_color (wletter + 1) current_row_number cold_color]
      ]
      set wletter wletter + 1

  ]
    ;check win condition
    ;if won, clear everthing, end the game, and set everthing else to yellow
    if num_green = 5 [
     set running False
     wait 2
     clear-all
     ask patches [set pcolor yellow
    ]
    ]

    set current_row_number current_row_number - 1


    ;check loss condition
    ;if loss, clear everthing, end game
    ;and set everthing else to red
    ;if loss,
    if current_row_number = 0 [
        set running False
        wait 2
        clear-all
        ask patches [
          set pcolor red
        ]



      ]

    create_empty current_row_number
    set guess ""
  ]


end



;;uses the box function to create boxs at speficic locations
;;observer procedure
;;created by elias xu
to create_boxes


  set on_x max-pxcor - border

  ;find the box width and box height values
  set box_height round((world-height - (border * 7)) / 6) - 1
  set box_width round((world-width - (border * 6)) / 5)

  while [on_x >= (min-pxcor + border + box_width)] [
    set on_y max-pycor - border
    while [on_y >= (min-pycor + border + box_height)] [

      create_box on_x on_y

      set on_y (on_y - (border + box_height))
    ]
    set on_x (on_x - (border + box_width))
  ]
end


;;creates a box at speficic loaction
;;observer procedure
;;created by elias xu
to create_box [x_val y_val]
  cro 1 [
    setxy x_val y_val
    pd
    lt 90
    fd box_width
    lt 90
    fd box_height
    lt 90
    fd box_width
    lt 90
    fd box_height
  ]
end

;;reports the inputted letter at a box
;;observer prodecure
;;created by elias xu
to-report get_letter [blength bheight]
  ;finds the top right value of a box
  let x_value max-pxcor - ((5 - blength) * (border + box_width)) - border
  let y_value max-pycor - ((6 - bheight)*(border + box_height)) - border

  let answer ""

  ;makes the turtle at the location to return the label it has
  ask turtles with [xcor = x_value - 15 and ycor = y_value - 50] [set answer label]

  report answer
end


;;split string to specific characters, reports list
;;observer procedure
;; created by elias xu and dannyar akhmedov
to-report string_list [string]
  let split-string []
  let while-num length string

  ;loops through each letter of the string, returns completed
  while [while-num >= 0] [
    let a  max list (0) (while-num - 1)
    let b  max list (0) (while-num)
    set split-string insert-item (length(string) - while-num) split-string (substring string a b)
    set while-num while-num - 1
  ]

  ;reports the string
  report(reverse(remove "" split-string))

end


;;Sets the pcolor
;;observer procedure
;;created by elias xu
to set_color [blength bheight bcolor]
  ;get top right corner values of the square you want to turn
  let x_value max-pxcor - ((5 - blength) * (border + box_width)) - border
  let y_value max-pycor - ((6 - bheight)*(border + box_height)) - border

  ;sets the pcolor of the patch
  ask patches with [between? (x_value - box_width) pxcor x_value and between? (y_value - box_height) pycor (y_value)]
    [set pcolor bcolor]

end

;;returns True if num is between or at the min and max, false if otherwise
;;observer function
;created by elias xu
to-report between? [bmin num bmax]
  ifelse num >= bmin and num <= bmax
  [report(true)]
  [report(false)]
end

;;This generates a letter within the boxes, using a turtle, it was written by Elias and utilizes the observer
to set_letter [blength bheight letter]
  let x_value max-pxcor - ((5 - blength) * (border + box_width)) - border
  let y_value max-pycor - ((6 - bheight)*(border + box_height)) - border

  ;creates a turtle and sets it to the correct x and y values
  ;then it sets

  cro 1  [
  setxy (x_value - 15) (y_value - 50)
  set label letter
  ]
end



;;Switches the label of the letter, this was written by Elias and used the observer
to switch_letter [blength bheight letter]
  let x_value max-pxcor - ((5 - blength) * (border + box_width)) - border
  let y_value max-pycor - ((6 - bheight)*(border + box_height)) - border



  ask turtles with [xcor = x_value - 15 and ycor = y_value - 50] [set label letter]
end

;;Outputs the box color, this uses the observer and was written by Elias.
to-report box_color [blength bheight]
  ;get top right corner values of the square you want to turn
  let x_value max-pxcor - ((5 - blength) * (border + box_width)) - border
  let y_value max-pycor - ((6 - bheight)*(border + box_height)) - border
  let turtle_color ""


  ask patches with [round (2 * x_value - box_width) = pxcor and round (2 * y_value - box_height) = pycor ]
    [set turtle_color pcolor]

  report(turtle_color)
end


;;changes lowercase letters to uppercase, this uses the observer and was written by Dannyar
to-report uppercase[character]
  if character = "a" [report "A"]
  if character = "b" [report "B"]
  if character = "c" [report "C"]
  if character = "d" [report "D"]
  if character = "e" [report "E"]
  if character = "f" [report "F"]
  if character = "g" [report "G"]
  if character = "h" [report "H"]
  if character = "i" [report "I"]
  if character = "j" [report "J"]
  if character = "k" [report "K"]
  if character = "l" [report "L"]
  if character = "m" [report "M"]
  if character = "n" [report "N"]
  if character = "o" [report "O"]
  if character = "p" [report "P"]
  if character = "q" [report "Q"]
  if character = "r" [report "R"]
  if character = "s" [report "S"]
  if character = "t" [report "T"]
  if character = "u" [report "U"]
  if character = "v" [report "V"]
  if character = "w" [report "W"]
  if character = "x" [report "X"]
  if character = "y" [report "Y"]
  ifelse character = "z" [report "Z"] [report character]

end

;;Creates empty row; this used the observer and was made by Seth
to create_empty [row_num]
  let wletter 0
  while [wletter <= 4] [
    set_letter (wletter + 1) row_num ""
    set wletter wletter + 1
  ]
end

@#$#@#$#@
GRAPHICS-WINDOW
210
10
619
580
-1
-1
1.0
1
70
1
1
1
0
1
1
1
-200
200
-280
280
0
0
1
ticks
30.0

INPUTBOX
760
124
989
184
guess
NIL
1
0
String

BUTTON
1002
126
1069
159
check
check
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

INPUTBOX
765
202
914
262
correct_color
55.0
1
0
Color

INPUTBOX
768
280
997
340
warmer_color
45.0
1
0
Color

INPUTBOX
777
353
1006
413
cold_color
5.0
1
0
Color

BUTTON
660
54
761
87
NIL
start_game
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
801
70
895
103
NIL
run_game\n
T
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

@#$#@#$#@
## WHAT IS IT?

This model is a replication of the classic New York Times word game netlogo, in which you guess the identity of a five letter word by inputting other five letter words. If a letter in a word one enters is not in the word  that you have to guess, it will have a grey color in its box. It it is in the word, but not in correct location, the letter will have a yellow colored box. And finially, if the letter is in the word and shares a location with the corresponding letter, it will have a green colored box.


## HOW IT WORKS

You hit setup to clear the board and then run the game, the code then randomly selects one of many pre inputted five letter words (and none words like LBOZO) and you have to put in letters to try to guess your word. Once you’ve inputted your word you hit check and the letters flash either green, yellow or black. If the letter flashes green it’s the right letter in the right place, if the letter flashes yellow it’s the right letter in the wrong place in the word and if the letter flashes gray it’s just not in the word. If you get the word right the board flashes yellow and if you make all your guesses and get it wrong the board flashes red.

## HOW TO USE IT

The start_game button would set the thing up. It would create the boxes and initialize the world.

The run-game button would allow the game to run correctly, it allows for the word to be rendered onto the screen and checks if the win has happened.

The guess input monitor is the spot where one enters his or her specific guess. 

The check button would check each letter of the bottom word on the screen, and would assign colors based on each letter and it's position

The correct_color, warmer_color, and cold_color monitors represent colors that appear in boxes when the check function is run.  

## THINGS TO NOTICE

The model doesn’t use a dictionary or a massive word bank but one of only about thirty words so if you play it enough times you can see the words repeating. Also this is something that pretty hard to notice without looking at the model from the code side of things but are the boxes patches and if not how did we (Elias) get letters to show up in them.


## THINGS TO TRY

One thing that I would want one to try is adding their own words to the answer word possibilities list. It would improve their experince.

## EXTENDING THE MODEL

I really recommend that one try to find a way to check if the words that a user inputs are actual words or not. It would vasty improve the program if somebody can stop people from just randomly typing letters. 

Another smaller thing that a person could do is find a way to have dark and light modes for this program, just as actual wordle does, and a more interesting font for each letter.

I don't know if this is possible, but I would really like this wordle copy to create sharable emojis just like normal wordle. It would be really interesting and would be true to the original intention of this model.

## NETLOGO FEATURES

This model uses a lot of while loops instead of for loops. Because of that, this model uses the let function pretty well, helping all the while loops run correctly by giving the while loops the iterators tha they need.

 Besides that, this model uses turtle labels for representing the letters on the squares. Thus the font in this model is different than actual wordle. 





## RELATED MODELS

Link to actual wordle: https://www.nytimes.com/games/wordle/index.html 


## CREDITS AND REFERENCES
Seth Fenton, Elias Xu, and Dannyar Akhmedov
Period 9

Inspired by Wordle, created by Josh Wardle and owned by the New York Times Company
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

airplane
true
0
Polygon -7500403 true true 150 0 135 15 120 60 120 105 15 165 15 195 120 180 135 240 105 270 120 285 150 270 180 285 210 270 165 240 180 180 285 195 285 165 180 105 180 60 165 15

arrow
true
0
Polygon -7500403 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

box
false
0
Polygon -7500403 true true 150 285 285 225 285 75 150 135
Polygon -7500403 true true 150 135 15 75 150 15 285 75
Polygon -7500403 true true 15 75 15 225 150 285 150 135
Line -16777216 false 150 285 150 135
Line -16777216 false 150 135 15 75
Line -16777216 false 150 135 285 75

bug
true
0
Circle -7500403 true true 96 182 108
Circle -7500403 true true 110 127 80
Circle -7500403 true true 110 75 80
Line -7500403 true 150 100 80 30
Line -7500403 true 150 100 220 30

butterfly
true
0
Polygon -7500403 true true 150 165 209 199 225 225 225 255 195 270 165 255 150 240
Polygon -7500403 true true 150 165 89 198 75 225 75 255 105 270 135 255 150 240
Polygon -7500403 true true 139 148 100 105 55 90 25 90 10 105 10 135 25 180 40 195 85 194 139 163
Polygon -7500403 true true 162 150 200 105 245 90 275 90 290 105 290 135 275 180 260 195 215 195 162 165
Polygon -16777216 true false 150 255 135 225 120 150 135 120 150 105 165 120 180 150 165 225
Circle -16777216 true false 135 90 30
Line -16777216 false 150 105 195 60
Line -16777216 false 150 105 105 60

car
false
0
Polygon -7500403 true true 300 180 279 164 261 144 240 135 226 132 213 106 203 84 185 63 159 50 135 50 75 60 0 150 0 165 0 225 300 225 300 180
Circle -16777216 true false 180 180 90
Circle -16777216 true false 30 180 90
Polygon -16777216 true false 162 80 132 78 134 135 209 135 194 105 189 96 180 89
Circle -7500403 true true 47 195 58
Circle -7500403 true true 195 195 58

circle
false
0
Circle -7500403 true true 0 0 300

circle 2
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240

cow
false
0
Polygon -7500403 true true 200 193 197 249 179 249 177 196 166 187 140 189 93 191 78 179 72 211 49 209 48 181 37 149 25 120 25 89 45 72 103 84 179 75 198 76 252 64 272 81 293 103 285 121 255 121 242 118 224 167
Polygon -7500403 true true 73 210 86 251 62 249 48 208
Polygon -7500403 true true 25 114 16 195 9 204 23 213 25 200 39 123

cylinder
false
0
Circle -7500403 true true 0 0 300

dot
false
0
Circle -7500403 true true 90 90 120

face happy
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 255 90 239 62 213 47 191 67 179 90 203 109 218 150 225 192 218 210 203 227 181 251 194 236 217 212 240

face neutral
false
0
Circle -7500403 true true 8 7 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Rectangle -16777216 true false 60 195 240 225

face sad
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 168 90 184 62 210 47 232 67 244 90 220 109 205 150 198 192 205 210 220 227 242 251 229 236 206 212 183

fish
false
0
Polygon -1 true false 44 131 21 87 15 86 0 120 15 150 0 180 13 214 20 212 45 166
Polygon -1 true false 135 195 119 235 95 218 76 210 46 204 60 165
Polygon -1 true false 75 45 83 77 71 103 86 114 166 78 135 60
Polygon -7500403 true true 30 136 151 77 226 81 280 119 292 146 292 160 287 170 270 195 195 210 151 212 30 166
Circle -16777216 true false 215 106 30

flag
false
0
Rectangle -7500403 true true 60 15 75 300
Polygon -7500403 true true 90 150 270 90 90 30
Line -7500403 true 75 135 90 135
Line -7500403 true 75 45 90 45

flower
false
0
Polygon -10899396 true false 135 120 165 165 180 210 180 240 150 300 165 300 195 240 195 195 165 135
Circle -7500403 true true 85 132 38
Circle -7500403 true true 130 147 38
Circle -7500403 true true 192 85 38
Circle -7500403 true true 85 40 38
Circle -7500403 true true 177 40 38
Circle -7500403 true true 177 132 38
Circle -7500403 true true 70 85 38
Circle -7500403 true true 130 25 38
Circle -7500403 true true 96 51 108
Circle -16777216 true false 113 68 74
Polygon -10899396 true false 189 233 219 188 249 173 279 188 234 218
Polygon -10899396 true false 180 255 150 210 105 210 75 240 135 240

house
false
0
Rectangle -7500403 true true 45 120 255 285
Rectangle -16777216 true false 120 210 180 285
Polygon -7500403 true true 15 120 150 15 285 120
Line -16777216 false 30 120 270 120

leaf
false
0
Polygon -7500403 true true 150 210 135 195 120 210 60 210 30 195 60 180 60 165 15 135 30 120 15 105 40 104 45 90 60 90 90 105 105 120 120 120 105 60 120 60 135 30 150 15 165 30 180 60 195 60 180 120 195 120 210 105 240 90 255 90 263 104 285 105 270 120 285 135 240 165 240 180 270 195 240 210 180 210 165 195
Polygon -7500403 true true 135 195 135 240 120 255 105 255 105 285 135 285 165 240 165 195

line
true
0
Line -7500403 true 150 0 150 300

line half
true
0
Line -7500403 true 150 0 150 150

pentagon
false
0
Polygon -7500403 true true 150 15 15 120 60 285 240 285 285 120

person
false
0
Circle -7500403 true true 110 5 80
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Rectangle -7500403 true true 127 79 172 94
Polygon -7500403 true true 195 90 240 150 225 180 165 105
Polygon -7500403 true true 105 90 60 150 75 180 135 105

plant
false
0
Rectangle -7500403 true true 135 90 165 300
Polygon -7500403 true true 135 255 90 210 45 195 75 255 135 285
Polygon -7500403 true true 165 255 210 210 255 195 225 255 165 285
Polygon -7500403 true true 135 180 90 135 45 120 75 180 135 210
Polygon -7500403 true true 165 180 165 210 225 180 255 120 210 135
Polygon -7500403 true true 135 105 90 60 45 45 75 105 135 135
Polygon -7500403 true true 165 105 165 135 225 105 255 45 210 60
Polygon -7500403 true true 135 90 120 45 150 15 180 45 165 90

sheep
false
15
Circle -1 true true 203 65 88
Circle -1 true true 70 65 162
Circle -1 true true 150 105 120
Polygon -7500403 true false 218 120 240 165 255 165 278 120
Circle -7500403 true false 214 72 67
Rectangle -1 true true 164 223 179 298
Polygon -1 true true 45 285 30 285 30 240 15 195 45 210
Circle -1 true true 3 83 150
Rectangle -1 true true 65 221 80 296
Polygon -1 true true 195 285 210 285 210 240 240 210 195 210
Polygon -7500403 true false 276 85 285 105 302 99 294 83
Polygon -7500403 true false 219 85 210 105 193 99 201 83

square
false
0
Rectangle -7500403 true true 30 30 270 270

square 2
false
0
Rectangle -7500403 true true 30 30 270 270
Rectangle -16777216 true false 60 60 240 240

star
false
0
Polygon -7500403 true true 151 1 185 108 298 108 207 175 242 282 151 216 59 282 94 175 3 108 116 108

target
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240
Circle -7500403 true true 60 60 180
Circle -16777216 true false 90 90 120
Circle -7500403 true true 120 120 60

tree
false
0
Circle -7500403 true true 118 3 94
Rectangle -6459832 true false 120 195 180 300
Circle -7500403 true true 65 21 108
Circle -7500403 true true 116 41 127
Circle -7500403 true true 45 90 120
Circle -7500403 true true 104 74 152

triangle
false
0
Polygon -7500403 true true 150 30 15 255 285 255

triangle 2
false
0
Polygon -7500403 true true 150 30 15 255 285 255
Polygon -16777216 true false 151 99 225 223 75 224

truck
false
0
Rectangle -7500403 true true 4 45 195 187
Polygon -7500403 true true 296 193 296 150 259 134 244 104 208 104 207 194
Rectangle -1 true false 195 60 195 105
Polygon -16777216 true false 238 112 252 141 219 141 218 112
Circle -16777216 true false 234 174 42
Rectangle -7500403 true true 181 185 214 194
Circle -16777216 true false 144 174 42
Circle -16777216 true false 24 174 42
Circle -7500403 false true 24 174 42
Circle -7500403 false true 144 174 42
Circle -7500403 false true 234 174 42

turtle
true
0
Polygon -10899396 true false 215 204 240 233 246 254 228 266 215 252 193 210
Polygon -10899396 true false 195 90 225 75 245 75 260 89 269 108 261 124 240 105 225 105 210 105
Polygon -10899396 true false 105 90 75 75 55 75 40 89 31 108 39 124 60 105 75 105 90 105
Polygon -10899396 true false 132 85 134 64 107 51 108 17 150 2 192 18 192 52 169 65 172 87
Polygon -10899396 true false 85 204 60 233 54 254 72 266 85 252 107 210
Polygon -7500403 true true 119 75 179 75 209 101 224 135 220 225 175 261 128 261 81 224 74 135 88 99

wheel
false
0
Circle -7500403 true true 3 3 294
Circle -16777216 true false 30 30 240
Line -7500403 true 150 285 150 15
Line -7500403 true 15 150 285 150
Circle -7500403 true true 120 120 60
Line -7500403 true 216 40 79 269
Line -7500403 true 40 84 269 221
Line -7500403 true 40 216 269 79
Line -7500403 true 84 40 221 269

wolf
false
0
Polygon -16777216 true false 253 133 245 131 245 133
Polygon -7500403 true true 2 194 13 197 30 191 38 193 38 205 20 226 20 257 27 265 38 266 40 260 31 253 31 230 60 206 68 198 75 209 66 228 65 243 82 261 84 268 100 267 103 261 77 239 79 231 100 207 98 196 119 201 143 202 160 195 166 210 172 213 173 238 167 251 160 248 154 265 169 264 178 247 186 240 198 260 200 271 217 271 219 262 207 258 195 230 192 198 210 184 227 164 242 144 259 145 284 151 277 141 293 140 299 134 297 127 273 119 270 105
Polygon -7500403 true true -1 195 14 180 36 166 40 153 53 140 82 131 134 133 159 126 188 115 227 108 236 102 238 98 268 86 269 92 281 87 269 103 269 113

x
false
0
Polygon -7500403 true true 270 75 225 30 30 225 75 270
Polygon -7500403 true true 30 75 75 30 270 225 225 270
@#$#@#$#@
NetLogo 6.3.0
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
default
0.0
-0.2 0 0.0 1.0
0.0 1 1.0 0.0
0.2 0 0.0 1.0
link direction
true
0
Line -7500403 true 150 150 90 180
Line -7500403 true 150 150 210 180
@#$#@#$#@
0
@#$#@#$#@
