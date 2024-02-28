import random

myNumber = int(input("Enter your number [1,10]"))

secretNumber = random.randint(1,10)

while True:
    if secretNumber == myNumber:
        print("Yes, It is")
        
    elif secretNumber < myNumber:
        print("It is bigger than your guess!")
        
    elif secretNumber > myNumber:
        print("It is lower than your guess")
        
    else:
        print("Are you joking to me ?? huh")
        

    print("It is : ",secretNumber) 
    break
