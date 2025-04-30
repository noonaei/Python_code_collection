import sys
from random import randint
def compare_to_random():
    if rando > x :
        print ('oh no! your number is smaller')
        #print(rando)
    elif rando< x :
        print ('oh no! your number is bigger')
        #print(rando)



rando= randint(0,10)
x= int(input('please enter a number: '))

while rando!= x:
    compare_to_random()
    pass
    x= int(input('please enter a number: '))

else:
    print ("you won!")
    print(rando)
