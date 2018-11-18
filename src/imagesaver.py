#csv code based on code from mfitzp on https://stackoverflow.com/questions/16043011/how-to-extract-certain-csv-data-based-on-the-header-in-python
#saves images in their respective class folder 
import csv
import requests
import pathlib

filename = 'C:\\meme-machine-learning\\memegenerator-dataset\\memegenerator.csv'
savepath = 'C:\\meme-machine-learning\\images\\'
memeID = '﻿Meme ID'
classID = 'Base Meme Name'
width = '100' #pixels
height = '100' #pixels

url = [] # This will contain our data
classes = [] # This will contain our data

# Create a csv reader object to iterate through the file
reader = csv.reader( open( filename, 'r', encoding='utf8'), delimiter='\t', dialect='excel')

hrow = next(reader)# Get the top row
memeidx = hrow.index(memeID) # Find the column of the data you're looking for
classidx = hrow.index(classID) # Find the column of the data you're looking for

# gather the data
counter = 0
try:
    for row in reader:
        url.append('http://memegenerator.net/img/instances/' + width + 'x' + height + '/' + row[memeidx] + '.jpg' )
        if row[classidx] not in classes:
            pathlib.Path(savepath + '\\' + row[classidx]).mkdir(parents=True, exist_ok=True);
            classes.append(row[classidx])
        with open(savepath + row[classidx] + '\\pic' + str(counter) + '.jpg', 'wb') as handle:
            response = requests.get(url[counter], stream=True)
            if not response.ok:
                print (response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
        counter = counter + 1
        print(counter)
except csv.error as e:
    print (e)

print (len(classes))
