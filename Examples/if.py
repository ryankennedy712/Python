#if statement

print("type in a vaule of 'a' or 'b'")
userinput = input()


#We are checking to see if the userinput has the letter, a stored inside it.
#In Python 2 equal signs stands for a comparision, where 1 equal sign is changing the vaule. 
if userinput == "a":
    print("you typed a!")

#elif stands for else if, this means that if the above if statement fails it tries the elif statement.
elif userinput == "b":
    print("you typed b!")

#else statements run when no conditions are matched of the if statements.
else:
    print("you did not type a or b")
