# Question:
# Write a program that takes a list of numbers and removes all duplicates using a set.

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

unique_numbers = list(set(numbers))

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)
