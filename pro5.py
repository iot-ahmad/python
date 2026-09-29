numbers = [15, 2, 45, 8, 99, 23]
max_num =numbers[0]
min_num = numbers[0]
for i in numbers:  
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
    
print("The largest number in the list is:", max_num)
print("The smallest number in the list is:", min_num)
