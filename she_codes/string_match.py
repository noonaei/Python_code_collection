def string_match(a, b):
    counter=0
    shorter= min(len(a), len(b))

    for i in range(shorter-1):
        a_sub =a[i:i+2]
        b_sub =b[i:i+2]
        if a_sub == b_sub:
            counter+=1
    return counter

def same(list):
    new_list=[]
    for word in list:
        if word[0]== word[-1]:
            new_list.append(word)
    return new_list


word_list=['ana','john','mom','mary','way wayw','bbb']


print(same(word_list))
