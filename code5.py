user_input = input("Enter a string to write to a file: ")

file_name = "output.txt"

 with open(file_name, 'w') as file:

 file.write(user_input) 

print(f"String has been written to {file_name}")
