def subarray_sum(arr):
    temp = 0
    max_sum = -float("inf")
    for ele in arr:
        temp += ele
        if (temp > max_sum):
            max_sum = temp
        if (temp < 0):
            temp = 0
    return max_sum
print subarray_sum([-10, 6, 7, 8, -3])

