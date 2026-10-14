vowels = "aeiouAEIOU"
count = 0
with open('sample.txt', "r") as file:
    content = file.read()
    for char in content:
        if char in vowels:
            count += 1
    print(f"Total vowels in sample.txt: {count}")
