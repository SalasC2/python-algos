# search in a string or an array

def search(element, target):
    for x in range(len(element)):
        if element[x] == target:
            return x

string = "something"
array = [1, 3, 5, 9]
print search(array, 5)
