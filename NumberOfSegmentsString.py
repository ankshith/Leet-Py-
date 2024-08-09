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
