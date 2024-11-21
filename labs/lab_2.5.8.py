# Anagrams
text1 = list(input('Enter the first text: ').lower().replace(' ', ''))
text2 = list(input('Enter the second text: ').lower().replace(' ', ''))

isAnagram = 'Not anagrams'

size1 = len(text1)
size2 = len(text2)

if size1 == size2 and size1 > 2:
    for c in text1:
        if c in text2:
            text2.remove(c)
    if len(text2) == 0:
        isAnagram = 'Anagrams'

print(isAnagram)
