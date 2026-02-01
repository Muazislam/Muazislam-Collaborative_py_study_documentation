## 6.Basic Input/Output: Write a program that uses input() to ask the user for their name and then prints a personalised greeting

###################################### Attempts ######################################
var_1 = input('Enter a valid python expression...\n')
print(f"Hello {var_1}\nIt's nice to meet you!\nYou have a meeting today.")

############################## Explanation ##############################
# When attempting to use a string as an index in programming, errors occur because most 
# programming languages expect an integer (a whole number) to specify the position of an 
# item within a sequence (like a list or array) [1]. This is because data structures are 
# fundamentally zero-indexed, meaning their elements are located by their numerical offset 
# from the start of the structure.

 
############################## Why this causes errors ##############################

# - **Type Mismatch:** The interpreter or compiler sees a string (e.g., `"apple"`) when it 
# needs a number (e.g., `0`) [1]. This is a fundamental type mismatch that prevents the computer 
# from knowing which memory address to access.

# - **Ambiguity:** An integer directly maps to a specific memory location. A string does not have 
# an inherent, universal numerical value that corresponds to a position in a sequence.
