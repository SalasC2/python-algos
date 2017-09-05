# find the most common element in an arrays

def most_common(array):
    counter = {}
    for x in range(len(array)):
        if array[x] in counter:
            counter[array[x]] += 1
        else:
            counter[array[x]] = 1
    return max(counter)
print most_common([1, 1, 4, 5, 6, 6, 6,])
