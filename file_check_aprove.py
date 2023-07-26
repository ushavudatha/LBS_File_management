import json
import os

# Folder path
folder_path = "/Users/ushavudatha/downloads/QC"

# Path to the JSON file
json_file_path = "/Users/ushavudatha/downloads/master1.json"

# Load the JSON file
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

# Get the list of file names in the folder
file_names = os.listdir(folder_path)
formatted_file_names=[]
for file in file_names:
    AA,AB,AF,E,CT,W, BG,v = file.split("_")
    # Format the file name according to the desired format
    formatted_file_names.append(f"AA{int(AA[2:])}_AB{int(AB[2:])}_AF{int(AF[2:])}_CT{int(CT[2:])}_E{int(E[1:])}_BG{int(BG[2:])}_W{int(W[1:])}")


json_list=[]
json_list1=[]
# Iterate through each entry in the JSON data
for i in range(len(json_data)):
    # Extract the file name and status from the JSON entry
    file_name = json_data[i][str(i+1)]["key"]
    status = json_data[i][str(i+1)]["status"]
    # AA,AB,AF,E,CT,W, BG = file_name.split("_")

    # Check if the file is present in the folder
    if file_name in formatted_file_names:
        # If the file is present, change the status to "approve"
        json_list.append({str(i+1): {"key": file_name,"remarks": "","status": "approve","marked":False}})
        json_list1.append({str(i+1): {"key": file_name,"remarks": "","status": "approve","marked":False}})
        # json_data[i][str(i+1)]["status"] = "approve"
    else:
        # If the file is not present, mark the status as "revert"
        json_list.append({str(i+1): {"key": file_name,"remarks": "","status": "revert","marked":False}})

# Write the modified JSON data back to the file
with open('master1.json', 'w') as f:
    json.dump(json_list,f)
with open('master_approved.json', 'w') as f:
    json.dump(json_list1,f)
