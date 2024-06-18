def string_to_list_of_characters(input_string):
    
    characters_list = list(input_string)
    return characters_list


input_string = "Hello, World!"


characters_list = string_to_list_of_characters(input_string)


print(f"The string '{input_string}' converted to a list of characters:")
print(characters_list)
