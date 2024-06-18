def find_min_max(numbers):
    
    if not numbers:
        return None, None
    
    
    min_value = min(numbers)
    max_value = max(numbers)
    
    return min_value, max_value


numbers_list = [3, 8, 1, 6, 2, 9, 4, 7]


min_val, max_val = find_min_max(numbers_list)

print(f"The minimum value in the list is: {min_val}")
print(f"The maximum value in the list is: {max_val}")
