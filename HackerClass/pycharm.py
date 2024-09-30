my_string = "Hello, World! How are you?"
words = my_string.split()
print(words)
reversed_words = []
for word in words:
    reversed_words.insert(0, word)
result = ' '.join(reversed_words)
print(result)  # Output: "you? are How World! Hello,"