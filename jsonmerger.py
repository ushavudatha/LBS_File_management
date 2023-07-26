import os
import json

data_list_paths = ["J:\\littleblackstar\\dev\\BASE\\data\\master.json",
                  "J:\\littleblackstar\\dev\\bombedcloth\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Bridal style\\data\\master.json",
                  "J:\\littleblackstar\\dev\\commando\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Cover suit\\data\\master.json",
                  "J:\\littleblackstar\\dev\\DENIM CLOTH\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Designer wear\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Floral_shirt\\data\\master.json",
                  "J:\\littleblackstar\\dev\\FX suit\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Jail cos\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Multi_cloth\\data\\master.json",
                  "J:\\littleblackstar\\dev\\NBA\\data\\master.json",
                  "J:\\littleblackstar\\dev\\New hoodie\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Rain coat\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Robe\\data\\master.json",
                  "J:\\littleblackstar\\dev\\ScifiMetal_suit\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Sweatshirt_scarf\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Tron\\data\\master.json",
                  "J:\\littleblackstar\\dev\\Veeraya_outfit\\data\\master.json"
                  ]

all_data = []

for filename in data_list_paths:
        
        with open(filename) as f:
            data = json.load(f)
        temp=[]
        for d in data:
            l=list(d.values())
            if l[0].get("status")=="approve":
                temp.append(l[0])
        all_data.extend(temp)
sorted_list = sorted(all_data, key=lambda x: x['key'][-4:])
final_data=[{index+1:val} for index,val in enumerate(sorted_list)]

with open("master.json", "w") as f:
    json.dump(final_data,f)