import random
def guess (a):
    while True:
        n = int(input("Enter a number from 1 to 10"))
        if n ==a:
            print ("You gussed it right")
            break
        else:
            print ("Wrong guess")
a = random.randint(1,10)
guess (a)