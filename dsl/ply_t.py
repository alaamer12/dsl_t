from ply import lex, yacc

# Lexer
tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN')

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()


# Parser
def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
    '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    else:
        p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor(p):
    '''
    factor : NUMBER
           | LPAREN expression RPAREN
    '''
    if isinstance(p[1], int):
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()

# Example usage
result = parser.parse("3 + 4 * (2 - 1)")
print(result)  # Output: 7
