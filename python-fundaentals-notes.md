# Python Fundamentals Study Notes

## 1. Identifying Data Types and Values

### Common Python Data Types
- **int**: Integer numbers (e.g., 5, -10, 42)
- **float**: Decimal numbers (e.g., -88.8, 42.0, 3.14)
- **bool**: Boolean values (True, False)
- **str**: String/text data (e.g., 'Hello', '11 Cats')
- **tuple**: Ordered, immutable collection (e.g., (1, 2, 3))
- **list**: Ordered, mutable collection (e.g., [1, 2, 3])
- **dict**: Key-value pairs (e.g., {'name': 'John', 'age': 25})

### Key Points
- `42` is an integer because it has no decimal point
- `42.0` is a float because it has a decimal point
- `+` is an operator, not a data type

## 2. Type Conversion and Expressions

### str(0)
```python
result = str(0)
print(result)        # Output: '0'
print(type(result))  # Output: <class 'str'>
```
**Explanation**: The `str()` function converts the integer `0` to the string `'0'`. Note that `0` ≠ `'0'` - they are different data types.

### int('42')
```python
result = int('42')
print(result)        # Output: 42
print(type(result))  # Output: <class 'int'>
```
**Explanation**: The `int()` function converts the string `'42'` to the integer `42` (base 10).

#### Base Conversion Example
```python
x = int('42', base=16)  # Convert hexadecimal '42' to decimal
print(x)  # Output: 66 (4*16 + 2 = 66)
```

### float(10)
```python
result = float(10)
print(result)  # Output: 10.0
```
**Explanation**: The `float()` function converts the integer `10` to the floating-point number `10.0`.

#### Scientific Notation
```python
x = float('1.23e2')  # Scientific notation
print(x)  # Output: 123.0
```

### int(1.99)
```python
result = int(1.99)
print(result)  # Output: 1
```
**Explanation**: The `int()` function **truncates** the decimal part (doesn't round). It simply removes everything after the decimal point.

### String Concatenation Error
```python
# This will cause a TypeError:
# text = 'I have eaten ' + 99 + ' burritos.'

# Correct way:
text = 'I have eaten ' + str(99) + ' burritos.'
print(text)  # Output: I have eaten 99 burritos.
```
**Error Reason**: Python cannot concatenate strings with integers directly. You must convert the integer to a string first.

### String Concatenation
```python
text = 'spam' + 'spamspam'
print(text)  # Output: spamspamspam
```

### String Repetition
```python
text = 'spam' * 5
print(text)  # Output: spamspamspamspamspam
```
**Explanation**: The `*` operator repeats a string the specified number of times.

### Input Function and Type Conversion
```python
spam = input("Enter a number: ")  # User enters: 101
print(spam)        # Output: 101
print(type(spam))  # Output: <class 'str'>

# To use in mathematical calculations:
number = int(spam)
result = number + 3
print(result)  # Output: 104
```
**Key Point**: The `input()` function **always** returns a string, regardless of what the user enters.

## 3. Boolean Values and Operators

### Boolean Data Type
The Boolean data type has only two values: `True` and `False` (note the capitalization).

```python
is_sunny = True
is_raining = False
```

### Boolean Operators

#### AND Operator
Returns `True` only if **both** operands are `True`.

```python
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False
```

#### OR Operator  
Returns `True` if **at least one** operand is `True`.

```python
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
```

#### NOT Operator
Returns the **opposite** of the operand.

```python
print(not True)   # False
print(not False)  # True
```

### Boolean Expression Evaluation

```python
# (5 > 4) and (3 == 5)
print((5 > 4) and (3 == 5))  # True and False = False

# not (5 > 4)
print(not(5 > 4))  # not True = False

# (5 > 4) or (3 == 5)
print((5 > 4) or (3 == 5))  # True or False = True

# not ((5 > 4) or (3 == 5))
print(not((5 > 4) or (3 == 5)))  # not True = False

# (True and True) and (True == False)
print((True and True) and (True == False))  # True and False = False

# (not False) or (not True)
print((not False) or (not True))  # True or False = True
```

### Why 42 == '42' is False
```python
print(42 == '42')  # False
print(type(42))    # <class 'int'>
print(type('42'))  # <class 'str'>
```
**Explanation**: Python compares both **value** and **type**. Since `42` is an integer and `'42'` is a string, they are considered different, even though they represent the same numeric value.

## 4. Variables, Assignment, and Memory

### Variable Assignment and Expressions

#### Snippet A
```python
spam = 20
spam + 1  # This doesn't change spam!
print(spam)  # Output: 20
```
**Important**: The expression `spam + 1` evaluates to `21`, but it doesn't modify the variable `spam`. To actually change `spam`, you need: `spam = spam + 1` or `spam += 1`.

#### Snippet B - Multiple Assignment
```python
x = 2
y = 3
x, y = y, x  # Swap values
print(x)  # Output: 3
print(y)  # Output: 2
```
**How it works**: Python evaluates all expressions on the right side first, then assigns them to the left side simultaneously. This allows for elegant value swapping.

### Object References and Memory

#### Snippet C - List References
```python
my_list = [1, 2, 3]
another_list = my_list  # Both variables reference the same list object
my_list.append(4)
print(my_list)      # Output: [1, 2, 3, 4]
print(another_list) # Output: [1, 2, 3, 4]
```

**Key Concepts**:
- Variables store **references** to objects, not the objects themselves
- When you assign `another_list = my_list`, both variables point to the same list object in memory
- Changes to the list through either variable affect the same object

### Creating Independent Copies

#### Shallow Copy
```python
import copy

my_list = [1, 2, 3]
another_list = copy.copy(my_list)  # or my_list.copy()
my_list.append(4)

print(my_list)      # Output: [1, 2, 3, 4]
print(another_list) # Output: [1, 2, 3]
```

#### Deep Copy (for nested objects)
```python
import copy

my_list = [[1, 2], [3, 4]]
another_list = copy.deepcopy(my_list)
my_list[0].append(3)

print(my_list)      # Output: [[1, 2, 3], [3, 4]]
print(another_list) # Output: [[1, 2], [3, 4]]
```

**Difference**:
- **Shallow copy**: Creates a new list, but nested objects are still referenced
- **Deep copy**: Creates completely independent copies of all nested objects

## Summary

Understanding these fundamental concepts is crucial for Python programming:

1. **Data types** determine what operations can be performed on values
2. **Type conversion** allows you to change between compatible data types
3. **Boolean logic** forms the foundation of conditional statements
4. **Variable assignment** creates references to objects in memory
5. **Object references** explain why some assignments create copies while others create aliases

These concepts form the building blocks for more advanced Python programming concepts.
