from lark import Lark, Transformer

dsl_grammar = """
start: command+
command: "add" NUMBER
       | "subtract" NUMBER
%import common.NUMBER
%import common.WS
%ignore WS
"""

class Calculate(Transformer):
    def __init__(self):
        self.result = 0

    def command(self, args):
        operation, number = args
        number = int(number)
        if operation == 'add':
            self.result += number
        elif operation == 'subtract':
            self.result -= number

parser = Lark(dsl_grammar, parser='lalr', transformer=Calculate())
program = "add 5\nsubtract 3"
result = parser.parse(program)
print(result)  # Output: 2
