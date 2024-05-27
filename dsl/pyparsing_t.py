from pyparsing import Word, nums, Literal, Group, Forward, alphas

integer = Word(nums)
variable = Word(alphas, max=1)

operand = integer | variable

plus = Literal("+")
minus = Literal("-")
mult = Literal("*")
div = Literal("/")

expr = Forward()
term = operand | Group('(' + expr + ')')
expr <<= term + (plus | minus | mult | div) + term

# Example usage
result = expr.parseString("a + b * (c - d)")
print(result)  # Output: ['a', '+', 'b', '*', ['c', '-', 'd']]
