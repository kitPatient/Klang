# Klang
Stack-Based Programming Language

# Usage

This Language requires [Python](https://www.python.org/) to use, so make sure it is installed and setup correctly.

Run the command ``` python klang.py Examples\test.klang ``` in the directory you downloaded it in, if it works successfully the number 20 should be displayed

# Language

Currently Supported types: 
- Int 
- Float 
- String

Current Keywords:
###### Operators:
- "+", Adds the top two items on the stack.
- "-", Negates the first item on the stack from the second most top.
- "*", Multiplys the top two items on the stack
- "/", Divides the top item on the stack from the second most top.
- "^", Raises the second most top item to the power of the top item.
###### Stack Manipulation
- ".", Takes the top item on the current stack and prints it. Also removes that item.
- "$", Removes the top item of the current stack.
- "close", Removes every item in the current stack.
- "swap", Swaps the top two items on the stack.
- "dup", Duplicates the top item on the current stack.
- "2dup", Duplicates the second most top item on the current stack.
- "s-n", Converts, if able, the top item of the string stack to a number.
- "n-s", Converts the top most item on the number stack to a string.
###### Stack Switching
- "-s", Changes the current stack to the string stack.
- "-n", Changes the current stack to the number stack.

#### Examples:
- ```1 2 + .``` prints the value 3
- ```4 3 - .``` prints the value 1
- ```2 3 ^ .``` prints the value 8
- ``` -s "Hello,World" . ``` prints `Hello,World`
- ```1 2 3 swap . close``` prints the value 2
- ```40 40 6 8 2dup - . close``` prints the value 2
