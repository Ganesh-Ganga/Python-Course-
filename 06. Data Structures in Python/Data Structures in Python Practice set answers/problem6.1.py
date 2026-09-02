def remove_duplicates(numbers):
    '''
    Remove duplicates from a list using a set.

    Parameters:
        numbers (list): A list of integers or floats.

    Returns:
        list: A new list with duplicates removed.
    '''
    return list(set(numbers))

 
nums = [1, 2, 3, 2, 4, 1, 5, 3]
print("Original list:", nums)
print("Without duplicates:", remove_duplicates(nums))
