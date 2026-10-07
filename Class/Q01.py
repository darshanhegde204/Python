text= "Welcome to IMCC!"
print(text.strip())
print(text.upper())
print(text.lower())
print(text.title())
print("Letter C occurs ", text.count("c"))
print(text.find("IMCC"))
print(text.replace("IMCC","Python Magic"))
print(text.startswith(" We"))
print(text.endswith("!"))
print(text.split())
words=[' python '," is ",' fun ']
print(text.join(words))
print(text*3)