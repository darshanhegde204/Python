#accept two values s and n . print square of first n number starting from s
s = int(input("Enter the number to start from: "))
n = int(input("Enter how many numbers to print: "))

for i in range (s,s+n):
    print(i**2)