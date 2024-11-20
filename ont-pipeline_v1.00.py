#!/usr/bin/env python3

#############################################
# Import packages
#############################################
import os  # For file management
import datetime # For file management
import sys # For calling the functions file
import pandas as pd # For managing dataframes
import subprocess # For running commands like cat on linux

#############################################
# User defined variables
#############################################

dir_data = "/var/lib/minknow/data/ONT-02/no_sample_id/20241111_1419_MN23638_FAZ97636_6cd4fac2/fastq_pass"
prefix = "2024-11-14"
dir_working = "/media/andrewdmarques/Data011/Bioinformatics/49_ONT-Processing/Test-01/"
file_function = "/media/andrewdmarques/Data011/Bioinformatics/49_ONT-Processing/Test_2024-11-13/functions_v1.py"
dir_out = dir_working + prefix + '/' 

#############################################
# Run
#############################################

# Monitor how the script is running.
cont  = True
script_note = ['ONT-Pipeline','Script started: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]

# Confirm that we are in the working directory and read in the functions.
os.chdir(dir_working)
module_dir, module_file = os.path.split(file_function)
module_name = module_file[:-3]
sys.path.insert(0, module_dir)
import functions_v1

# Determine all of the files that are in the data directory.
file1 = list_files_recursively(dir_data) 

# Remove all files that are not fastq.gz
file2 = [file for file in file1 if file.endswith('.fastq.gz')]
if len(file2) == 0:
    cont = False
    script_note =  [script_note,'Error: No fastq.gz files detected']

# Organize the fastq files:
if cont == True:
    ref1 = create_barcode_dataframe(file2)

# Combine all sequence reads for each barcode together into a file and save it in the working date out dir (dir_out).
for index, row in ref1.iterrows():
    # Construct new file path using dir_out and barcode
    new_file_path = f"{dir_out}Fastq/{row['barcode']}.fastq.gz"
    # Assign the new file path to the new column 'file_cat'
    ref1.at[index, 'file_cat'] = new_file_path
if not os.path.exists(dir_out + 'Fastq/'):
    os.makedirs(dir_out + 'Fastq/')
# Iterate through each row of the data frame and concatinate all files from a barcode together.
concatenate_files(ref1)

# Prepare the metrics directory. This will be where the gz files will be unzipped and manually assessed.
dir_metrics = dir_out + 'Metrics/'
if not os.path.exists(dir_metrics):
    os.makedirs(dir_metrics)

# Process each of the barcodes individually
for xx in range(len(ref1)):
    # Unzip the gz file to the barcode directory.
    dir_bar = dir_metrics + ref1.at[xx, 'barcode'] + '/'
    file_temp = dir_bar + os.path.basename(ref1.at[xx, 'file_cat']).replace('.gz','')
    if not os.path.exists(dir_bar):
        os.makedirs(dir_bar)
    os.system('gunzip -c ' + ref1.at[xx, 'file_cat'] + ' > ' + file_temp)
    print(xx)

# Determine how many lines are present in the file.
# Open the file, read lines, and count them
with open(file_temp, 'r') as file:
    line_count = sum(1 for line in file)/4
    # Enumerate the lines, starting the count from 1 for simplicity
    for ii, line in enumerate(file, 1):
        # Check if the line number is the second line or every fourth line after that
        if (ii - 2) % 4 == 0:
            seq = line.strip()  # Add line to list, stripping newline characters
            print(seq)










# Iterate through the files and determine the 
ref1.at[0, 'file_cat']

