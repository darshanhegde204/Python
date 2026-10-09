#Create a heterogenous list of numbers and names. Split the list from higest number
my_list = [10, "Darshan", 5, "Rahul", 25, "Amit", 15]

highest = max(x for x in my_list if isinstance(x, int))
index = my_list.index(highest)

left = my_list[:index]
right = my_list[index :]

print("Left list:", left)
print("Right list:", right)