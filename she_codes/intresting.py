def abs():
    a= int(input("please enter a number:"))
    if a > -1:
        print("the absolute value is:%d" %a)
    if a < -1:
        print('the absolute value is: (%d*-1)' %a)

#for multiple values add ();"your initials are %s and your age is %d" %(initials, age)
#you can preform an action on the variable in the curly brakets!
#also, negative number*(-1)  will make it positive.



"""message = "all the numbers are equal " if (num2==num1==num3) else "any of the numbers are equal"
print(message)"""
# printing a simple message for one condition. doesn't work for elif| another if.




def addition_subtraction(a,b):
    return a+b, a-b
#you can return a few things at the same time.
"""sum,diff= calculation(4,2)"""
# assigning the two values to variables accordingly.
"""print (sum, diff)"""


def sum_plus_5(a,b):
#nested func,a and b dont have to be defined again because they already are in the outer func.
    def func2():
       return a+b
#calling the inner func in the outer func.
    sum= func2()+ 5
    print(func2())
    return sum


def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return -3
    res = addition(5)
    print(res)


#print(list(range(4,31,2)))
def even_numbers(start,stop):
#finds the even numbers in a given range
    list=[]
    if start%2==0:
        for i in range (start,stop,2):
            list.append (i)


    else:
        start+=1
        for i in range (start,stop,2):
            list.append (i)
    return list

if "__name__"== "__main__":
    list1 = ["100"," ","raven", "", "avatar", "", '400','totoro']
    res= list(filter(None,list1))
    #filters empty variables from the list.

    #creating  list and adding numbers input number
    input_nums=[]

    while len(input_nums) <10:
        num= int(input('enter a number: \n'))
        input_nums.append(num)


    list1 = [1,2,3,40,35,22,61,32,78]
    #for i in list1:
    #    if len(i) ==0:
    #        list1.remove(i)

    res = list(filter(lambda num: num %2 !=0 , list1))
    #returns a list with only the items for which the condition is True
    print(res)


    list1 = [5, 10, 15,['Emma','Vinnie','noga','sage',"arny"],20,[1,2,3,4,5], 25, 50, 20]
    names= ' - '.join(map(str,list1[5]))
#printsthe nested list as strings seperated by '-'. olny works when all the items are nested lists or none at all are.

def listproduct(list):
    product= 1

    for i in list:
        product*= i
    return product


def is_num_in_list(list):
    guess= int(input('random number: \n'))

    i=len(list)-1
    count=0
    while i>= 0:
        if guess ==list[i]:
            print ('yes, that number is in the list')
            count+= 1
            break
        i-=1

    if count== 0:
        print('the number is not on the list')


a=[53,18,34,1,2,3,4,5,6,7,8,9]
b=[3,2,6,17,17,6,2,3]
#checikng if a list is a palindrome. thought of it all on my own;)
def isitthat(list):
    f= 0
    while f<((len(list))/2)-1 :
        if list[f]==list[-f-1]:
            return True
            f+=1

        else:
            return False
            break



#count the frequency of letter and returns them in a dict
def letter_count(str):
    freq= {}

    for n in str:
         freq[n] = freq.get(n, 0) + 1
    return freq

#.get(key, value) key is the key you'd like to return the value from.
#value will be return if that ^ is none (nothing)
"""so here we have two cases: 1.the key doesnt exist in the dict, no value is returned,
 and then you return 0 as the default value and add 1.
2. the key does exist and you return its value and add 1"""
