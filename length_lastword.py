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



-The time complexity of this code is O(n), where n is the length of the input string. This is because the code iterates through each character in the input string once to split it into words and store them in a list.

-The space complexity is also O(n) because the code uses a list to store the words extracted from the input string. The size of this list will be proportional to the length of the input string.
