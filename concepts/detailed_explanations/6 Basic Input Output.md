## 6.Basic Input/Output: Write a program that uses input() to ask the user for their name and then prints a personalised greeting


The input() function in python reads a line of text from standard input 
(typically from a keyboard) and returns it as a string (str). Any text provided 
within the parenthesis is displayed to the user as a prompt before input is collected.

The function itself does not perform syntactic validation of the user's input.
Consequently, it does not raise an error based on the content 
entered by the user. Errors may only occur if the returned string 
is subsequently used in an invalid operation (for example, attempting 
numerical computation without explicit type conversion).

In the given code, the value returned by input() is assigned to the
variable var_1 and interpolated into an f-string, which safely converts 
the value to its string representation during output.

 ------------------------------------------------------ Explanation of the quoted sentence

## "Error may occur if the the returned string is subsequently used in an invalid operation."

### What does returned string mean?

When a function executes, it may *return* a value back to the point where it was called.
In this case:

` var_1 = input("Enter something..") `
- `input()` returns a string
- That string is assigned to `var_1`

Hence, returned string means:
** The String produced by the `input()` function and handed back to the program.

### Why should errors occur later?

Because `input()` only collects text.
Errors occur not during input, but when the program later tries to use that string improperly.

Example:
```
x = input("Enter a number: ")
y = x + 5;  # Error
```
The error happens because:
- `x` is a string.
- `+5` is a numerical operation.
- This is an *invalid operation

## The function itself does not perform syntactic or semantic validation of the user's input

### What does this mean?
It means:
- `input()` does *not*
    - check whether the input is valid python code.
    - checks whether it makes logical or mathematical sense.
    - check whether it is appropriate for mathematicl use.

The function behaves passiely:
- It displays prompt.
- It reads text.
- It displays text as a string.

** All responsibility for correctness lies with the programmer**, not the `input()` function
Input function is not an aquisition function, not a validation function.
It does not think, not judge, not interpret.
It merely capture text.

 ------------------------------------------------------ Further questions for input()

### Is giving input value to the input function in python same as passing argument to the input function
    
No, giving a line of text from standard input value to the `input()` function is 
not the same as passing an argument to it.
** Passing an argument to `input()`** means providing a value inside the paranthesis
when you call the function. This value is used as a **prompt** displayed to the user, telling them what kind of data to enter.

Example:
```
name = input("Enter your name...")
# "Enter your name" is the argument/prompt.
```
the __argument__ is the message displayed to the user, while the **input value** is the data the user provides in response.

### When attempting to use a string as an index in programming

When attempting to use a string as an index in programming, errors occur because most programming languages expect an integer 
a whole number to specify the position of an item within a sequence (like a list or array). This is because data
structure are fundamentally zero-indexed, meaning their elements are located by their numerical offset from the start of the
structure.

##### Why this causes an error
- **Type Mismatch:** The interpreter or compiler sees a string such as ("apple") when it needs a number
(e.g., '0'). This is fundamental type mismatch that prevents the computer from knowing
which memory address to access.
- **Ambiguity:** An integer directly maps to a specific memory location. A string does not have an inherent, universal 
numerical value that corresponds to a position in a sequence.
