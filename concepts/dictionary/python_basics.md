### 1: Conform
comply with rules, standards, or laws.

---------------------------

### 2: Passively

In coding and computer science,
passive (or acting "passively") generally refers to components, 
data structures, or systems that do not take initiative, consume 
resources without generating them, or wait to be acted upon by another 
part of the system (the "active" part). 

---------------------------

### 3: Data Aquisition function

In coding and software engineering, a data acquisition (DAQ) function refers 
to a programmatic routine, library method, or API call designed to collect, 
sample, and convert physical, analog, or real-world signals into digital data 
that a computer can store, analyze, or process.

---------------------------

### 4: Validation or Evaluation function

In coding, validation and evaluation functions are routines designed to ensure 
data integrity, verify user input, or assess the performance of an algorithm or 
model. They act as "gatekeepers" or "judges" within the code, often returning a 
boolean (true/false) or a numerical score to guide program flow.

---------------------------


### 5: Standard Input

Standard input (often abreviated as stdin) is the default data stream from which the
program reads input during execution.
In most interactive programs, standard input corresponds to keyboard input provided by the user.
In python, the input() function reads data from standard input and returns it to the program.

---------------------------

### 6: Syntactic or semantic validation

This refers to two forms of correctness checking:

Syntactic validation: Verification that conforms to the formal structure or 
grammar of a language(i.e. correct arrangment of symbols).
Example: whether 3+*5 follows Python grammar -- it does not.

Semantic validation: Verification that input is meaningful and logically valid 
within a given context.
Example: dividing by zero or using a string where a number is required.

When we say a function does **not perform syntactic or semantic validation**, 
it means it **does not analyze correctness, meaning, or suitability** of the input.

---------------------------


### 7: Invalid Operation

An invalid operation is an action applied to data that voilates the rules of the
programming language or it's type system.

Example: 
- Adding a number to a string("5" + 3)
- Dividing a number by zero (10/0)
- Using a string as an index where an integer is required.
Such operations result in runtime errors, not in input errors.

---------------------------

### 8: Numerical Computation

Numerical computation refers to mathematical operations performed on numeric data
types such as int, float or decimal.

Examples:
- Addition, subtraction, multiplication
- Division, exponentiation
- Statistical or scientific calculations

Strings cannot participate in numerical computation unless converted into numeric types.

---------------------------

### 9: Explicit type conversion

It is the delibrate transformation of a value from one data type to another using 
a conversion function.

Examples:
int("5") --> Convert string to integer.
float("3.14") -->Converts string to floating point number.

The word explicit means the programmer must intentionally request the conversion;
python will not guess.

---------------------------

### 10: Interpolated

Interpolation is the process of embeding variable values inside a string.
In python, it is most commonly done using f-string.
f"Hello {var_1}"
Here. the value of the name is evaluated and inserted into the string at runtime.
