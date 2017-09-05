#majority element: [1,2,3,4,2,3,2,7,1,2,3,2,7] => 2



def majority_element(array):
    counter = {}
    for x in range(len(array)):
        if array[x] in counter:
            counter[array[x]] += 1
        else:
            counter[array[x]] = 1

    maximum = counter[array[0]]
    max_key = counter[array[0]]
    for key, value in counter.iteritems():
        if value > maximum:
            maximum = value
            max_key = key
    return max_key






print majority_element([1,2,3,4,2,3,2,7,1,2,3,2,7])


