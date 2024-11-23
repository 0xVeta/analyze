import os

# Define the directory to search
directory = 'src/mercal/'

# Define the text to find and the text to replace
text_to_find = "leash"
text_to_replace = "restrain"

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.py'):  # Check for Python files
        file_path = os.path.join(directory, filename)
        
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Replace the specified text
        new_content = content.replace(text_to_find, text_to_replace)
        
        # Write the changes back to the file only if changes were made
        if new_content != content:
            with open(file_path, 'w') as file:
                file.write(new_content)
            print(f"Updated: {file_path}")