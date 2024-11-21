# LAB Improving the Caesar cipher
text = input("Enter your message: ").strip()
while True:
    try:
        shift = int(input('Enter a shift value [1..25]: '))
    except:
        print('Your input is invalid. Try again.')
    else:
        if 1 <= shift <= 25:
            break
        print('Please, enter a value between 1 and 25 only.')
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    code = ord(char) + shift
    if char.isupper() and code > ord('Z'):
        code = ord('A') + code - ord('Z') - 1
    if char.islower() and code > ord('z'):
        code = ord('a') + code - ord('z') - 1
    cipher += chr(code)

print(cipher)