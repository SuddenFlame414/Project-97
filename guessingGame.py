import random


chances=0
guess = int(input("Enter guess: "))
number = random(0,10)
while chances<5:
    if guess==number :
        print("Congratulations you won!!")
    break
if not chances<5:
    print("YOU LOSE!!! The number is ", number)
