s = "race a car"

str = ""

# Creating a for loop and declaring words that will hold values of s
for words in s:
    # `isalnum()`: will check if words is an alphabet or not
    if words.isalnum():
        # only alphabets will pass and then be lowered then added to str
        str += words.lower()


i,j = 0, len(str) - 1

# Creating a function that take two parameters i,j
def check(i,j):
    # the while loop will work until `i` is smaller than `j`
    while i < j:
        # if the letter at index i in str is not equal to index j in str
        if str[i] != str[j]:
            # it will return False
            return False
        else:
            # if its equal then 1 will be added to i and 1 will be subtracted to j
            i += 1
            j -= 1

    # if the chars are equal till the end of the while then True will be returned
    return True

result = check(i,j)

print(result)