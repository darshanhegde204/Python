#create a list of 10 element and print the sum of last 4 element
#remove the item from the list located at 2 and 5 pos
#print the diff of largest and smallest number
#app a new element to the list which is half of the item of third position in a list

x=[1,2,10,4,5,6,7,8,9,10]
sum=sum(x[-4:])
print(sum)

del x[1]
del x[4]
print(x)

print(max(x)-min(x))

haf = x[2] // 2 
x.append(haf)    
print(x)