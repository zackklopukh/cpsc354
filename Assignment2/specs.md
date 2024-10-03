# Specifications for Calculator Implementation
# (specs.md file created using GPT)

## Overview
This document outlines the specifications for the calculator implementation using Lark for parsing and evaluating arithmetic expressions. The calculator supports various mathematical operations, including addition, subtraction, multiplication, division, exponentiation, logarithmic calculations, and handling of negative numbers.

## Grammar Specification
The grammar for the calculator is defined in `grammar.lark`. The following rules are implemented:

- **Expressions**:
  - `sum`: Represents addition and subtraction.
  - `product`: Represents multiplication and division.
  - `atom`: Represents numbers, parentheses, and negative numbers.
  
- **Mathematical Functions**:
  - Support for logarithmic calculations with a specified base.

### Example Grammar
```lark
start: sum
?sum: product
    | sum "+" product   -> plus
    | sum "-" product   -> minus
?product: atom
    | product "*" atom  -> times
    | product "/" atom  -> divide
?atom: NUMBER           -> num
    | "-" atom          -> neg
    | "(" sum ")"
    | "log" atom "base" atom -> log
%import common.NUMBER
%import common.WS
%ignore WS
