digits = [1,2,3,4]

# Creating a new string to store new_num
num_str = ""

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