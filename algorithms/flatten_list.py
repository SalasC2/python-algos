## Recursive Function
def flatten(arr):
    if arr == []:
        return arr
    if type(arr[0]) == list:
        return flatten(arr[0]) + flatten(arr[1:])
    return arr[:1] + flatten(arr[1:])

# l = [[2], 3, [], 4, [[6], 7]]
# print(flatten(l)) 
# print(flatten([[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]))

## Use of Helper Function
def single_flat3(arr):
  flatten_l = []
  for ele in arr:
    if type(ele) == list:
      flatten_l.extend(single_flat3(ele))
    else:
      flatten_l.append(ele)
  return flatten_l

def flatten3(arr):
  if not arr:
    return arr
  return single_flat3(arr)

# print(flatten3(l))
# print(flatten3([[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]))

## TODO: In Progress, making custom flatten method called flatten2
# class list(object):

#   def __init__(self):
#     pass
    
#   def single_flat(self, arr): 
#     flatten_l = []
#     for ele in arr:
#       if type(ele) == list:
#         flatten_l.extend(ele)
#       else:
#         flatten_l.append(ele)
#     return flatten_l

#   def multiple_flatten(self, arr, n):
#     counter = 0
#     a = arr
#     while counter < n:
#       a = self.single_flat(a)
#       counter += 1
#     return a

#   def flatten2(self, arr, n):
#     if not arr:
#       return arr
#     if n is None:
#       return self.single_flat(arr)
#     else:
#       return self.multiple_flatten(arr, n)

# print(list().flatten2([], None))

# print(list().flatten2(l, len(l)))