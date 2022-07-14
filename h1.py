import csv
f=open('harshul.csv','w')
data=csv.writer(f)
row(['id','name','class'])
data.writerow(['90','harshul','sybca'])
data.writerow(['140','meet','tybca'])