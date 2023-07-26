import os
import json

# Set the path to the folder containing the files
folder_path = 'J:\\littleblackstar\\h_sh000\\renders\\Pipeline_v531\\json'

# Get a list of all the filenames in the folder
filenames = os.listdir(folder_path)

# Sort the filenames alphabetically
# filenames.sort()

# Create an empty list to store the JSON objects
json_list = []

# Loop through the filenames and create a JSON object for each one
for i, file in enumerate(filenames):
    AA, AB, AF, CT, E, BG, W,v =file.split("_")
    v=v[:-5]
    # Creating a dictionary for each file and adding it to the JSON object
    json_list.append({str(i+1): {"key": f"AA{int(AA[2:])}_AB{int(AB[2:])}_AF{int(AF[2:])}_CT{int(CT[2:])}_E{int(E[1:])}_BG{int(BG[2:])}_W{int(W[1:])}",
                                "remarks": "",
                                "status": "approve",
                                "marked":False}})

# Write the list of JSON objects to a file
with open('master.json', 'w') as f:
    json.dump(json_list,f)