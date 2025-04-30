movies=["the notebook", "maleficent","batman vs superman","black swan", 'gone girl',
"war of the worlds", "just married"]

actor =["rachel mcadams", "angelina julie", "gal gadot","natalie portman",
 "rosamund pike", "dakota fanning", "brittany murphy"]

#making a new list and appending a string with the items of each list
res_lst = [f"{movies} is played by {actor}" for (movies,actor) in zip(movies, actor)]
#making a dict with each pair as a key :value
res_dct = {movies[i]: actor[i] for i in range(0, len(movies))}
#same list as line8 just using the res_dict
lst2= [f"{m} is played by {a}" for (m,a) in res_dct.items()]


# more then one condition with for loop
lst= [x*100 if x%2==0 else x for x in range(1,10) ]
print (lst)
lst2= [ "BOOM" if x%7==0 else x for x in range(1,100)]
print (lst2)
