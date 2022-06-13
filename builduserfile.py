import csv

f1 = open('users.csv', encoding='utf-8')
f2 = open('ctrylist.csv','w+',newline='') #remove blank line in between output
csv_rd = csv.reader(f1)
csv_wr = csv.writer(f2) #use ',' as delimeter, '"' as quote and quote all items
ctry = ""
hamnum = 0
ctrylist = []
hamnumlist = []
for row in csv_rd:
    if (row[6].upper() != ctry.upper()):
        ctrylist.append(row[6])
        hamnumlist.append(hamnum)
        ctry = row[6]
        hamnum = 0
        #print(row[6])
        #csv_wr.writerow(row)
    else:
        hamnum = hamnum + 1

csv_wr.writerow(ctrylist.split())
csv_wr.writerow(hamnumlist.split())

f1.close()
f2.close()