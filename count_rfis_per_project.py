import math
import pandas as pd
import numpy as np
import os
import datetime
import re

def capitalize_words(text):
    # Use regex pattern to match the start of each word
    text = text.replace('B+s', '')
    text = text.replace('_', ' ')
    
    pattern = r"(^|\s)(\w)"
    capitalized_text = re.sub(pattern, lambda match: match.group(1) + match.group(2).upper(), text)
    return capitalized_text

def print_file_date(file_path):
    # Get the file's status
    file_stats = os.stat(file_path)

    # Extract the last modified timestamp
    modified_timestamp = file_stats.st_mtime

    # Convert the timestamp to a datetime object
    modified_datetime = datetime.datetime.fromtimestamp(modified_timestamp)
    
    return modified_datetime
    
#read all folders in the directory
path = r"Z:\B+S ARCHITECTURE\017 JOBS\01712.0 VCHC-720 E Rose Ave Mixed Use\01712.0 6.Construction Admin\01712.0 RFIs\01712.0 RFIs In"



def file_renaming():
    
    for file in files: 
        #print the date of the file
        
        file_name = str(file)
        new_name = capitalize_words(file_name)
        print(new_name)
        
        #rename the files to lower case
        
        
        # Create the full file paths
        old_path = os.path.join(path, file)
        new_path = os.path.join(path, new_name)
        
        # Rename the file
        #os.rename(old_path, new_path)
    
def count_RFIs(path):
    
    li = [] #empty list
    items = os.listdir(path)
    
    for item in items:
        li.append(1)
    
    return len(li)

print(count_RFIs(path))