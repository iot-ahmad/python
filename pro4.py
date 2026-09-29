# Count the number of vowels in a string
text = "HEllo World"
vowel_count = 0
for i in text:
    if i.lower() in "aeiou":
        vowel_count += 1
        print(vowel_count)