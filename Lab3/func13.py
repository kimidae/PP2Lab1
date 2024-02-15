import random 

def game(number, guess, name, rand):
    if number == rand:
        print("Good job, ", name, "! You guessed my number in ", guess, " guesses!")
        return
    elif number > rand:
        print("Your guess is too high.", "\n", "Take a guess.")
    else:
        print("Your guess is too low.", "\n", "Take a guess.")
    
    guess += 1
    number = int(input())
    game(number, guess, name, rand)

rand = random.randint(1, 20)
print("Hello! What is your name?")
name = input()
print("Well, ", name, ", I am thinking of a number between 1 and 20.", "\n", "Take a guess.")
number = int(input())
guess = 1
game(number, guess, name, rand)
