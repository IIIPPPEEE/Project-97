import random
number=random.randint(1,9)
chances=0
print("Guess a number from 1 to 9")
while chances<5:
    enterInput=int(input("Enter your guess!"))
    if enterInput==number:
        print("Your guess is correct.You won!!")

    elif enterInput<number:
        print("Your guess too low,try guessing higher number",enterInput)
    else:
         print("Your guess is too high,try guessing smaller number",enterInput)

    chances+=1
    if not chances<5:
        print("You lose.The number is",number)



