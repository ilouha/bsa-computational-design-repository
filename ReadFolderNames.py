import os

#create a list from all the folders in the following folder path: Y:\
folderList = os.listdir("Y:\\")
revised_names = [] 

dic = {}

for folder in folderList:
    
    li_temp = []
    #check if the folder is a file or a folder
    if os.path.isdir("Y:\\" + folder):
        
        li_temp = os.listdir("Y:\\" + folder + "\\")
        for file in li_temp:
            file_name = file.capitalize()
            
            #replace the file with file_name in li_temp
            li_temp[li_temp.index(file)] = file_name
        
    dic[folder.capitalize()] = li_temp


#read a json file to data
import json
filename = "folder_names.json"
with open(filename, 'r') as file:
    data = json.load(file)

filename = "folder_names.txt"

with open(filename, 'w') as file:
    for key, value in data.items():
        file.write(f"{key}: {value}\n")