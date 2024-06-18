def count_occurrences(input_list, element):
    
    count = 0
    
    for item in input_list:
        if item == element:
            count += 1
    
    return count

example_list = [1, 2, 3, 4, 2, 2, 5, 2, 6]


element_to_count = 2

occurrences = count_occurrences(example_list, element_to_count)

print(f"The number of occurrences of {element_to_count} in the list is: {occurrences}")
