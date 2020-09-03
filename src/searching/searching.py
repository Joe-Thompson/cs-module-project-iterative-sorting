def linear_search(arr, target):
    for i, elm in enumerate(arr):
        if target == elm:
            return i
    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start_bs = 0
    end_bs = len(arr) -1

    while end_bs >= start_bs:
        middle_index = (start_bs + end_bs) // 2
        middle_value = arr[middle_index]
        if target == middle_value:
            return middle_index
        if target > middle_value:
            start_bs = middle_index + 1
        if target < middle_value:
            end_bs = middle_index - 1

    return -1  # not found
