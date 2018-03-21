''Author Anurag Kumar(mailtoanuragkumarak95@gmail.com)
Module for implementing the simpest Magic 8 Ball Game.
Python:
  - 3.5
Requirements:
  - colorama
Usage:
  - $python3 magic8ball.py
Ask a question, and know the future.

# importing modules for time, random, colorama
# sleep function seems to be some type of call that pauses for an indicated amount
# of seconds 
from time import sleep

# randint will generate a random integer between two parameters that are accepted
from random import randint

# importing from colorama which sets different colors, Possible values below:
# Fore[ground]: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
from colorama import Fore, Style


# this is a list of possible responses 
# response list..
# 20 items in this list
response = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Quite possibly so",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"]

# defining the function game
# core game...
def game():

    #Sets the ques variable to user's input/ response to "What is your question?"
    #making the question in lower case
    ques = str(input("What is your question? \n").lower())
    
    #prints on the screen the following string while pausing for one second
    print ("thinking...")
    sleep(1)

    #setting idx to a randomly generated interger between 0-20 
    idx = randint(0,20)

    #If the randomly generated integer is less than 10, it will set the foreround color to green
    if idx <10: color = Fore.GREEN

    #else if it is between 10 and 15 will set the foreground color to yellow
    elif idx>=10 and idx<15: color = Fore.YELLOW
    
    #For cases not included above, it will set the color to red
    else: color = Fore.RED

    #This will print the randomly generated integer's item on the list in the color indicated with
    #the previous else if statement 
    print (color+response[idx]+Style.RESET_ALL+'\n\n')

    #this will them go through the loop set below
    playloop()

# looping func...
# setting the looping function
def playloop():

    #setting question again to the user inputted value of "would you like another q". 
    #setting all the responses to lower case
    ques_again = str(input("Would you like to ask another question? (y/n)\n").lower())

    #if the response is 'y', then we will call the game function again
    if ques_again == 'y':
        game()
    
    #if the response is 'n', we will print "Auf Widersehen"
    elif ques_again == 'n':
        print("Auf Wiedersehen!")
    
    #if the response is neither y or n, then we will go back to the beginning of the loop
    else:
        print ("What was that?/n")
        playloop()

#this sets a check to see if the script is being imported by another module or if it is being run directly
#https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__=='__main__':
    game()