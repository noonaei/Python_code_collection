
sum=0.0
count=0

while True:
    num= input("enter a number:")
    if num=="done":
        break
    try:
        num=float(num)
    except:
        print ("invalid input")
        continue
    sum += num
    count=count+1

print(sum,count, sum/count)
