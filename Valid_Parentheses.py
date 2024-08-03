valid = {'{': '}', '(': ')', '[': ']'}


# Creating an empty list to store the values from case_1
stack = []

def check(case_1):
    # checks the brackets in case_1
    for bracket in case_1:
        # if the bracket in case_1 is one of the keys in valid
        if bracket in valid.keys():
            # then it will add to the stack
            stack.append(bracket)
            # if the bracket in case_1 is one of the values
        elif bracket in valid.values():
            # If it is one of the values then it will check if the stack is empty or not
            # if not empty then it will check the key in the stack is equal to the value
            if stack and valid[stack[-1]] == bracket:
                # if the key: value then the stack will pop, leaving with no chars
                stack.pop()
            else:
                # else it will return False
                return False

    # If the stack is not empty, then it will return True or else it will return False
    return len(stack) == 0

case_1 = "["
result = check(case_1)
print(result)  # This will print False, as the bracket is not balanced




# The time complexity of this function is O(n) where n is the number of characters in the input string `case_1`. This is because the function iterates through each character in the input string once to check if it is a bracket and to perform the necessary operations.

# The space complexity of this function is also O(n) where n is the number of characters in the input string `case_1`. This is because the function uses a stack data structure to store the brackets as it iterates through the input string. In the worst case scenario, the stack could contain all the opening brackets before encountering any closing brackets, leading to a space complexity of O(n).


