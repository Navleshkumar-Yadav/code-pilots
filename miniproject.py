from datetime import date, datetime
import datetime
year1 = int(input("Enter starting year : "))
month1 = int(input("Enter starting month : "))
date1 = int(input("Enter starting date : "))
d = date(year1,month1,date1)
year2 = int(input("Enter Ending year : "))
month2 = int(input("Enter Ending month: "))
date2= int(input("Enter Ending date: "))
b=date(year2,month2,date2)
L1=[]
L2=[]
print("Range: ")
print(d, "To" ,b)
for year in range(year1,year2):
    if(year%400==0)and(year%100==0):
      L1=L1+[year,]
    elif(year%4==0)and(year%100!=0):
      L1=L1+[year ,]
    else:
        L2=L2+[year ,]
print("list of leap year: ")
print(L1)
print("list of non leap year: ",)
print(L2)

