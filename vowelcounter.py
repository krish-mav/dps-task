# count the number of vowels in a string
def vowel_counter(word):
    vowels =  {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0

    for char in word:
        if char in vowels:
            count = count+1

    return count

print("Give a string:")
word = input()
vowel_count = vowel_counter(word)
print(f"The number of vowels in '{word}' are {vowel_count}")