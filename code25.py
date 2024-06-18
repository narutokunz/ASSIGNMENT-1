def copy_file(source_file, destination_file):
    try:
        
        with open(source_file, 'r') as f:
            
            content = f.read()

      
        with open(destination_file, 'w') as f:
            
            f.write(content)

        print(f"Contents of '{source_file}' copied successfully to '{destination_file}'.")
    
    except FileNotFoundError:
        print("Error: One of the files does not exist.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


