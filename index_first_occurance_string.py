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


# The time complexity of this code is O(n), where n is the length of the haystack string. This is because the code iterates through the haystack string to find the position of the "find" string within it.

# The space complexity is O(1) because the code only uses a constant amount of extra space regardless of the size of the input. The only extra space used is for the empty list `store` and the variables `haystack` and `find`, which do not depend on the size of the input.
