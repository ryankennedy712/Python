def reorder_digits(lst, direction):
    temp = 0
    if direction == "desc":
        for x in lst:
            for j in range(0,len(x) - 1):
                if x[j] < x[j + 1]:
                    temp = x[j+1]
                    x[j+1] = x[j]
                    x[j] = temp

    elif direction == "asc":
        for x in lst:
            for j in range(0,len(x) - 1):
                if x[j] > x[j + 1]:
                    temp = x[j+1]
                    x[j+1] = x[j]
                    x[j] = temp
                    
    else:
        print("you did not enter the info correctly")



def convert_str_to_array(str_input):
    num_input = []
    count = 0
    str_input = str_input + " "
    while True:
        num_input.append(str_input[:str_input.find(" ")])
        temp = []
        for x in range(0,len(num_input[count])):
            temp.append(int(num_input[count][x]))

        num_input[count] = temp
        count += 1
        str_input = str_input[str_input.find(" ")+1:]
        if str_input == "" or str_input == " ":
            break
    return num_input
    

direction = input("'asc' or 'desc'")
str_input = input("input numbers with spaces: ")
arr = convert_str_to_array(str_input)
print(arr)
reorder_digits(arr, direction)


