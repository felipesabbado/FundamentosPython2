# 2.3 Section 3 – String Methods

# Demonstrating the capitalize() method:
# print('aBcD'.capitalize())
# print("Alpha".capitalize())
# print('ALPHA'.capitalize())
# print(' Alpha'.capitalize())
# print('123'.capitalize())
# print("αβγδ".capitalize())

# ----------------------------------------
# Demonstrating the center() method:
# print('[' + 'alpha'.center(10) + ']')
# print('[' + 'Beta'.center(2) + ']')
# print('[' + 'Beta'.center(4) + ']')
# print('[' + 'Beta'.center(6) + ']')
# print('[' + 'gamma'.center(20, '*') + ']')

# ----------------------------------------
# Demonstrating the endswith() method:
# if "epsilon".endswith("on"):
#     print("yes")
# else:
#     print("no")
#
# t = "zeta"
# print(t.endswith("a"))
# print(t.endswith("A"))
# print(t.endswith("et"))
# print(t.endswith("eta"))

# ----------------------------------------
## Demonstrating the find() method:
## it looks for a substring and returns the index of the first occurrence of this substring
# print("Eta".find("ta"))
# print("Eta".find("mma"))

# t = 'theta'
# print(t.find('eta'))
# print(t.find('et'))
# print(t.find('the'))
# print(t.find('ha'))

# # The second argument specifies the index at which the search will be started
# print('kappa'.find('a', 2))

# the_text = """A variation of the ordinary lorem ipsum
# text has been used in typesetting since the 1960s
# or earlier, when it was popularized by advertisements
# for Letraset transfer sheets. It was introduced to
# the Information Age in the mid-1980s by the Aldus Corporation,
# which employed it in graphics and word-processing templates
# for its desktop publishing program PageMaker (from Wikipedia)"""
#
# fnd = the_text.find('the')
# while fnd != -1:
#     print(fnd)
#     fnd = the_text.find('the', fnd + 1)

# # the third argument points to the first index which won't be taken into consideration during the search
# print('kappa'.find('a', 1, 4))
# print('kappa'.find('a', 2, 4))

# ----------------------------------------
## The isalnum() method checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.
# # Demonstrating the isalnum() method:
# print('lambda30'.isalnum())
# print('lambda'.isalnum())
# print('30'.isalnum())
# print('@'.isalnum())
# print('lambda_30'.isalnum())
# print(''.isalnum())

# ----------------------------------------
# # Example 1: Demonstrating the isapha() method: (letters only)
# print("Moooo".isalpha())
# print('Mu40'.isalpha())

# # Example 2: Demonstrating the isdigit() method: (digits only)
# print('2018'.isdigit())
# print("Year2019".isdigit())

# ----------------------------------------
# # islower() and isupper()
# print("Moooo".islower())
# print('moooo'.islower())
# print("Moooo".isupper())
# print("MOOOO".isupper())

# ----------------------------------------
# # Demonstrating the join() method:
# print(",".join(["omicron", "pi", "rho"]))
# str_lst = list('string')
# str_tpl = tuple('string')
# print(str_lst)
# print(str_tpl)
# print(''.join(str_lst))
# print('*'.join(str_tpl))
# print('*.*'.join(str_tpl))

# ----------------------------------------
# # Demonstrating the lstrip() method:
# print("[" + " tau ".lstrip() + "]")
# print("www.cisco.com".lstrip("w.")) # removes all characters enlisted in its argument (a string), not just whitespaces

# ----------------------------------------
# # Demonstrating the replace() method:
# print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
# print("This is it!".replace("is", "are")) # output: Thare are it
# print("Apple juice".replace("juice", ""))
# print("Apple juice".replace("", "*"))

# # the third argument (a number) limits the number of replacements.
# print("This is it!".replace("is", "are", 1))
# print("This is it!".replace("is", "are", 2))

# ----------------------------------------
