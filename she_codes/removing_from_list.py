list1 = [5, 10, 15, 20, 25, 50, 20]

'''removing only the first value'''
spot= list1.index(20)
list1[spot]= 200
print(list1)

"""removing all values"""
def remove_value(list, val):
    return [i for i in list if i != val ]
#new_list= remove_value(list1, 20)
#print(new_list)

"""removing all values 2.0"""
while 20 in list1:
    list1.remove(20)
