import sys

# Zack Klopukh
# parentheses.py

def check_parentheses(expression: str) -> str:
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'no'
            stack.pop()
    return 'yes' if not stack else 'no'

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) < 2:
        print("Error: No input string provided.")
    else:
        print(check_parentheses(sys.argv[1]))
