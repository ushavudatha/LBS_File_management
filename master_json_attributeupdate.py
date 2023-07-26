import os
import json
import random
import collections
folder_path='#folder_path'
hm=collections.defaultdict(list)
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        l=filename.split('_')
        l=l[:-1]
        key=[str(int(i[2:])) for i in l[:3]]
        key.append(str(int(l[-1][1:])))
        l=l[:-1]
        hm[tuple(key)]="_".join(l[3:])


with open(os.path.join('#folder_path')) as f:
    data = json.load(f)
    for i,d in enumerate(data):
        search_val=(d[str(i+1)]['key']).split('_')
        key_val=[i[2:] for i in search_val[:3]]
        key_val.append(search_val[-1][1:])
        key_val=tuple(key_val)

        if key_val in hm:
#            print("loop here")
            d[str(i+1)]['key']="_".join(search_val[:3])+"_"+hm[key_val]+"_"+search_val[-1]

with open('master.json', 'w') as f:
    json.dump(data,f)