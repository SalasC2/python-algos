# reverse a string

def reverse_string(string):
    reverse = ""
    for x in range(len(string)):
        reverse = string[x] + reverse
    return reverse
print reverse_string("car")
