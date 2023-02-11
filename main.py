import csv
import sys


help_text = """
Parameters:
-dict = 'dict.csv' # default dict csv file path
-data = 'data.csv' # default data csv file path
-out = 'output.csv' # default output csv file path

Run script:
python3 main.py -dict dict.csv -data data.csv -out out.csv
"""


list_args = sys.argv
fileNameDict = 'dict.csv'.encode(encoding='utf-8')
fileNameData = 'data.csv'.encode(encoding='utf-8')
fileNameOut = 'output.csv'.encode(encoding='utf-8')

for i, arg in enumerate(sys.argv):
    if arg == '-help':
        print(help_text)
        exit()
    if arg == '-dict':
        fileNameDict = list_args[i+1].encode(encoding='utf-8')

    if arg == '-data':
        fileNameData = list_args[i+1].encode(encoding='utf-8')

    if arg == '-out':
        fileNameOut = list_args[i+1].encode(encoding='utf-8')

fileDict = open(fileNameDict)
fileData = open(fileNameData)
fileOutput = open(fileNameOut, 'w')

writer = csv.writer(fileOutput)

dict_list = csv.reader(fileDict)
dict = {key: val for key,val in dict_list}

data = csv.reader(fileData)
data = list(data)

for i, row in enumerate(data):
    for n, el in enumerate(row):
        # print(i , " ---> " , n)
        if el == "":
            continue
        
        if el in dict:
            # row[n] = f'{dict[el]}'
            doit = row[n] , " ---> " , dict[row[n]]
            doit = str(doit)
            doit.encode(encoding='utf-8')
            print(doit)
            row[n] = dict[row[n]]
            
            writer.writerow(row)

fileDict.close()
fileData.close()
fileOutput.close()