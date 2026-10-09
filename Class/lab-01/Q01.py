#print the tables of odd numbers (1-10)
for i in range(1,10,+2):
    for j in range(1,11):
        sum=i*j
        print(f"{i} x {j} = {sum}")
    print()