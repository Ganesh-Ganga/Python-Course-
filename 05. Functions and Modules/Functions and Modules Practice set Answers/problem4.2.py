def sum_of_digits(n):
    if n == 0:
        return 0
    
    return n%10 + sum_of_digits(n//10)


# sum of digits of 7532 is same as:
# 2 (last digit) + sum of digits of 753
print(sum_of_digits(7532))