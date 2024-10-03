# Zack Klopukh
# Assignment 2 
# CPSC 354

from lark import Lark, Transformer
import math
import sys

# Load the grammar from grammar.lark
with open("grammar.lark", "r") as grammar_file:
    grammar = grammar_file.read()

# Create a Lark parser
parser = Lark(grammar, parser='lalr')

# Define an AST transformer
class CalcTransformer(Transformer):
    def plus(self, items):
        return ('plus', items[0], items[1])
    
    def minus(self, items):
        return ('minus', items[0], items[1])

    def times(self, items):
        return ('times', items[0], items[1])

    def divide(self, items):
        return ('divide', items[0], items[1])

    def power(self, items):
        return ('power', items[0], items[1])

    def neg(self, items):
        return ('neg', items[0])

    def log(self, items):
        return ('log', items[0], items[1]) 

    def num(self, items):
        return ('num', float(items[0]))

    def start(self, items):
        return items[0]

# Function to evaluate the AST
def evaluate(ast):
    if ast[0] == 'plus':
        return evaluate(ast[1]) + evaluate(ast[2])
    elif ast[0] == 'minus':
        return evaluate(ast[1]) - evaluate(ast[2])
    elif ast[0] == 'times':
        return evaluate(ast[1]) * evaluate(ast[2])
    elif ast[0] == 'divide':
        return evaluate(ast[1]) / evaluate(ast[2])
    elif ast[0] == 'power':
        return evaluate(ast[1]) ** evaluate(ast[2])
    elif ast[0] == 'neg':
        return -evaluate(ast[1])
    elif ast[0] == 'log':
        num_val = evaluate(ast[1])
        base_val = evaluate(ast[2])
        return math.log(num_val, base_val)
    elif ast[0] == 'num':
        return ast[1]
    else:
        raise ValueError("Unknown operation: {}".format(ast))

# Main execution
if __name__ == "__main__":
    calc_transformer = CalcTransformer() 
    input_string = sys.argv[1]
    tree = parser.parse(input_string)
    
    ast = calc_transformer.transform(tree)
    
    result = evaluate(ast)
    print(result)
