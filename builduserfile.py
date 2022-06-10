import csv

f1 = open('test.csv')
f2 = open('malaysia2.csv','w',newline="") #remove blank line in between output
csv_rd = csv.reader(f1)
csv_wr = csv.writer(f2, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL) #use ',' as delimeter, '"' as quote and quote all items
for row in csv_rd:
    if ((row[6]) == "Malaysia"):
        csv_wr.writerow(row)

f1.close()
f2.close()