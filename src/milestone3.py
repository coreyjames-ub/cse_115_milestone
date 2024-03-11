import os
import urllib.request
import milestone1
import milestone2
import json
import csv
import matplotlib.pyplot as plt
import numpy as np

def cacheAndLoadData(file):
    keys = ['title','category','type','medium','frame','photo_url_link','artist','site','street_address','city','zip_code','state','latitude','longitude']
    if not os.path.isfile(file):
        url = 'https://data.buffalony.gov/resource/6xz2-syui.json'
        res = urllib.request.urlopen(url)
        content = json.loads(res.read().decode())
        aLst=milestone2.convertToLists(keys,content)
        with open(file,"w") as fp:
            writer=csv.writer(fp)
            writer.writerow(keys)
        milestone2.writeRecords(file,aLst)
    values=milestone2.loadRecords(file)
    out=milestone2.convertToDictionaries(keys,values)
    return out

def cleanData(data):
    for ad in data:
        dataAdVal = ad["category"]
        if "PAINTING" in dataAdVal:
            ad["category"]="PAINTING"
        elif "DECORATIVE OBJECT" in dataAdVal:
            ad["category"]="DECORATIVE OBJECT"
        elif "GRAPHIC"  in dataAdVal[0:8]:
            ad["category"]="GRAPHIC ARTS"
    return None

def plotPieForKey(key,data):
    dataFreq = milestone1.computeFrequency(key,data)
    labels = dataFreq.keys()
    sizes=[]
    for aKey in labels:
        val=dataFreq[aKey]
        sizes.append(val)
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.f%%')
    plt.show()
    return None

def plotBarForKey(key, data):
    dataFreq=milestone1.computeFrequency(key,data)
    labels= dataFreq.keys()
    x=np.array(list(labels))
    sizes=[]
    for aKey in labels:
        val=dataFreq[aKey]
        sizes.append(val)
    y=np.array(sizes)
    plt.barh(x,y)
    plt.show()
    return None

def plotFilteredBarForKey(key,fkey,fval,data):
    fData=milestone1.filterByKey(fkey,fval,data)
    dataFreq = milestone1.computeFrequency(key,fData)
    labels= dataFreq.keys()
    x=np.array(list(labels))
    sizes=[]
    for aKey in labels:
        val=dataFreq[aKey]
        sizes.append(val)
    y=np.array(sizes)
    plt.barh(x,y)
    plt.show()
    return None


out=cacheAndLoadData("corey.csv")
cleanData(out)
plotPieForKey('category', out)
plotBarForKey('category', out)
plotFilteredBarForKey('type', 'category', 'PAINTING', out)

        
        
