def stars():
    n=int(input('how many lines would you like to print?'))
    counter=0
    while counter< n:
        print ('*'*(counter+1), end="\n")
        counter+=1 # regular triangle

def stars2(s,l):
    counter=0
    last_line=s
    while counter<=l:

        print('*'*last_line)
        last_line+=1
        counter+=1

def diamond(n):
    for r in range(n):
        # decreasing pattern of spaces, increasing stars, increasing stars
        for s in range(r,n):
            print(" ", end=" ")
        for l in range(r+1):
            print("*", end=" ")
        for w in range(r):
            print("*", end=" ")
        print()

    for i in range(n):
        # increasing pattern of spaces, decreasing stars, decreasing stars
        for l in range(i+1):
            print(" ", end=" ")
        for s in range(i,n):
            print("*", end=" ")
        for k in range(i,n-1):
            print("*", end=" ")
        print()
#^ ^ a dumber way to make a diamond
