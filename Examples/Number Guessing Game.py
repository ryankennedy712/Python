import random

def check(userinput):
    if userinput > randomvar:
        print("Too big")
    elif userinput < randomvar:
        print("too small")

randomvar = random.randint(1,100)

print(randomvar)

count = 0

while True:
    userinput = input("Input a number 1 to 100 ")
    count += 1
    check(userinput)
    if userinput == randomvar:
        print('you won ' + str (count))
        break