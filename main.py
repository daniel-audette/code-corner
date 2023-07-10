'''
This is bad code!
- Bad variable names
- print statements rather than log statements

The purpose of this file is to demonstrate VSCode functionality
'''

foo = 13
bar = 5

def add(a, b):
    print("We are about to add two numbers!")
    sum_value = a + b + b
    print("Hello!")
    print(f"We have added {a} + {b} and the result is {sum_value}")
    return sum_value

result = add(foo, bar)
