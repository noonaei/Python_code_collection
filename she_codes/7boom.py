# the computer on its own
def seven_boom(x):
    for i in range(x,21):
        if i % 7==0:
            print ("Boom")
            break
        else:
            print (i)
            break

#checks if the input is "boom"
def check_not_boom(input):
    if input != "boom":
        return True
    else:
        return False

#user plays on his own
def next_number(z):
    for num in range (z,21):
        guess= input("what's the next number? ")
        if num % 7==0 and check_not_boom(guess):
            print ("you're worng")
            return False
            break

        elif num % 7==0 and not check_not_boom(guess) or guess.isdigit() and int(guess) == num:
            break

        else:
            if guess.isdigit() and int(guess) != num:
                print ("you're worng, try again")
                return False
                break
            if  not guess.isdigit()  and check_not_boom(guess):
                print ("invalid input")
                continue
#supposed to be a full functioning game,with alternating turns
def game():
    is_comp=0
    current_num= 1
    while is_comp< 21:
        if is_comp%2 != 0:
            seven_boom(current_num)

        else:
            next_number(current_num)

        is_comp+=1
        current_num+=1

game()
