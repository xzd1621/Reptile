import csv

#写入csv
with open('data.csv','w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','Mike',20])
    writer.writerow(['10002','Bob',23])
    writer.writerow(['10003','Jack',22])
    writer.writerows([['10001','Mike',20],['10001','Mike',20],['10001','Mike',20]])

#以dict写入csv
with open('data1.csv','w') as csvfile:
    fieldnames=['id','name','age']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001','name':'Mike','age':20})

#读取
with open('data.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)