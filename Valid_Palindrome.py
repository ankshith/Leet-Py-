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


# The time complexity of this code is O(n) where n is the length of the input string s. This is because the code iterates through each character in the string s to build the new string str, and then it compares characters in str from both ends towards the middle. 

# The space complexity of this code is also O(n) because the new string str is created to store only the alphanumeric characters from the input string s. Additionally, the variables i and j are used to keep track of the indices for comparison, but they do not scale with the input size.

# Overall, the time and space complexity of this code is linear with respect to the length of the input string s.
