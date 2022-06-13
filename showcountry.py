import csv

f1 = open('countrylist.csv', encoding='utf-8')
f2 = open('countryname.csv','w',newline="") #remove blank line in between output
csv_rd = csv.reader(f1)
csv_wr = csv.writer(f2) #use ',' as delimeter, '"' as quote and quote all items

ctryname = []
ctry = ""
for row in csv_rd:
    if ((row[6]).upper() != ctry.upper()):
        if (ctry not in ctryname):
            ctryname.append(ctry)
        #print(row)
        ctry = row[6]
        
csv_wr.writerow(ctryname)
print(ctryname)

f1.close()
f2.close()