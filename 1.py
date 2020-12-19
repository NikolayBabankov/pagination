import csv
from pprint import pprint



# with open('data-398-2018-08-30.csv','r',encoding='cp1251') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             pprint(row)

# with open('data-398-2018-08-30.csv', newline='', encoding='cp1251') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#          print(row['Name'], row['Street'])


results = []
with open('data-398-2018-08-30.csv', encoding='cp1251') as File:
    reader = csv.DictReader(File)
    for row in reader:
        tmp = {}
        tmp.setdefault('Name',row['Name'])
        tmp.setdefault('Street',row['Street'])
        tmp.setdefault('District',row['District'])
        results.append(tmp)
        break



print(results[0])