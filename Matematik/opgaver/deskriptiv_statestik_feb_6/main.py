import csv
from gym_cas import *


file = open('sasExportD0PP.csv')
type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)
header

rows = []
for row in csvreader:
    row.pop(2)
    row.pop(0)
    row = list(map(float, row))
    rows.append(row)

flat_list = [item for sublist in rows for item in sublist]

sumOfArray = sum(flat_list)
middel = sumOfArray/len(flat_list)
print(len(flat_list))
print(middel)

# Omdanner maksimum- og minimumværdien til strings (tekst)
maxInt = str(max(flat_list))
minInt = str(min(flat_list))

middel = round(middel, 2)


varriation = max(flat_list) - min(flat_list)


print("maksimumværdi: " + maxInt + "%")
print("minimumværdi: " + minInt + "%")
print("middelværdi: " + str(middel) + "%")
print("variationsbredden: " + str(varriation) + "%-point")

#print(len(flat_list)/2)
#print(sorted(flat_list))


numbersHalf = len(flat_list) / 2

def checkDecimal(number):
    return number % 1 != 0


if checkDecimal(numbersHalf):
    #print("has decimal")
    decimalListProcess = len(flat_list) / 2
    decimalListProcess = round(decimalListProcess) + 1
    print(decimalListProcess)
else:
    #print("whole number")
    sortedList = sorted(flat_list)    

    #value = sortedList[((len(flat_list) / 2 - 1))] + sortedList[((len(flat_list) / 2))]
    #value = value / 2

    value1 = sorted(flat_list)
    value1Index = len(flat_list) / 2 - 1
    value1Index = int(value1Index)
    #print(value1[value1Index])

    value2 = sorted(flat_list)
    value2Index = len(flat_list) / 2
    value2Index = int(value2Index)
    #print(value2[value2Index])
    
    value = value1[value1Index] + value2[value2Index]
    value = value / 2
    print("median: " + str(value))

    if middel > value:
        print("skævhed: Højreskævt")
    elif middel < value:
        print("skævhed: Venstreskævt")

kvartil = flat_list

print(sorted(kvartil))
    

    


#boxplot(flat_list)