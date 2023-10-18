

# Project 1 - Number Guessing Game

We're going to be using Replit for projects, just like we do for our in-class labs and homeworks. These projects will be graded on completeness AND correctness! 

Understand the problem below and design and implement the solution in **main.py**. 

**All work must be done individually.**

We will only have a limited number of tests for the projects. Part of the project will be to understand the problem well enough to design a complete solution. That means understanding when your code fullfills all the requirements!

To this end, in order to recieve credit on projects, you MUST pass off the project with a TA or the Instructor. This means coming to either TA or instructor office hours and do so either in person, or virtually.

The TA or the Instructor will verify that your program meets the requirements and also look over your code for any major style issues. If your project fails to meet the criteria, you will be asked to keep working on the project until you can successfully pass it off. **No Partial credit**---you either pass off the project, or you don't. Late pass offs will be docked -15 points.

**NOTE:** Remember to test your code before submitting!

#

## Instructions

In this project, we'll be implementing a number guessing game!

### How The Game Works

* The program asks the user for the maximum value a number could be, as well as the maximum amount of allowed guesses.
* The program randomly chooses an integer between 0 and the maximum number.
* The user then has only the max amount of guesses to figure out what number was selected.
* The user enters a guess.
* After each guess, the program tells the user whether their guess is too high, or too low.
* The user keeps guessing until they get the correct number, or they've reached the maxmum amount of allowed guesses.

Here is an example run of what the program output and interaction should be:

**Example 1:**

    Input seed for random (leave blank for none):   

    Welcome to the number guessing game!

    What is the maximum value the number could be? 100
    What is the maximum number of guesses allowed? 5

    OK! I've thought of a number between 0 and 100 and you must guess it.
    For each guess, I'll tell you if you're too high or too low.

    Number of guesses left: 5
    Enter your guess: 50
    Too low!

    Number of guesses left: 4
    Enter your guess: 75
    Too high!
    
    Number of guesses left: 3
    Enter your guess: 60
    Too high!

    Number of guesses left: 2
    Enter your guess: 55
    Too low!

    Number of guesses left: 1
    Enter your guess: 57
    Too low!

    Boo! You didn't guess it. The number was 59

**Example 2:**

    Input seed for random (leave blank for none):

    Welcome to the number guessing game!

    What is the maximum value the number could be? 20
    What is the maximum number of guesses allowed? 4

    OK! I've thought of a number between 0 and 20 and you must guess it.
    For each guess, I'll tell you if you're too high or too low.

    Number of guesses left: 4
    Enter your guess: 10
    Too low!

    Number of guesses left: 3
    Enter your guess: 15
    Too high!

    Number of guesses left: 2
    Enter your guess: 12
    Too high!

    Number of guesses left: 1
    Enter your guess: 11

    Yay! You guessed the value: 11

#

### Project Requirements

Implement the game as described above. You should more or less follow similar flows as the example outputs above. The exact text to use in printing the output is up to you. However, in order for the **test cases** to pass, you must do the following:

* This project requires `import random`. In order to use test cases with random, we need to initialize it with a seed value. This allows the test cases to have consistent results across runs. To enable this, put the following lines of code at the top of **main.py**:

      import random
      
      seed = input("Input seed for random (leave blank for none): ")
      if seed.isnumeric():
          random.seed(int(seed))

* First, ask the user for the maximum value the number could be.
* Second, ask for the maximum amount of guesses allowed.
* Right before the user inputs each guess, print the number of guesses the user has left. Print exactly:

      Number of guesses left: <num_left>

* If the guessed number is lower than the actual number, print exactly:

      Too low!

* If the guessed number is higher than the actual number, print exactly:

      Too high!

* When the game is over, if the user guessed the number, print exactly:

      Yay! You guessed the value: <the_number>
* Otherwise, if the user failed to guess the number, print:

      Boo! You didn't guess it. The number was <the_number>

### Python Coding Style

In addition to fulfilling the above requirements, the project must be implemented in a way that uses good programming style and best practices as discussed in class, and in the reading on **Python Style Guide**. When you pass off the project, we'll particularly look for:

* Did you use functions to help organize your code, avoid code duplication, and improve code readability?
* Are your variable and function names useful and informative?
* Did you make good use of whitespace to organize your code and make it more readable?

### Hints

* Remember, projects are about making use of multiple concepts we've learned so far in class.
* Consider concepts like while loops, random, conditionals, functions, etc.

### Collaboration and Copying Code

Each student must implement the project indvidually. You CANNOT just copy entire code from another student, or from the internet.

You are welcome, however, to work together. It is perfectly fine to discuss how to solve specific parts of the project, or ideas for how to approach things. 

**Examples of Good Collaboration**

It would be completely fine to discuss how to strucure your while loop to know when to stop asking for user guesses. You discuss ideas, then go on your own to implement the ideas discussed.

It's even fine to ask for specific code snippets. For example, if you ask someone how to convert a string to lower case letters, they can send you sample code that calls the string function `.lower()`. You can then apply that method to your own code.

**Example of Bad Collaboration**

You're not sure how to implement the while loop part, so you ask another student how they did it and they send you all their project code. You then just copy that code directly into your project, but change the variable/function names a bit.

Or you Google search and you find a complete implementation of the number guessing game online, and you just copy that code directly into your project.

#

We will be reviewing everyone's code to see if any are similar enough to other students or from what we find online. If you are just wholesale copying anothers code, **you will recieve no credit for the project.**
