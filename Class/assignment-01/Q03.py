sentence = input("Enter a sentence: ")
words = sentence.split()

if not words:
    print("No words entered.")
else:
    print(f"Words list: {words}")
    longest_word = max(words, key=len)
    print(f"The longest word is: '{longest_word}' (Length: {len(longest_word)})")