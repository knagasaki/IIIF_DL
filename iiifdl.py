#!/usr/bin/env python3
import urllib.request
import json
import sys

url = sys.argv[1] #'http://www2.dhii.jp/nijl/NIJL0018/099-0014/manifest.json'
readObj = urllib.request.urlopen(url)
data = json.loads(readObj.read().decode('utf-8'))

arImageUrls = []
for seq in data['sequences']:
     for canvas in seq['canvases']:
         for image in canvas['images']:
             arImageUrls.append(image['resource']['service']['@id'])

tLen = len(str(len(arImageUrls))) + 1
fileNumber = 1
print ('downloading...')
for imageUrl in arImageUrls:
    localFilename = str(fileNumber).zfill(tLen)+'.jpg'
    imageUrl = imageUrl+'/full/full/0/default.jpg'
    urllib.request.urlretrieve(imageUrl, localFilename)
    fileNumber = fileNumber + 1
    print (localFilename)
