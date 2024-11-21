# 2.2 Section 2 – The nature of strings in Python

# char_1 = 'a'
# char_2 = ' ' # space
#
# print(ord(char_1))
# print(ord(char_2))

# ----------------------------------------
# space = 32
# a = 97
# print(chr(a - space)) # A
# print(chr(945))

# ----------------------------------------
# chr(ord(character)) == character
# ord(chr(codepoint)) == codepoint

# ----------------------------------------
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# del alphabet

# ----------------------------------------
# # Demonstrating min() and max() - Example 1:
# print(min("aAbByYzZ")) # output: A
# print(max("aAbByYzZ")) # output: z
#
# # Demonstrating min() and max() - Examples 2 & 3:
# t = 'The Knights Who Say "Ni!"'
# print('[' + min(t) + ']') # output: [ ]
# print('[' + max(t) + ']') # output: [y]
#
# t = [0, 1, 2]
# print(min(t)) # output: 0
# print(max(t)) # output: 2

# ----------------------------------------
# print(tuple('string'))
# print(list('string'))

# ----------------------------------------
# # Demonstrating the index() method:
# print("aAbByYzZaA".index("b")) # output: 2
# print("aAbByYzZaA".index("Z")) # output: 7
# print("aAbByYzZaA".index("A")) # output: 1

# ----------------------------------------
# Demonstrating the count() method:
print("abcabc".count("b")) # output: 2
print('abcabc'.count("d")) # output: 0
