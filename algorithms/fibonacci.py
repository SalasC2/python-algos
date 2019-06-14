
#
# Your last Python code is saved below:
#
#
#
# # 1 1 2 3 5 8 13
# # fibonacci
# # input: index of the fibonacci sequence
# # output: number at index of the fibonacci sequence
#
#
# # 0 1 1 2 3
#
# # input: 0
# # output: 0
#
# # input: 3
# # output: 2
#
# # space : O(n)
#
# # Create an array to store numbers. Start with an array of [0, 1]
# # You'll be adding the last number before the last index.
# # loop 3 times and the end result 0 1 1 2
#
# # 15 on the next call I call n of 3.
#
# # def fibonacci(n):
# #     fib = [0, 1]
# #     for x in range(1, n):
# #         sum = fib[x - 1] + fib[x]
# #         fib.append(sum)
#
# #     print fib[n]
#
# # fibonacci(3)
#
#
# cache = {0: 0, 1: 1}
#
def fibonacci(idx):
    # Something to state that idx already exists and you already know the value
    # if idx is in the cache {1 ==> 1, 2 ==> 1, 3 ,4}
    # {0 == > 1, 1 == > 1, }
    # is 5 in the cache, no, create_fib(3) === > is 3 in the cache create_fib(2)
    cache = {0: 0, 1: 1}

    def fibonacci_helper(n):

        if n < 0:
            return 0

        if n in cache:
            return cache[n]

        cache[n] = fibonacci_helper(n - 2) + fibonacci_helper(n - 1)
        return cache[n]

    fibonacci_helper(idx)
    print(cache)
    return cache[idx]


print(fibonacci(5))




#
#
#
#
#
# #     fib(5)
# #     /  \
# # fib(4)    fib(3)
# #    /  \
# # fib(2) fib(3)
#
# # fib(0) fib(1)
# # # 0     # 1
#
#
# # [0, 1, 1, 2, ]
#
#
#

