class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

class NumberNode(Node):
    def __init__(self, v):
        if('.' in v):
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value

class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == '+'):
            return self.v1.evaluate() + self.v2.evaluate()
        elif (self.op == '-'):
            return self.v1.evaluate() - self.v2.evaluate()
        elif (self.op == '*'):
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            return self.v1.evaluate() / self.v2.evaluate()

class PrintNode(Node):
    def __init__(self, v):
        self.value = v

    def execute(self):        
        self.value = self.value.evaluate()
        print(self.value)

class BlockNode(Node):
    def __init__(self, s):
        self.sl = [s]

    def execute(self):
        for statement in self.sl:
            statement.execute()

tokens = (
    'LBRACE', 'RBRACE',
    'PRINT','LPAREN', 'RPAREN', 'SEMI',
    'NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE'
    )

# Tokens
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_PRINT    = 'print'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMI  = r';'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'

def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_error(t):
    print("Syntax error at '%s'" % t.value)
    
# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE')
    )

def p_block(t):
    """
    block : LBRACE inblock RBRACE
    """
    t[0] = t[2]

def p_inblock(t):
    """
    inblock : smt inblock
    """
    t[0] = t[2]
    t[0].sl.insert(0,t[1])

def p_inblock2(t):
    """
    inblock : smt
    """
    t[0] = BlockNode(t[1])
    
def p_smt(t):
    """
    smt : print_smt
    """
    t[0] = t[1]

def p_print_smt(t):
    """
    print_smt : PRINT LPAREN expression RPAREN SEMI
    """
    t[0] = PrintNode(t[3])

def p_expression_binop(t):
    '''expression : expression PLUS factor
                  | expression MINUS factor
                  | expression TIMES factor
                  | expression DIVIDE factor'''
    t[0] = BopNode(t[2], t[1], t[3])

def p_expression_factor(t):
    '''expression : factor'''
    t[0] = t[1]

def p_factor_number(t):
    'factor : NUMBER'
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()

import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')
code = ""
for line in fd:
    code += line.strip()

#code = "{ print(1+2); print(2*3); }"

try:
    lex.input(code)
    while True:
        token = lex.token()
        if not token: break
        print(token)
    ast = yacc.parse(code)
    ast.execute()
except Exception:
    print("ERROR")

