# Remove digits from a string and reverse it
new_word="python2026code"
clean_word=""
for i in new_word:
    if i not in "0123456789":
        clean_word+=i
new_word=clean_word[::-1]
print(new_word)