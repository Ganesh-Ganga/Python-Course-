# There are 2 solutions as discussed in the video
# Solution 1 
def merge_dicts(dict1, dict2):
    '''
    Merge two dictionaries into one.

    Parameters:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: A new dictionary with combined key-value pairs
    '''
    return {**dict1, **dict2}

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = merge_dicts(d1, d2)
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Solution 2
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)
print(d1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
