import csv
import json

info=[]
Vards=[]
with open("Srk.csv","r",encoding='utf-8') as csv_file:
    reader=csv.DictReader(csv_file)
    for line in reader:
        info.append(line)
    
print(info)
with open("Srk.json","w",encoding='utf-8') as json_file:
    json.dump(info,json_file,indent=4)

for vards in info:
    print(vards['Skolena vards'])
    if vards['Skolena vards'] not in Vards:
        Vards.append(vards['Skolena vards'])
print(Vards)
    
for i in info:
    print(i['Skolena vards'],i["Maksa pusdienam"],"makss pusdienam")
kopa=0
for kb in info:
    k=int(kb["Maksa pusdienam"])
    kopa+=k
print(f"{kopa} ir visu pusdienu summa")