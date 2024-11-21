# Find a word!
word1 = input('Enter first word: ').strip().lower()
word2 = input('Enter second word: ').strip().lower()

i = 0
text = ''
for c in word2:
    if c == word1[i]:
        text += c
        i += 1

if text == word1:
    print('Yes')
else:
    print('No')
