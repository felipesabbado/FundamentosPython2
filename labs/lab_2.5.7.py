# LAB Palindromes
text = input('Enter the text: ').lower().replace(' ', '')
reverse = text[::-1]
if text == reverse and len(reverse) > 1:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
print(reverse)
