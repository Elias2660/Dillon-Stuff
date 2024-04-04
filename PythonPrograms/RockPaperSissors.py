import random
import os
import time
w,l,d = 0,0,0

#link to flow chart: https://docs.google.com/drawings/d/1__2vTxFOlljw0liitYkOlzmg0SsOuG6I3WPu3uFNaIU/edit?usp=sharing



def run_game():
  """
  AUTHORS(s)
  Elias / Victor
  
  CONTRACT
  Runs Program
  run_game() -> game method

  DESCRIPTION
  This function runs the game
  
  TEST CASES
  #run_game()
  >> creates game method
  """
  global w,l,d
  w,l,d = 0,0,0
  running = True
  #run the game
  welcome()
  while running:
    usr = get_user_input()
    #user input there
    print("\n")
    print (3)
    time.sleep (1)
    print (2)
    time.sleep (1)
    print (1)
    time.sleep (1)
    print("\n")
    print(win_lose_draw(usr))
    running = ask_for_repeat()


def welcome():
  """
  AUTHORS(s)
  Adeline
  
  CONTRACT
  -> string
  
  DESCRIPTION
  Upon receiving input "Y" from the user to signify that they want to play the game,
  shows a welcome message before introducing the instructions for how to play
 
  TEST CASES
  welcome() -> 
"""
  print(
    "Welcome to Rock Paper Scissors! \nAre you ready to rock? \nTo tear your opponent apart? \nTo cut through the competition? \nIf so... \n"
  )


def win_lose_draw (usr):
  """
  AUTHOR
  Victor
  
  CONTRACT
  0, 1, or 2 to an output of Win, Draw or Loss randomly depending on what the computer picks
  
  DESCRIPTION
  Takes user input from get_user_input() then returns a win, draw or loss randomly
  
  UNIT CASES
  win_lose_draw(0) -> Win, Draw or Loss randomly
  win_lose_draw(1) -> Win, Draw or Loss randomly
  win_lose_draw(2) -> Win, Draw or Loss randomly
  """
  #return
  temp = random.randint(0, 2)
  global d, l, w
  if usr == temp:
    d += 1
    return " hmm, a draw- better luck next time \n"
  if usr + 1 == temp or usr - 2 == temp:
    l += 1
    print (insult())
    return " You lose! LLLL \n"
  w+= 1
  return " Woah! You won :) \n"

#Scissors = 0, Rock = 1, Paper = 2 
def get_user_input():
  """
  AUTHOR
  Elias Xu

  CONTRACT
  -> int


  DESCRIPTION
  returns a number, representing the thing that the 
  user choose as their choice of either rock, paper, and sissors


  UNIT TESTS
  get_user_input() -> 0
  get_user_input() -> 1
  get_user_input() -> 2
  """
  #prompt the user for input
  #deals with all input
  while True:
    usr_input = input("Please enter either rock (r), paper (p) scissors (s)\n")
    if usr_input =="scissors" or usr_input == "s" or usr_input == "S":
      return 0
    elif usr_input == "rock" or usr_input == "r" or usr_input == "R":
      return 1
    elif usr_input =="paper" or usr_input == "p" or usr_input == "P":
      return 2
    else:
      print(" \n Sorry that's not an option! Try again!")
    #USER FEEDBACK ADDITIONAL FUNCTION: 
    # we noticed that while out tester was playing, they broke the game by typing in something other than s/r/p or rock/paper/scissors, so we added this feature to counter that :)))

  
#define function
def ask_for_repeat():
  """
  AUTHOR
  Ayesha

  DESCRIPTION
   ask the user if they want to play again, if yes the program runs the game, if no, the game stops and user stats are show

  CONTRACT
  -> True if usr want to play again, False if they do not
  

  UNIT CASES
  y -> Your record is: 3/2/4
  n -> "Your record is: 3/2/4" 
        running = FALSE
  """
  
  global w,l,d
  time.sleep (3.0)
  os.system ('clear')
  print(f" Your score is: \n wins: {w}\n draws: {d} \n losses: {l}")
  want_to_play_again = input("\n Do you want to play again? Please type 'Y' if you want to play again \n Type any other character otherwise \n\n ")
  if want_to_play_again == "Y" or want_to_play_again =="y":
    print("\n\n")
    return True
    #allows the user to play again and re-runs the function
  else:
    print(' \n Okay, thanks for playing!')
    print(f' \n Your FINAL score is: \n wins: {w}\n draws: {d} \n losses: {l} ')
    return False
    #ends the function, shows the user what their final record is
    

def insult():
  """
  AUTHOR
  Victor


  DESCRIPTION
  returns a random insult

  
  CONTRACT
  -> random insult

  UNIT TESTS
  insult() -> Stupid people can believe in anything, so you can believe in yourself!

  insult() -> our life is more about regret management than goal achievement, isn’t it? 

  """
  o = random.randint(0, 6)
  if o == 0:
    return "Stupid people can believe in anything, so you can believe in yourself!"
  if o == 1:
    return "Your life is more about regret management than goal achievement, isn’t it?"
  if o == 2:
    return "Bob Ross would call you a mistake."
  if o == 3:
    return "You’re not even your Mom’s favorite child."
  if o == 4:
    return "You need to go think about everything you are. Then change it."
  if o == 5:
    return "Mirrors can't talk. Lucky for you, they can't laugh either."
  if o == 6:
    return "You have miles to go before you reach mediocre."
#REFLECTION!: 
# 1. We managed the work of this project by equally dividing up the work into different parts and sections so that everyone could have an equal contribution to theproject
# 2. Some of the hardships we encountered was trying to an output an image as an additional feature into our code. 
# 3. We persevered through different solutions until we eventually made our code work!
# 4. We added an additional feature based on user feedback which told you that anything that's not s/r/p is not an option, and also changed the spacing so our game looks more clean/aesthetic
# 5. Adi: I'm proud of creating the countdown function
# Elias: I'm proud of organizing and helping the team
# Victor: I'm proud of creating the insults as it adds a fun component to our game
# Ayesha: I'm proud of creating the ask_for_repeat() function and for adding an additional feature to the code 
run_game()