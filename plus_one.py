digits = [1,2,3,4]

# Creating a new string to store new_num
num_str = ""

# initially new_num stores value 0, so that we can update with new_str
new_num = 0

def check(num_str, new_num):

    # loops through the digits and add's it to the num_str
    for i in digits:
        num_str += str(i)

    # checks if num_str is empty or not
    if num_str:
        # if num_string is not empty then num_str stored in datatype str, will be converted to int and added with 1
        new_num = str(int(num_str) + 1)

    # then it will be converted to int and stored in list
    return [int(x) for x in new_num]




result = check(num_str, new_num)
print(result)




# The time complexity of this code is O(n) where n is the number of digits in the 'digits' list. This is because the code loops through each digit in the list once to create the 'num_str' string.

# The space complexity of this code is O(n) as well. This is because the 'num_str' string will store all the digits in the 'digits' list, and the 'new_num' variable will store the updated number after adding 1 to the 'num_str'. Additionally, the final list comprehension will create a new list based on the 'new_num' string.
