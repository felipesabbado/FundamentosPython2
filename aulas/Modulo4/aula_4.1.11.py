"""4.1.11 SECTION QUIZ"""
"""Question 2: Write a lambda function, setting the least significant bit of its integer argument, and apply it to the map() function to produce the string 1 3 3 5 on the console."""

any_list = [1, 2, 3, 4]
even_list = list(map(lambda n: n | 1, any_list))
print(even_list)
