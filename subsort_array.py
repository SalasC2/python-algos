# subarray sort

# input: list of ints (pos and/or neg)
# output: list of two indices, start and end of unsorted part of array

# [4, 3, 5]
# [0, 1]
# start = 2
# end = 5

# indices = [2, 5]
# min = 1
# max = 22

# for x in range(0, start):
    # if min < arr[x]:
    #    indices[0] = x
    #    start = x
    #    break

# for y in range(len(arr) - 1, -1, -1):
    # if max >    arr[y]:
        # indices[1] = y
        # end = y
        # break

# indices.append(start)
#


# return [start, end]

# end = 5
# input: [3, 4, 8, 1, 10, 6, 17]
#               n         j

# output: [2, 5]

# t: o(n)
# s: o(1)


def subarray_sort(arr):
    results = [-1, -1]
    if arr == []:
        return results


    i = -1
    j = len(arr)

    minimum = float("inf")
    maximum = -float("inf")

    while i < j:
        i += 1
        if arr[i] > arr[i + 1]:
            start = i
            break

    while j > i:
        j -= 1
        if arr[j] < arr[j - 1]:
            end = j
            break

    for less in range(start, end + 1):
        if minimum > arr[less]:
            minimum = arr[less]

    for high in range(end, start - 1, -1):
        if maximum < arr[high]:
            maximum = arr[high]

    for x in range(0, start):
        if minimum < arr[x]:
            start = x
            results[0] = start
            break

    for y in range(len(arr) -1, start - 1, -1):
        if maximum > arr[y]:
            end = y
            results[1] = end
            break
    return results

print subarray_sort([3, 4, 8, 1, 10, 6, 17])
print subarray_sort([3, 4, 8, 1, 22, 6, 17])


#    indices[0] = x
#    start = x
#    break

