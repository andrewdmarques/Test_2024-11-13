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

# Organize the fastq files
def create_barcode_dataframe(files):
    # Create a dictionary to store the barcode as key and list of files as value
    barcode_files = {}
    # Loop through each file in the list
    for file in files:
        # Extract the barcode from the file path, assuming a consistent structure
        barcode = file.split('/')[-2]  # Assumes barcode is always in the same path segment
        # Add the file to the list of files for this barcode in the dictionary
        if barcode in barcode_files:
            barcode_files[barcode].append(file)
        else:
            barcode_files[barcode] = [file]
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(list(barcode_files.items()), columns=['barcode', 'file_list'])
    # Sort the DataFrame alphabetically by the 'barcode' column
    df = df.sort_values(by='barcode', ascending=True)
    # Sort the DataFrame alphabetically by the 'barcode' column
    df_sorted = df.sort_values(by='barcode', ascending=True)
    # Reset the index of the DataFrame
    df_sorted = df_sorted.reset_index(drop=True)
    return df_sorted