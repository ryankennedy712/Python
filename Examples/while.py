

print("How many times would you like to loop?")

#here we take the user input, convert it to an integer ( int() ) and store it in a variable.(loopcount)
loopcount = int(input())


#While loopcount is greater or equal to 0 this loop will not stop.
while loopcount >= 0:
    print("Looped! ", loopcount, " More to go!")

#this line is to make sure the value of loop count decreases each loop.
    loopcount -= 1
