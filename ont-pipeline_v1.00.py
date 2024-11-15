#!/usr/bin/env python3

#############################################
# Import packages
#############################################
import os  # For file management


#############################################
# User defined variables
#############################################

dir_data = "/var/lib/minknow/data/ONT-02/no_sample_id/20241111_1419_MN23638_FAZ97636_6cd4fac2/fastq_pass"
prefix = "2024-11-14"
dir_working = "/media/andrewdmarques/Data011/Bioinformatics/49_ONT-Processing/Test_2024-11-13/" 

#############################################
# Run
#############################################

# Monitor how the script is running.
script_cont  = True
script_note = 'begin'

# Confirm that we are in the working directory and read in the functions.
os.chdir(dir_working)
from functions_v1 import *

# Determine all of the files that are in the data directory.
file1 = list_files_recursively(dir_data) 

# Remove all files that are not fastq.gz
file2 = [file for file in file1 if file.endswith('.fastq')]

# Determine which files are present in the directory.

