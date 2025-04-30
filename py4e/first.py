print( "hey there! whats's your name?")
name= input("my name is: ")
print(f"great, {name}")

def numbers():
    global num1
    num1= int(input(" please enter a number: "))
    global num2
    num2= int(input("please enter a second number: "))
    global pre  # you have to declare a global variable before you give t a value.
    pre= (num1/num2)*100


while True:
    numbers()

    if num1==num2:
       print("come on " ,name, " you can be a bit more creative the that")
       continue

    if pre<=67:
       print (f"{pre},too small please try again.")
       continue

    else:
       print (pre," great choice!")
       break
