#this script is used to remove empty folders from a folder structure. 

import os

# Define the directory you want to check
directory_path = "./testingFolder"  # Replace with the directory path you want to check

# Recursive function to check and rename empty folders
def check_and_rename_empty_folders(base_directory):
    for root, dirs, files in os.walk(base_directory, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                # If the folder is empty, rename it
                new_folder_name = folder + "_empty"
                new_folder_path = os.path.join(root, new_folder_name)
                os.rename(folder_path, new_folder_path)
                print(f"Folder '{folder}' was empty and has been renamed to '{new_folder_name}'")

def check_and_delete_empty_folders(base_directory):
    for root, dirs, files in os.walk(base_directory, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                # If the folder is empty, delete it
                os.rmdir(folder_path)
                print(f"Folder '{folder}' was empty and has been deleted.")

# Call the recursive function to check and rename empty folders
check_and_delete_empty_folders(directory_path)

print("Empty folder checking and renaming completed.")