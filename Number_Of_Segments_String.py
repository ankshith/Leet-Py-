string = "Hello"

lst = []
s = ""


# Iterating throughout the string
for chars in string:
    # if chars doesn't hold any spaces
    if chars != " ":
        # it will be added to the empty string `s`
        s += chars
    else:
        # if there is space `" "` then it will check if var-> s holds any value
        if s:
            # if s holds value, then it will be added to the list
            lst.append(s)
            # once the value is added, `s` will hold empty value
            s = ""

# This is for the last words, usually last words do not have space at the end of it
if s:
    # if s is not empty then the value be added
    lst.append(s)


print(len(lst))


# The time complexity of this code is O(n), where n is the length of the input string. This is because the code iterates through each character in the string exactly once.

# The space complexity is also O(n) because the code uses an empty string `s` to store each word before adding it to the list `lst`. The size of `s` can grow up to the length of the input string, so the space complexity is linear with respect to the input size.
