# This 'specs.md' File was created using ChatGPT

specs_content = """
# Assignment 1 - Specifications

## File: `parentheses.py`

### Function: `check_parentheses(expression: str) -> str`

- **Purpose**: This function checks if a given string contains balanced parentheses.
  
- **Input**: 
  - A string `expression` containing any characters but focusing on the parentheses `(` and `)`.
  
- **Output**: 
  - Returns `"yes"` if the parentheses are balanced, otherwise returns `"no"`.
  
- **Logic**:
  - Iterates over the input string.
  - Uses a stack to track opening parentheses.
  - For every closing parenthesis `)`, it checks if there is a corresponding opening parenthesis `(`. If not, the expression is unbalanced.
  - After processing the string, the stack should be empty if all parentheses are properly balanced.
  
- **Error Handling**: 
  - If no command-line arguments are provided, the script prints `"Error: No input string provided."`.

---

## File: `calculator.py`

### Function: `stringToTokens(expression: str) -> list[str]`

- **Purpose**: Tokenizes an arithmetic expression into a list of numbers, operators, and parentheses.
  
- **Input**:
  - A string `expression` representing the arithmetic expression.
  
- **Output**:
  - Returns a list of tokens, where each token is either a number, operator (`+`, `*`, `^`), or a parenthesis (`(`, `)`).
  
- **Logic**:
  - Iterates over the characters in the expression.
  - Groups consecutive digits together to form multi-digit numbers.
  - Separates operators and parentheses as individual tokens.
  
---

### Function: `precedence(op: str) -> int`

- **Purpose**: Returns the precedence level of the given operator.
  
- **Input**:
  - A string `op`, which is one of the operators: `+`, `*`, or `^`.
  
- **Output**:
  - An integer representing the operator's precedence, where:
    - `^` has the highest precedence (3),
    - `*` has medium precedence (2),
    - `+` has the lowest precedence (1).
  
---

### Function: `apply_operator(operators: list[str], values: list[int]) -> None`

- **Purpose**: Applies the last operator from the `operators` stack to the last two numbers from the `values` stack.
  
- **Input**:
  - A list `operators` containing the operators `+`, `*`, and `^`.
  - A list `values` containing the current numbers being evaluated.
  
- **Logic**:
  - Pops the operator from the `operators` stack and applies it to the last two values on the `values` stack.
  - The result is pushed back onto the `values` stack.

---

### Function: `is_valid_expression(tokens: list[str]) -> bool`

- **Purpose**: Validates the tokenized arithmetic expression to check if it is properly formatted.
  
- **Input**:
  - A list `tokens` representing the tokenized arithmetic expression.
  
- **Output**:
  - Returns `True` if the expression is valid and `False` otherwise.
  
- **Logic**:
  - Ensures the expression does not start or end with an operator.
  - Checks for consecutive operators or improper placement of operators.
  - Ensures parentheses are balanced by counting opening and closing parentheses.

---

### Function: `calculate(expression: str) -> Union[int, str]`

- **Purpose**: Evaluates a valid arithmetic expression using the operators `+`, `*`, and `^`, and handles parentheses.
  
- **Input**:
  - A string `expression` representing the arithmetic expression.
  
- **Output**:
  - Returns the result of the evaluated expression as an integer if the expression is valid.
  - Returns `"Error: Malformed expression"` if the input string is not a valid arithmetic expression.
  
- **Logic**:
  - Tokenizes the expression using `stringToTokens`.
  - Validates the tokenized expression with `is_valid_expression`.
  - Uses two stacks:
    - `operators` to store operators and parentheses,
    - `values` to store numbers.
  - Operators are applied according to their precedence, and parentheses are handled appropriately.
  - If the expression is invalid, it returns an error message.

- **Error Handling**:
  - If no command-line argument is provided, it prints `"Error: No input string provided."`.
  - If the expression is malformed (e.g., contains consecutive operators or mismatched parentheses), it returns `"Error: Invalid expression"`.

# Save the specs.md file
file_path = '/mnt/data/specs.md'
with open(file_path, 'w') as f:
    f.write(specs_content)

file_path
