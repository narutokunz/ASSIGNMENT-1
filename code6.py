file_name = "sample.txt"

with open(file_name, 'r') as file:
    file_content = file.read()

print("Content of the file:")
print(file_content)

