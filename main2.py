import csv
import json

songs=[]
year=[]
count_year=[]
with open("sptf.csv","r",encoding='utf-8') as csv_file:
    reader=csv.DictReader(csv_file)
    for line in reader:
        songs.append(line)
    #print(songs)

with open("sptf.json","w",encoding='utf-8') as json_file:
    json.dump(songs,json_file,indent=4)


for song in songs:
    print(song['Title'])
    if song['Year'] not in year:
        year.append(song['Year'])
print(year)
song_count=0
for year in year:
    for song in songs:
        if song['Year']==year:
            song_count+=1
count_year.append(song_count)
        
print(year)    
print(count_year)