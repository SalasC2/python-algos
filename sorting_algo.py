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






# reverse vowels: whiteboard

# w
# h
# a
# t
# o
# b
# e
# i
# r
# d

# 0 1 2 3 4 5 6 7 8 9
# w h i t e b o a r d
#             b
#         e

#what
def reverse_vowels(string):
    vowels = "aeiou"
    beginning = 0
    ending = len(string) - 1
    while beginning < len(string):
        if string[beginning] in vowels:
            if string[ending] in vowels:
                print string[ending]
                beginning += 1
            ending -= 1
        else:
            print string[beginning]
            beginning += 1


reverse_vowels("whiteboard")
