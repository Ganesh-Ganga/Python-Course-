from functools import reduce

l =  [1, 2, 3, 4] 

product = lambda a, b: a*b

print(reduce(product, l))
