# sort array by ascending numbers
def sort_array(arr):
    sorted_array = []
    while arr:
        minimum = arr[0]
        for x in arr:
            if x < minimum:
                minimum = x
        sorted_array.append(minimum)
        arr.remove(minimum)
    return sorted_array


arr = [10, 4, 2, 8]
print sort_array(arr)


