import os

def count_folders(path):
    folder_count = 0

    for root, dirs, files in os.walk(path):
        folder_count += len(dirs)  # Counting immediate subfolders in the current directory

    return folder_count

folder_path = ("Y:\\")
total_folders = count_folders(folder_path)

print(f"Total folders in {folder_path} is {total_folders}")