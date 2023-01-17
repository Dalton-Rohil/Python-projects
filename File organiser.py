import os
import shutil

# Function to organize files
def organize_files(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Create a dictionary to store the file types as keys and lists of corresponding files as values
    file_types = {}

    # Iterate through the list of files
    for file in files:
        # Get the file extension
        file_extension = os.path.splitext(file)[1][1:]

        # Check if the file extension already exists in the dictionary
        if file_extension in file_types:
            # If it does, append the file to the list of files for that file extension
            file_types[file_extension].append(file)
        else:
            # If it doesn't, create a new key for the file extension and add the file to the list
            file_types[file_extension] = [file]

    # Iterate through the dictionary of file types
    for file_type in file_types:
        # Create a new directory for the file type if it doesn't already exist
        if not os.path.exists(os.path.join(directory, file_type)):
            os.makedirs(os.path.join(directory, file_type))

        # Move all the files of that type to the new directory
        for file in file_types[file_type]:
            shutil.move(os.path.join(directory, file), os.path.join(directory, file_type))

# specify the directory you want to organize
organize_files("/path/to/directory")