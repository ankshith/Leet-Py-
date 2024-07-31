# Find the length of the last string
input = " luffy is still joyboy"

list = []
str = ""

for n in range(len(input)):
    # Checks if the input has space
    if input[n] != " ":
        # if the input doesn't have " " than the declared
        # variable(str) stores the letter
        # if " " found then else loop will be activated
        str += input[n]

    else:
        # if " " found then it check if str is empty or not
        # if it's not empty then the word formed in variable(str)
        # will be appended to list
        if str:
            list.append(str)
            str = ""

# It checks if str is empty or not, if its not then it adds to the list

if str:
    list.append(str)



print(list)






















# print(input_list)



#
# result = check(input, i)
# print(input_list)