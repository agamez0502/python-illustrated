# mini project: the number guessing game

import random 

nr = random.randint(1, 10)
print(nr)

#set up the necessary fields 
secret_nr = random.randint(1,10)
max_guesses = 6

# num = input("\nPick a number, any number between 1 and 10? ")

# loop for guessing 
for attempt in range(max_guesses):
    guess = int(input("\nTake a guess: "))
    
    # check attempted guess
    if guess == secret_nr:
        print("\nOMG, right on the money!")
        break 
    elif guess < secret_nr: 
        print("\nGood guess, but not good enough..")
    else: 
        print("\nUm we're gonna be here all day.")