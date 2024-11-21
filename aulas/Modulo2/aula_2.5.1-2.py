# 2.5 Section 5 – Four simple programs
# 2.5.1 The Caesar Cipher: encrypting a message
text = input("Enter your message: ").strip().upper()
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# 2.5.2 The Caesar Cipher: decrypting a message
#cipher = input('Enter your cryptogram: ').strip().upper()
text = ''
for char in cipher:
    if not char.isalpha():
        text += char
        continue
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
