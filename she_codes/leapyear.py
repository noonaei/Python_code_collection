
year= int(input("the year: "))

if year%4 == 0:
    print("this year is a leap year")
elif year%400 ==0:
    print("this year is a leap year")
else :
    print ('this year is not a leap year')
