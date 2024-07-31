haystack = "sadbutsad"

find = "sad"

# Declaring an empty list and storing it in the variable `store`
store = []
def check(haystack, find):
    # The functions takes two parameters: haystack and find

    # if the word in the haystack then find the position of the word and
    # print the position of the word.
    # when the position is printed, the position of `s` will be considered

    if find in haystack:
        print(haystack.index(find[:]))


check(haystack, find)