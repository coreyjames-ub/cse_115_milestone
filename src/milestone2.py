import csv

def convertToDictionaries(keys, values):
    out=[]
    for thing in values:
        temp = {}
        for i in range(len(keys)):
            key = keys[i]
            value = thing[i]
            temp[key] = value
        out.append(temp)
    return out

def loadRecords(filename):
    out = []
    with open(filename, "r") as fp:
        reader=csv.reader(fp)
        header = next(reader)
        for row in reader:
            temp = []
            for item in row:
                temp.append(item)
            out.append(row)
    return out

def convertToLists(keys, lod):
    out = []
    for ad in lod:
        temp=[]
        for key in keys:
            temp.append(ad.get(key, ""))
        out.append(temp)
    return out

def writeRecords(filename, records):
    with open(filename,"a") as fp2:
        writer=csv.writer(fp2)
        for row in records:
            writer.writerow(row)
    return None
            
            
