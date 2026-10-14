with open("sample.txt", "r") as file:
    content = file.read()

words = content.split()

total_words = len(words)
print(f"Total number of words: {total_words}")

unique_words = list(set(words))
print(f"Unique words: {unique_words}")
print(f"Total unique words: {len(unique_words)}")