#Accept the name and cheak if its palindrome
name = input("Enter your name: ")
res=""
for i in range (len(name)-1,-1,-1):
    res+=name[i]
if name==res:
    print("Its palindrome")
else:
    print("Its not palindrome")