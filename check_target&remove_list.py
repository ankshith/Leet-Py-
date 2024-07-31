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
