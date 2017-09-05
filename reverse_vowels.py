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

# 0 1 2 3 4 5 6 7 8 9
# w h i t e b o a r d
#             b
#         e

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
