"""4.1 Section 1 – Generators, iterators, and closures"""
"""
4.1.1 Generators - where to find them
    An iterator is an object of a class providing at least two methods (not counting the constructor):
        * __iter__() is invoked once when the iterator is created and returns the iterator's object itself;
        * __next__() is invoked to provide the next iteration's value and raises the StopIteration exception when the iteration comes to an end.

4.1.2 The yield statement
    The yield statement can be used only inside functions. The yield statement suspends function execution and causes the function to return the yield's argument as a result. Such a function cannot be invoked in a regular way – its only purpose is to be used as a generator (i.e. in a context that requires a series of values, like a for loop).

4.1.3 How to build a generator
    A conditional expression is an expression built using the if-else operator. For example:
"""
print(True if 0 >= 0 else False) # outputs True

"""
4.1.4 More about list comprehensions
    A list comprehension becomes a generator when used inside parentheses (used inside brackets, it produces a regular list). For example:
"""
for i in (el * 2 for el in range(5)):
    print(i, end='')
print() # outputs 02468

"""
4.1.5 The lambda function
A lambda function is a tool for creating anonymous functions. For example:
"""
def foo(x, f):
    return f(x)

print(foo(9, lambda x: x ** 0.5)) # outputs 3.0

"""
4.1.6 How to use lambdas and what for?
    The code has become shorter, clearer, and more legible.
"""
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

"""
4.1.7 Lambdas and the map() function
    The map(fun, list) function creates a copy of a list argument, and applies the fun function to all of its elements, returning a generator that provides the new list content element by element. For example:
"""
short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)
# outputs ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor'].

"""
4.1.8 Lambdas and the filter() function
    The filter(fun, list) function creates a copy of those list elements, which cause the fun function to return True. The function's result is a generator providing the new list content element by element. For example:
"""
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list) # outputs ['Python', 'Monty'].

"""
4.1.9 A brief look at closures
    A closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore. For example:
"""
def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(txt):
        return tg + txt + tg2
    return inner

b_tag = tag('<b>')
print(b_tag('Monty Python')) # outputs <b>Monty Python</b>
