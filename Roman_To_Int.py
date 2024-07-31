## To Convert Roman Numerals to Int ##


# creating a dictionay where keys are Roman Numerals  and values are Int
roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


# declaring variable s that takes str of Roman Numerals
s = "MCMXCIV"

# declaring variable `final_value` that stores value after performing for-loop
final_value = 0


# The following for-loop ranges from 0 till the length of s
for i in range(len(s)):

    # The first condition is if i[0-->len(s)[7]) if its True
    # then checks if the value of the first roman_numerals < or > to the second numeral
    if i < len(s) - 1 and roman_numerals[s[i]] < roman_numerals[s[i+1]]:

        # if i < len(s) - 1 [6] and roman_numerals[s[i]] the current one is smaller than the next
        # then subtract the value by the value stored in final_value
        final_value -= roman_numerals[s[i]]
    else:
        # if it's greater than add the value with value stored in final_value
        final_value += roman_numerals[s[i]]

print(final_value)




-The time complexity of this code is O(n), where n is the length of the input string `s`. This is because the code iterates through each character in the string once in the for-loop.

-The space complexity is O(1) because the code only uses a fixed amount of extra space regardless of the size of the input string. The space complexity does not depend on the input size.

