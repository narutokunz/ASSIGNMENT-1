def concatenate_strings(str1, str2):
    concatenated_string = str1 + str2
    return concatenated_string

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = concatenate_strings(string1, string2)

print(f"The concatenated string is: {result}")

