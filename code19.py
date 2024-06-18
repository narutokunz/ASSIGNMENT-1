import string

def remove_punctuation(input_string):
    
    translator = str.maketrans('', '', string.punctuation)
    
    cleaned_string = input_string.translate(translator)
    
    return cleaned_string

input_string = input("Enter a string with punctuation: ")

cleaned_string = remove_punctuation(input_string)


print(f"The string without punctuation is: {cleaned_string}")
