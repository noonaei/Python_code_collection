keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


numbers= dict()
#make sure to create the dictionary outside of the loop!!
#otherwise you'd get only the last key:value.

for i in range(len(keys)):
    numbers.update({keys[i]:values[i]})
#print (numbers)
#creating a dictionary from two lists.

res_dict =dict(zip(keys, values))
#print(res_dict)
#takes two lists and converts them into one list\dict\set

def Convert(list1,list2):
    res_dct = {list1[i]: list2[i] for i in range(0, len(list1))}
    return res_dct

#print(Convert(keys,keys))
#creating a dictionary from two lists. could work for the same list as well.
