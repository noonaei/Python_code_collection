
#question 1
#a1= int(input("enter the first number:"))
#an= int(input("enter the desired n: "))
#q= float(input("enter the sequence's multiplier:"))

#an=a1*q**(an-1)
#print(an)

#question 2


while True:
    some_number = input("please enter a number:")
    try:
        some_number=float(some_number)
        break
    except:
        print("invalid input")
        continue

for i in [1,2,3,4]:
    if some_number% i ==0:
        print("true")
        break
    else:
        print("false")
