import time

t1 = time.time()

numOutput = 50

f = 'CENSUSPROFILE2016.csv'

num = 1
listing = list()

while num < (numOutput + 1):
    listing.append(('censusprofile2016_part'+str(num)))
    num += 1

def listItem(listName, itemIndex):
    '''chooses the correct item from our list'''
    i = 0
    for a in listName:
        if str(listName[i]) == str(listName[itemIndex]):
            return a
        else: i += 1

counter = 0
rowNumber = 1000000
index = 0
condition = False
holdingLine = ''

with open(f) as cur:
    for line in cur.readlines():
        if counter < rowNumber:
            if condition != True:
                try:
                    csvName = listItem(listing, index)
                    csv = open((csvName+'.txt'), 'w')
                    condition = True
                except Exception as f: print(str(f))
            try: csv.write(holdingLine)
            except Exception as e: print(str(e))
            csv.write(line)

        else:
            csv.close()
            condition = False
            index += 1
            rowNumber += 1500000
            holdingLine = line
            
        counter += 1

try: csv.close()
except: pass

t2 = time.time()

print(f'This process took {t2 - t1} seconds which is {(t2 - t1) / 60} minutes')
# 14 files; it took roughly 7 minutes
