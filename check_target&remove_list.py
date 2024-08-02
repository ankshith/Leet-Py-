lst = [0, 1, 2, 2, 3, 4, 2, 4]
target = 2
k = 0

# Iterate through the list
i = 0

# The while loop run until i is > 6
while i < len(lst):
    # check if the lst[i]: lst[i=0] = 0, if its == target
    if lst[i] == target:
        # if its equal to the target then remove the number at the given index(i) from the lst
        lst.pop(i)
    else:

        # if not then add 1 to k--> represents score and i--> helps in increasing the index
        k += 1
        i += 1

# print k: the final score and the updated_list: lst
print(f"Final score: {k}")
print(f"Modified list: {lst}")


# The time complexity of this code is O(n^2) because there is a nested loop structure - the outer loop iterates through the list once, and the inner loop potentially iterates through the list again when an element is removed. This results in a worst-case scenario where each element in the list is checked and potentially removed, leading to a quadratic time complexity.

# The space complexity of this code is O(1) because the amount of extra space used does not increase with the size of the input list. Only a constant amount of extra space is used for variables like k, i, and target
