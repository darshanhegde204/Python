#Remove duplicates from list
x=[1,4,8,0,9,4,7,3,1]
uni_x = []

for item in x:
    if item not in uni_x:
        uni_x.append(item)

print(uni_x)