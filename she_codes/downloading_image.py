from random import randint

file_name= str(randint(0,1000) )+ ".jpg"
print (file_name)
url= input("enter the photo's url: \n")

import urllib.request
urllib.request.urlretrieve (url,file_name)
# if i wanted to download an image or give it a name myself, ill have to write the url\file name in ""
#like so :
#urllib.request.urlretrieve ("https://i.pinimg.com/564x/48/a8/a8/48a8a8fad038f7a09c67eb344f251d14.jpg","dragon.jpg")
