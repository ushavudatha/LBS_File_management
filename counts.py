import csv
from collections import Counter
import os

csv_list_paths = ["J:\\littleblackstar\\dev\\BASE\\csv\\BASE_v009.csv",
                  "J:\\littleblackstar\\dev\\bombedcloth\\csv\\Bombedcloth_v004.csv",
                  "J:\\littleblackstar\\dev\\Bridal style\\csv\\Bridal style_v005.csv",
                  "J:\\littleblackstar\\dev\\commando\\csv\\Commando_v005.csv",
                  "J:\\littleblackstar\\dev\\Cover suit\\csv\\Cover suit_v003.csv",
                  "J:\\littleblackstar\\dev\\DENIM CLOTH\\csv\\DENIM CLOTH_v002.csv",
                  "J:\\littleblackstar\\dev\\Designer wear\\csv\\Designer_wear_v003.csv",
                  "J:\\littleblackstar\\dev\\Floral_shirt\\csv\\Floral shirt_v004.csv",
                  "J:\\littleblackstar\\dev\\FX suit\\csv\\FX_suit_v002.csv",
                  "J:\\littleblackstar\\dev\\Jail cos\\csv\\Jailcos_v003.csv",
                  "J:\\littleblackstar\\dev\\Multi_cloth\\csv\\Multi_cloth_v003.csv",
                  "J:\\littleblackstar\\dev\\NBA\\csv\\NBA_v007.csv",
                  "J:\\littleblackstar\\dev\\New hoodie\\csv\\NEW Hoodie_v003.csv",
                  "J:\\littleblackstar\\dev\\Rain coat\\csv\\Raincoat_v004.csv",
                  "J:\\littleblackstar\\dev\\Robe\\csv\\Robe_v004.csv",
                  "J:\\littleblackstar\\dev\\ScifiMetal_suit\\csv\\ScifiMetal_suit_v002.csv",
                  "J:\\littleblackstar\\dev\\Sweatshirt_scarf\\csv\\Sweatshirt_v004.csv",
                  "J:\\littleblackstar\\dev\\Tron\\csv\\Tron_v004.csv",
                  "J:\\littleblackstar\\dev\\Veeraya_outfit\\csv\\Veeraya_outfit_v003.csv"
                  ]

total_values = Counter()
eachfile_values = {}
len_list={}

for filename in csv_list_paths:
        each_file=Counter()
        with open(filename) as csvfile:
            csvreader = csv.reader(csvfile)
            header= next(csvreader)
            
            for row in csvreader:
                if len(row) >= 3:
                    total_values[row[0][-4:]] += 1
                    total_values[row[1][-4:]] += 1
                    total_values[row[2][-4:]] += 1
                    each_file[row[0][-4:]]+=1
                    each_file[row[1][-4:]]+=1
                    each_file[row[2][-4:]]+=1
            len_list[filename]=sum(each_file.values())
        eachfile_values[filename]=each_file

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

print("\n\nTotal NFTS count")
print(sum([i//3 for i in len_list.values()]))
print()
for k,v in eachfile_values.items():
    count = 0
    print()
    print("\n**  "+k+"   **"+"\n")
    for key, value in sorted(v.items()):
        print(f"{key}: {value}", end="  ")
        count += 1
        if count == 10:
            print()
            count = 0