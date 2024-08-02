arr = [3,4,2,1,2]


def check(arr):
    # i ranges from 0 till len(arr) = len(arr) - 1
    for i in range(0, len(arr) - 1):
        # Checks the neighbour numbers if the left_neighbour is < or >
        # Checks if its right number is < or >
        # If both the conditions are < then it will return i
        if arr[i - 1] < arr[i] > arr[i + 1]:
            return i

    # checks the last number if it's left neighbour is smaller or greater
    # if its smaller, then index of the number will be returned
    if arr[-1] > arr[-2]:
        return arr.index(arr[-1])

    return 0


result = check(arr)
print(result)



