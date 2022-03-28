import random


chances=0
guess = int(input("Enter guess: "))
number=random.randint(1,9)
while chances<5:
    if guess==number :
        print("Congratulations you won!!")
    break
if not chances<5:
    print("YOU LOSE!!! The number is ", number)
