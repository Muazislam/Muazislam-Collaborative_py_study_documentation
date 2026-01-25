
The `input()` function reads the line of text from standard input and returns it as a string. The prompt `Please enter a phrase ...` is displayed to the user before input is collected.

The returned string is assigned to the variable `phrase`. The built-in `len()` function is then called with `phrase` as it's argument. `len()` computes the number of items contained in the object passed to it. In the case of a string, this corresponds to the number of characters.

Finally, the `print()` function outputs the computed length. Since input always returns a string, the length calculation counts characters regardless of whether the input contains letters, digits or special symbols.

##### Question: If embedding a variable into a string is called interpolation, what do we call passing a variable into len()?

It is called _argument passing(or function invocation with an argument)_

- interpolation is a -string formating concept_
      It applies only to strings.
- `len()` is a function call
      You are supplying an _argument_ to a function parameter.

Terminology:

- `f"{phrase}"` -> string interpolation.
- `len(phrase)` -> passing an argument to a function.

##### Question: What does item mean in len()?
An item is a single element contained within a data structure, as defined by that structure's iteration rules.

| object type | What len() counts   |
| `str`       | Uni code character  |
| `list`      | Elements            |
| `tuple`     | Elements            |
| `sets`      | Unique elements     |
| `Dict`      | Keys                |
| `Bytes`     | Bytes               |
| `range`     | No.s in the sequence|

So:
```
len("A1@")  # 3characters
len([10,20]) # 2 elements
len({"a":1}) # 1 key
```
##### Since the input is provided by the user, does it become the argument?

Yes, it becomes argument.

###### Formal explanation
- `input()` returns a string.
-  That returned string is stored in `phrase`.
-  When you write `len(phrase)`, `phrase` __is the argument__.

The source of the value (user, file, network) is irrelevant.
What matters is how it is passed to the function.

##### Question: How can len() accept so many types?

`len()` works on _objects that implement length protocol (internally __len__() ).

###### Example:
```
# string
len("Hello")     # 5 characters

# Bytes
len(b"ABC")      # 3

# Tuple
len((1,2,3))     # 3

# List
len([10, 20, 30, 40])        # 4

# Range
len(range(5, 15))            # 10

# Dictionary (counts keys)
len({"a": 1, "b": 2})        # 2

# Set
len({1,2,3})    # 3

# Frozen set
len(frozenset([1,2])         # 2
```

##### len() Overflow -- What does it mean?

`len()` raises an overflow on lengths larger than sys.maxsize.

```
len(range(2**10))    # overflow
```

Why?
- `range` stores start, stop, step efficiently.
- `len()` must return an integer.
- Python integers are unbounded, but _C-level APIs are not_.
- Length must fit in `sys.maxsizer`
