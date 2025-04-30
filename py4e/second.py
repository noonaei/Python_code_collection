smallest= None
count=0

for val in [13,209,67,35,88,3,13,78,194,123,345,45,678,23]:
    if smallest is None:
        smallest=val
        count=count+1
    elif val< smallest:
        smallest= val
        count=count+1
        print(smallest, val)
    else:
        print(smallest, val)
        count=count+1

print(smallest, "is the smallest number and the",count,"th on the list")
