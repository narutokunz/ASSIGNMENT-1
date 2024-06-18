def convert_to_title_case(input_string):
    
    title_case_string = input_string.title()
    return title_case_string

input_string = input("Enter a string to convert to title case: ")


title_case_string = convert_to_title_case(input_string)

print(f"The title case version of the string is: {title_case_string}")
