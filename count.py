import csv
from collections import Counter
import os

total_values = Counter()
len_list={}
counts = {}


with open('J:\\littleblackstar\\LBSAPE_NFT\\dev\\master\\csv\\master_v001.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip the header row
    for row in reader:
        key = row[4][-3:]
        total_values[row[0][-4:]] += 1
        total_values[row[1][-4:]] += 1
        total_values[row[2][-4:]] += 1
        for i in range(3):
            if key not in counts:
                counts[key]={}
            if row[i][-4:] not in counts[key]:
                counts[key][row[i][-4:]]=0
            counts[key][row[i][-4:]]+=1

for k,v in len_list.items():
    print(str(k[:-4])+ ":: "+str(v//3))

print("\nEach Accessory Occurences are below")
count = 0
for key, value in sorted(total_values.items()):
    print(f"{key}: {value}", end="  ")
    count += 1
    if count == 10:
        print()
        count = 0



# print("\n\nTotal NFTS count")
# print(sum([i//3 for i in len_list.values()]))
# print()
l = []
for k, v in counts.items():
    count = 0
    print()
    print("\n**  "+k+"   **"+"\n")
    for key, value in sorted(v.items()):
        print(f"{key}: {value}", end="  ")
        count += 1
        if count == 10:
            print()
            count=0
    print("\n\nNFT's with this wear")
    l.append(sum(v.values())//3)
    print(l[-1])
    print()
print("\nTotal Number of NFT's")
print(sum(l))