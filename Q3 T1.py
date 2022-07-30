from itertools import count


word = input("Enter the word: ")

count= 0 
for char in word:
    if char in 'aeiou':
        print(char)
        count += 1
print("Num of Vowels: " , count)