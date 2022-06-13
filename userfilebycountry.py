import csv

f1 = open('users.csv', encoding='utf-8')
f2 = open('Brunei Darussalam.csv','w',newline="") #remove blank line in between output
csv_rd = csv.reader(f1)
csv_wr = csv.writer(f2, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL) #use ',' as delimeter, '"' as quote and quote all items
for row in csv_rd:
    if ((row[6]).upper() == "Brunei Darussalam".upper()):
        csv_wr.writerow(row)

f1.close()
f2.close()