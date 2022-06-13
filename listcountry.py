#read from users.csv
#store the country name and compare with the next line. 
#if its not same, write to countrlist.csv
import csv

f1 = open('users.csv', encoding='utf-8')
f2 = open('countrylist.csv','w',newline="") #remove blank line in between output
csv_rd = csv.reader(f1)
csv_wr = csv.writer(f2) #use ',' as delimeter, '"' as quote and quote all items

ctry = ""
for row in csv_rd:
    if ((row[6]).upper() != ctry.upper()):
        print(row)
        ctry = row[6]
        csv_wr.writerow(row)

f1.close()
f2.close()