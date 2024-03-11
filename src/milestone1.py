def getValuesForKey(key, records):
    out=[]
    for ad in records:
        temp=ad.get(key,-1)
        if (temp != -1) and temp not in out:
            out.append(temp)
    return out

def countMatchesByKey(key, value, records):
    count=0
    for record in records:
        temp=record.get(key,-1)
        if (temp == value):
                count+=1
    return count

def countMatchesByKeys(key1, value1, key2, value2, records):
    count=0
    for record in records:
        temp1=record.get(key1,-1)
        temp2=record.get(key2,-2)
        if (temp1 == value1) and (temp2 == value2):
            count+=1
    return count

def filterByKey(key, value, records):
    out=[]
    for record in records:
        temp=record.get(key,-1)
        if (temp == value):
            out.append(record)
    return out

def computeFrequency(key, records):
    out={}
    for record in records:
        value=record.get(key,-1)
        if (value != -1):
            temp=out.get(value,-1)
            if (temp != -1):
                out[value]=temp+1
            else:
                out[value]=1
    return out
