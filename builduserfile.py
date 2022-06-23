#extract users based on the country
import csv
import pandas as pd

with open('users.csv',newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

countries = ["AUSTRALIA","BAHRAIN","BANGLADESH","BRUNEI DARUSSALAM","CANADA","CHINA","DENMARK","FINLAND","FRANCE","GEORGIA","GERMANY","HONG KONG","HUNGARY","INDIA","INDONESIA","IRELAND","ITALY","JAPAN","KOREA REPUBLIC OF","KUWAIT","MALAYSIA","MALTA","MEXICO","NETHERLANDS","NEW ZEALAND","NORWAY","PAKISTAN","PHILIPPINES","POLAND","PORTUGAL","QATAR","SAUDI ARABIA","SINGAPORE","SOUTH AFRICA","SPAIN","SRI LANKA","SWEDEN","SWITZERLAND","TAIWAN","THAILAND","TURKEY","UNITED ARAB EMIRATES","UNITED KINGDOM","UNITED STATES"]
ctryname = []

for i in range(len(data)):
    for j in range(len(countries)):
        #print(countries[j])
        if ((data[i][6]).upper() == countries[j]):
            print(data[i])
            ctryname.append(data[i])

countrydf = pd.DataFrame(ctryname)
countrydf.to_csv('myusers.csv', index=False)
