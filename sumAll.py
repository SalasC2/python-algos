# Add all items in an array without reduce method

def sum_all(arr):
    combined = 0
    for x in range(len(arr)):
        combined += arr[x]
    return combined
print sum_all([1, 2, 3, 4])
