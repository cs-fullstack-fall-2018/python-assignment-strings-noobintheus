import random
userInput = int(input("0-9?"))
randomNumber = random.randint(0,9)
print(random.randint(0,9))

while True:
    userInput =input("0-9?")
    if int(userInput) == randomNumber:
        print("good job")
        break
    else:
        print("incorrect")
        continue




