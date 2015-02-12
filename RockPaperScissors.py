# Option 3: Rock Paper Scissors
# By Evelyn Ramos

#Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox 
import random 

# Creagte a Window
root = Tk()
w = Label(root, text= " Rock Paper Scissors Game ")
w.pack()

# Welcome the User
messagebox.showinfo("title", "Welcome User")
messagebox.showinfo( "title", "Today you will be playing Rock, Paper, Scissors Game") 
messagebox.showinfo("title", "Good Luck")

# Set-up
rock = 0
paper = 0
scissors = 0
winner = None 
player = input("Enter your choice (rock/paper/scissors): ")
tries = 0
player = player.lower()
if tries <= 3:
    print( "Would you like to continue playing?" "Yes" or "No?")
if player == "Yes":
    "continue"
else:
    "break"
       
        


# Computer Choice Set-up
computerChoice = random.randint(1,3)
if (computerChoice == 1):
    computerChoice = "rock"
elif (computerChoice == 2):
    computerChoice = "paper"
elif (computerChoice == 3):
    computerChoice = "scissors"
else :
    ComputeChoice = " Error Try Again "

    
# Determine the Winner
while tries <= 3: print(" Enter your choice rock, paper, or scissors")
if (player == computerChoice):
    print("Draw!")
elif (player == "rock"):
    if(computerChoice == "paper"):
        print("Computer wins");
    else:
        print("You Win! Yay!")
        
elif (player == "paper"):
    if(computerChoice == "rock"):
        print("You win! Yay!");
    else:
        print("Computer wins")
elif(player == "scissors"):
    if(computerChoice == "rock"):
        print("Computer wins");
    else:
        print("You win! Yay!")    

  

    

      
    

    




                    
