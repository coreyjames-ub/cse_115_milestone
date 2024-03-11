#SAMPLE DATA
data = [ {'Title': 'SOLE PARK', 'Category': 'SCULPTURE', 'Type': 'RELIEF',
'Medium': 'STONE', 'Frame': 'false', 'Photo URL Link': 'UNKNOWN',
'Artist':'UNKNOWN', 'Street Address': 'BUSTI AVE & NIAGARA ST', 'City': 'BUFFALO',
'Zipcode': '14213', 'State': 'NY'},
{'Title': 'BUFFALO STREET MAP', 'Category': 'GRAPHIC ARTS', 'Type': 'MAP',
'Medium': 'PARCHMENT', 'Frame': 'true', 'Photo URL Link': 'UNKNOWN',
'Artist': 'SMITH BROTHERS COMPANY', 'Street Address': '65 NIAGARA SQUARE',
'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
{'Title': 'WAR  MEMORIAL STADIUM RENDERING', 'Category': 'GRAPHIC ARTS',
'Type': 'DRAWING', 'Medium': 'PAPER', 'Frame': 'false', 'Photo URL Link':
'UNKNOWN', 'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARA SQUARE',
'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
{'Title': 'MAYOR HIRAM BARTON', 'Category': 'PAINTINGS', 'Type': 'PORTRAIT',
'Medium': 'OIL ON CANVAS', 'Frame': 'true', 'Photo URL Link':
'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/HIRAM%20BARTON.HTML', 'Artist': 'UNKNOWN',
 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
{'Title': 'MAYOR ELI COOK', 'Category': 'GRAPHICS ARTS', 'Type': 'PORTRAIT',
'Medium': 'PASTEL ON PAPER', 'Frame': 'true', 'Photo URL Link':
'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/ELI%20COOK.HTML', 'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARA SQUARE',
'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
{'Title': 'MAYOR ANTHONY MASIELLO', 'Category': 'PAINTINGS', 'Type':
'PORTRAIT', 'Medium': 'OIL ON CANVAS', 'Frame': 'true', 'Photo URL Link':
'UNKNOWN', 'Artist': 'NATHAN NAETZKER', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
{'Title': 'MAYOR CHANDLER J WELLS', 'Category': 'PAINTINGS', 'Type':
'PORTRAIT', 'Medium': 'OIL ON CANVAS', 'Frame': 'true', 'Photo URL Link':
'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/CHANDLER%20WELLS.HTML', 'Artist': 'ALVAH BRADISH',
 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'} ]
##################################################################################################################################

def getValuesForKey(key, records):
    out=[]
    for ad in records:
        temp=ad.get(key,-1)
        if (temp != -1) and temp not in out:
            out.append(temp)
    return out

# Test Cases for function getValuesForKey()
def getValuesForKeysTestCaseRunner():
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Test Cases for function getValuesForKey(key, records)')
    print("-----------------------------------------------------")
    testCasesExpected=[['SOLE PARK', 'BUFFALO STREET MAP', 'WAR  MEMORIAL STADIUM RENDERING', 'MAYOR HIRAM BARTON', 'MAYOR ELI COOK',
                        'MAYOR ANTHONY MASIELLO', 'MAYOR CHANDLER J WELLS'],
                       ['SCULPTURE', 'GRAPHIC ARTS', 'PAINTINGS', 'GRAPHICS ARTS'],
                       ['RELIEF', 'MAP', 'DRAWING', 'PORTRAIT'],
                       ['STONE', 'PARCHMENT', 'PAPER', 'OIL ON CANVAS', 'PASTEL ON PAPER'],
                       ['false', 'true'],
                       ['UNKNOWN', 'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/HIRAM%20BARTON.HTML',
                        'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/ELI%20COOK.HTML',
                        'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/CHANDLER%20WELLS.HTML'],
                       ['UNKNOWN', 'SMITH BROTHERS COMPANY', 'NATHAN NAETZKER', 'ALVAH BRADISH'],
                       ['BUSTI AVE & NIAGARA ST', '65 NIAGARA SQUARE'],
                       ['BUFFALO'],
                       ['14213', '14202'],
                       ['NY']
                       ]
    testCases=['Title', 'Category', 'Type', 'Medium', 'Frame', 'Photo URL Link', 'Artist', 'Street Address', 'City', 'Zipcode', 'State']
    expectedCount=0
    for testCase in testCases:
        result = getValuesForKey(testCase, data)
        if (result == testCasesExpected[expectedCount]):
            print('TEST CASE '+testCase+' ... PASS')
        else:
            print('TEST CASE '+testCase+' ... FAIL')
            print('Expected: ')
            print(testCasesExpected[expectedCount])
            print("-----------------------------------------------------")
            print("But got: ")
            print(result)
        expectedCount+=1
        print("-----------------------------------------------------")
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        
getValuesForKeysTestCaseRunner()

##################################################################################################################################

def countMatchesByKey(key, value, records):
    count=0
    for record in records:
        temp=record.get(key,-1)
        if (temp == value):
                count+=1
    return count

# Test Cases for countMatchesByKey()
def countMatchesByKeyTestCaseRunner():
    testCasesExpected=[1, 3, 1, 3, 5, 4, 1, 6, 7, 6, 7]
    testCases=['Title', 'Category', 'Type', 'Medium', 'Frame', 'Photo URL Link', 'Artist', 'Street Address', 'City', 'Zipcode', 'State']
    values=["MAYOR ELI COOK", "PAINTINGS", "MAP", "OIL ON CANVAS", "true", "UNKNOWN", "NATHAN NAETZKER", "65 NIAGARA SQUARE", "BUFFALO", "14202", "NY"]
    expectedCount=0
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Test Cases for function countMatchesByKeyTestCaseRunner(key, value, records)')
    print("-----------------------------------------------------")
    for testCase in testCases:
        result = countMatchesByKey(testCase, values[expectedCount], data)
        if (result == testCasesExpected[expectedCount]):
            print('TEST CASE '+testCase+' ... PASS')
        else:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('TEST CASE '+testCase+' ... FAIL')
            print('Expected: ')
            print(testCasesExpected[expectedCount])
            print("-----------------------------------------------------")
            print("But got: ")
            print(result)
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        expectedCount+=1
        print("-----------------------------------------------------")
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

countMatchesByKeyTestCaseRunner()                

##################################################################################################################################

def countMatchesByKeys(key1, value1, key2, value2, records):
    count=0
    for record in records:
        temp1=record.get(key1,-1)
        temp2=record.get(key2,-2)
        if (temp1 == value1) and (temp2 == value2):
            count+=1
    return count

def countMatchesByKeysTestRunner():
    testCasesExpected=[1, 2, 3]
    key1=['Artist','Artist', 'Medium']
    value1=['NATHAN NAETZKER', 'UNKNOWN', 'OIL ON CANVAS']
    key2=['Category', 'Photo URL Link', 'Frame']
    value2=['PAINTINGS', 'UNKNOWN', 'true']
    expectedCount=0
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Test Cases for function countMatchesByKeys(key1, value1, key2, value2, records)')
    for expectedResult in testCasesExpected:
        result = countMatchesByKeys(key1[expectedCount], value1[expectedCount], key2[expectedCount], value2[expectedCount], data)
        if (result == expectedResult):
            print('TEST CASE key1 = '+key1[expectedCount]+' with key2 = '+key2[expectedCount]+' ... PASS')
        else:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('TEST CASE key1 = '+key1[expectedCount]+' with key2 = '+key2[expectedCount]+' ... FAIL')
            print('Expected: ')
            print(expectedResult)
            print("-----------------------------------------------------")
            print("But got: ")
            print(result)
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        expectedCount+=1
        print("-----------------------------------------------------")
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

countMatchesByKeysTestRunner()

##################################################################################################################################        

def filterByKey(key, value, records):
    out=[]
    for record in records:
        temp=record.get(key,-1)
        if (temp == value):
            out.append(record)
    return out

def filterByKeyTestRunner():
    testCasesExpected=[[{'Title': 'SOLE PARK', 'Category': 'SCULPTURE', 'Type': 'RELIEF', 'Medium': 'STONE', 'Frame': 'false',
                         'Photo URL Link': 'UNKNOWN', 'Artist': 'UNKNOWN', 'Street Address': 'BUSTI AVE & NIAGARA ST', 'City': 'BUFFALO',
                         'Zipcode': '14213', 'State': 'NY'}],
                       [{'Title': 'MAYOR ELI COOK', 'Category': 'GRAPHICS ARTS', 'Type': 'PORTRAIT', 'Medium': 'PASTEL ON PAPER', 'Frame': 'true',
                         'Photo URL Link': 'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/ELI%20COOK.HTML',
                         'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'}],
                       [{'Title': 'MAYOR HIRAM BARTON', 'Category': 'PAINTINGS', 'Type': 'PORTRAIT', 'Medium': 'OIL ON CANVAS', 'Frame': 'true',
                         'Photo URL Link': 'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/HIRAM%20BARTON.HTML',
                         'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
                        {'Title': 'MAYOR ELI COOK', 'Category': 'GRAPHICS ARTS', 'Type': 'PORTRAIT', 'Medium': 'PASTEL ON PAPER', 'Frame': 'true',
                         'Photo URL Link': 'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/ELI%20COOK.HTML',
                         'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
                        {'Title': 'MAYOR ANTHONY MASIELLO', 'Category': 'PAINTINGS', 'Type': 'PORTRAIT', 'Medium': 'OIL ON CANVAS', 'Frame': 'true',
                         'Photo URL Link': 'UNKNOWN', 'Artist': 'NATHAN NAETZKER', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO',
                         'Zipcode': '14202', 'State': 'NY'},
                        {'Title': 'MAYOR CHANDLER J WELLS', 'Category': 'PAINTINGS', 'Type': 'PORTRAIT',
                         'Medium': 'OIL ON CANVAS', 'Frame': 'true',
                         'Photo URL Link': 'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/CHANDLER%20WELLS.HTML',
                         'Artist': 'ALVAH BRADISH', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'}]]
    keys=['Category', 'Medium',  'Type']
    values=['SCULPTURE', 'PASTEL ON PAPER', 'PORTRAIT']
    expectedCount=0
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Test Cases for filterByKey(key, value, records)')
    print("-----------------------------------------------------")
    for key in keys:
        result = filterByKey(key, values[expectedCount], data)
        if (result == testCasesExpected[expectedCount]):
            print('TEST CASE '+key+' ... PASS')
        else:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('TEST CASE '+key+' ... FAIL')
            print('Expected: ')
            print(testCasesExpected[expectedCount])
            print("-----------------------------------------------------")
            print("But got: ")
            print(result)
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        expectedCount+=1
        print("-----------------------------------------------------")
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

filterByKeyTestRunner()                      

##################################################################################################################################

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

def computeFrequencyTestCaseRunner():
    testCasesExpected=[{'SCULPTURE': 1, 'GRAPHIC ARTS': 2, 'PAINTINGS': 3, 'GRAPHICS ARTS': 1}, {'RELIEF': 1, 'MAP': 1, 'DRAWING': 1, 'PORTRAIT': 4},
                       {'STONE': 1, 'PARCHMENT': 1, 'PAPER': 1, 'OIL ON CANVAS': 3, 'PASTEL ON PAPER': 1}, {'false': 2, 'true': 5}]
    keys=['Category', 'Type', 'Medium', 'Frame']
    expectedCount=0
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Test Cases for computeFrequency(key, records)')
    print("-----------------------------------------------------")
    for key in keys:
        result = computeFrequency(key, data)
        if (result == testCasesExpected[expectedCount]):
            print('TEST CASE '+key+' ... PASS')
        else:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('TEST CASE '+key+' ... FAIL')
            print('Expected: ')
            print(testCasesExpected[expectedCount])
            print("-----------------------------------------------------")
            print("But got: ")
            print(result)
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        expectedCount+=1
        print("-----------------------------------------------------")
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

computeFrequencyTestCaseRunner()

##################################################################################################################################
