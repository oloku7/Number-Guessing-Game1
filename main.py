# TODO: Implement Number Guessing game!
import random 
seed = input("Input seed for random (leave blank for none): ")
if seed.isnumeric():
  random.seed(int(seed))
#PRINTS IF YOU HAVE WON THE GAME
def printWinMessage(number):
    print(f"Congratulations, the number was {number}")
# PRINT THIS IF THE VALUE IS LOWER
def printLoseMessage(number):
    print(f"HAHA, you lose the number was {number}")
#PRINT IF IT IS GREATER THAN
def printGreaterMessage(guess):
    print(f"The number {guess} is too high")
# PRINT IF IT IS LESS THAN
def printLesserMessage(guess):
    print(f"The number {guess} is too Low")
def printInvalidMessage(number):
    print(f"Invaild entry, {number} try again !")



def guessingGame(max_number, num_guesses):
    number = random.randint(0, max_number) #
    while num_guesses > 0:
        guess = int(input("Enter your guess: ")) 
        if guess == number:
            printWinMessage(number)
            return
        elif guess > number:
            printGreaterMessage(guess)
            num_guesses -= 1
        elif guess < number:
            printLesserMessage(guess)
            num_guesses -= 1
        else:
          
            printInvalidMessage(number)
    printLoseMessage(number)


max_number = int(input("Enter your max number: "))
num_guesses = int(input("Enter the amount of guesses: "))
guessingGame(max_number, num_guesses)
            

