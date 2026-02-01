## 2: Identify Types: Given a set of literals and operators (e.g., 'hello', +, 5, -88.8), identify which are operators and which are values.

## Attemp 1

items = {'hello', '+', 5, -88.8}

for item in items:
    if type(item) == str:
        if item == '+':
            print(f"{item} is an operator!")
        else:
            print(f"{item} is a string")
        
    elif type(item) == int or type(item) == float:
        print(f"{item} is a number")

## Attempt 2

items = ['hello', '+', 5, -88.8]

for item in items:
    if type(item) == str:
        if item == '+':
            print(f"{item} is an operator!")
        else:
            print(f"{item} is a string")
        
    elif type(item) == int or type(item) == float:
        print(f"{item} is a number")
