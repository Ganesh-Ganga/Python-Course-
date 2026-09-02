l = [10, 11, 12, 13, 14] 

f = lambda x: x%2==0

l2 = list(filter(f, l))
print(l2)