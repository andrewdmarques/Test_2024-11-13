#!/usr/bin/env python3

#############################################
# Import packages
#############################################
import os  # For file management
import datetime # For file management
import pandas as pd # For managing dataframes
import subprocess # For running commands like cat on linux

#############################################
# User defined variables
#############################################

dir_data = "/var/lib/minknow/data/ONT-02/no_sample_id/20241111_1419_MN23638_FAZ97636_6cd4fac2/fastq_pass"
prefix = "2024-11-14"
dir_working = "/media/andrewdmarques/Data011/Bioinformatics/49_ONT-Processing/Test-01/"
dir_out = dir_working + prefix + '/' 

#############################################
# Run
#############################################

# Monitor how the script is running.
cont  = True
script_note = ['ONT-Pipeline','Script started: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]

# Confirm that we are in the working directory and read in the functions.
os.chdir(dir_working)
from functions_v1 import *

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

# Calculate (1) reads, (2) quality of each read, (3) 
dir_metrics = dir_out + 'Metrics/'
if not os.path.exists(dir_metrics):
    os.makedirs(dir_metrics)
# Iterate through the files and determine the 
ref1.at[0, 'file_cat']

