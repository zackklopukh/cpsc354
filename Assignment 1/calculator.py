import sys

# This will take the string input from the cmd and transalte it
# into an ordered stack of numbers and operations using a stack
# to implement a system to differentiate the paretheses properly
def stringToTokens(expression):
    tokens = []
    current_num = []
    for char in expression:
        if char.isdigit():
            current_num.append(char)
        else:
            if current_num:
                tokens.append(''.join(current_num))
                current_num = []
            if char in "+*^()":
                tokens.append(char)
    if current_num:
        tokens.append(''.join(current_num))
    return tokens

# Operation is order dependent
def precedence(op):
    if op == '^':
        return 3
    if op == '*':
        return 2
    if op == '+':
        return 1
    return 0

# Using the stak of values and operators complete
# a single math operator
def apply_operator(operators, values):
    op = operators.pop()
    right = values.pop()
    left = values.pop()
    if op == '+':
        values.append(left + right)
    elif op == '*':
        values.append(left * right)
    elif op == '^':
        values.append(left ** right)

# Complete error checking
def is_valid_expression(tokens):
    """Check if the tokenized expression is valid."""
    if not tokens:
        return False
    if tokens[-1] in "+*^":
        return False  # Expression cannot end with an operator
    if tokens[0] in "+*^":
        return False  # Expression cannot start with an operator
    open_paren_count = 0
    for i, token in enumerate(tokens):
        if token == '(':
            open_paren_count += 1
        elif token == ')':
            open_paren_count -= 1
            if open_paren_count < 0:
                return False  # More closing parentheses than opening
        elif token in "+*^" and (i == 0 or tokens[i-1] in "+*^("):
            return False  # Consecutive operators or operator after opening parenthesis
    return open_paren_count == 0

def calculate(expression):
    tokens = stringToTokens(expression)
    
    if not is_valid_expression(tokens):
        return "Error: Invalid expression"

    operators = []
    values = []
    
    for token in tokens:
        if token.isdigit():
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
        else:
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(token)):
                apply_operator(operators, values)
            operators.append(token)
    
    while operators:
        apply_operator(operators, values)
    
    return values[0]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input string provided.")
    else:
        print(calculate(sys.argv[1]))
