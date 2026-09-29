# Find the longest word in a sentence
sentence = "Python is an amazing language"
longest_word = ""
max_length = 0
sentence = sentence.split()

for i in sentence:
    if len(i)>max_length:
        max_length = len(i)
        longest_word = i

print(longest_word)