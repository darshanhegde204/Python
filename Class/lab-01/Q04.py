#Print the sum of digits
digit=list(map(int,input("Enter the digits: ").split()))
sum=0
for i in digit:
    if i<0:
        continue
    else:
        sum+=i
print(sum)