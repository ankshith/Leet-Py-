nums = [0, 1, 0, 3, 12]

# initialting the index at zero
index = 0

for n in range(len(nums)):
    # checks the current index has value of 0 or not
    if nums[n] != 0:
        # if not 0, it will iterate until it finds the index with value non_zero
        nums[index], nums[n] = nums[n], nums[index]
        index += 1

print(nums)



# The time complexity of this code is O(n) because it iterates through the list of numbers once.
# The space complexity is O(1) because it only uses a constant amount of extra space regardless of the input size.



# Example:

## Iteration 1: ##
# nums[index = 0] = 0
# nums[n=1] = 1


# nums[0] , nums[1] = nums[1] , nums[0]
# output: nums[1,0,0,3,12]

## Iteration 2: ##
# index will be incremented += 1

# nums[index = 1] = 0
# nums[3] = 3

# nums[1], nums[3] = nums[3], nums[1]
# output = nums[1,3,0,0,12]


## Iteration 3: ##

# index will be incremented += 1

# nums[index = 2] = 0
# nums[4] = 12

# nums[2], nums[4] = nums[4], nums[2]
# output = nums[1,3,12,0,0]
