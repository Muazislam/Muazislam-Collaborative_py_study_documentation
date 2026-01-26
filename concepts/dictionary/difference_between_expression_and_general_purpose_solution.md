### What is the difference between expression and general purpose solution?

## What is an Expression?
An _expression_ is:

A construct that evaluates a value.

##### Key Properties
- Produces a value
- Has no side effects
- Does not perform input/output
- Does not control program flow
- Is context independent

##### Example
```
42*60
(42*60)+42
len("Hello")
```

An __Expression__ answers:
"What is the value?"

## What is a general-purpose solution?

A general-purpose solution is:

A reusable procedure or program designed to handle _many possible inputs_, not a single fixed case.

##### Key Properties
- Accepts input (user, file, function parameters)
- Handles multiple scenarios
- Includes validation and conversion
- Operates at a higher abstraction level
- Often includes control flow and input/output

##### Examples
```
hour = int(input())
minutes = int(input())
seconds = int(input())
total = hours*3600+minutes*60+seconds
```

A general purpose solution answers:
"How do i solve this class of problem?"

## The core Difference

An expression computes a value.
A general purpose solution computes values for many cases.

Or more sharply:

| Aspect | Expression | General-purpose solution |
|--------|------------|--------------------------|
|Scope   | Single case | Many case               |
|Input   | Fixed values | Variable inputs        |
|I/O     | None         | Usually present        |
|Reusability | Not required | Required           |
|Question it answers | What is the value | "How do I handle all values?" |

## How to never mistake the distinction

Before writing code, ask one diagnostic question:

"Is the problem asking for a value or a mechanism?"

- If it asks for a value -> write an _expression_.
- If it asks for a mechanism -> write a _general purpose solution_.

##### Keyword Signals

| If the question says...                             | You should write |
|-----------------------------------------------------|------------------|
| "calculate", "compute", "evaluate"                  |  Expression      |
| "Write the program", "Ask the user", "Handle input" | General solution |

## Ending bonus
Expression belongs to mathematics.
General-purpose solutions belong to engneering.
