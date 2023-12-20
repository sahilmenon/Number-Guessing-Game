import random

totalguesses = int(input("What is the total number of guesses you want? "))
lowerbound = int(input("Input the lower bound: "))
upperbound = int(input("Input the upper bound: "))

randomvalue = random.randint(lowerbound,upperbound)

for x in range(totalguesses):
    Guess = int(input("Guess the number: "))
    if Guess > randomvalue:
        print("Too High!")
        if x+1 == totalguesses:
            print(f"The number was {randomvalue}. Try again next time!")

    elif Guess < randomvalue:
        print("Too Low!")
        if x+1 == totalguesses:
            print(f"The number was {randomvalue}. Try again next time!")
    else:
        print(f"Bingo! You got it in {x+1} tries")
        break

    