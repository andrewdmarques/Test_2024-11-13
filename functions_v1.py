#############################################
# Import packages
#############################################
import os  # For file management

#############################################
# Define functions
#############################################

# List all files in a directory recursively
def list_files_recursively(directory):
    all_files = []
    # os.walk() generates directory names and file names in a directory tree
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct the full file path and add it to the list
            all_files.append(os.path.join(root, file))
    return all_files
