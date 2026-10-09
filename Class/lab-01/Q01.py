#print the tables of odd numbers (1-10)
for i in range(1,10,+2):  #outer loop i will be (1,3,5,7,9)
    for j in range(1,11): #inner loop j will be from 1-10
        sum=i*j #store the result
        print(f"{i} x {j} = {sum}") #prints in the table format
    print()