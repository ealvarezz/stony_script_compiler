# Edwin Alvarez 109448839
# First I will define the classes that my parser is going to use
class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

class RootNode(Node):       # This is the root note that will perform the
    def __init__(self, v):  # evalaluation from the top down once the tree
        self.v = v      # the tree if finally constructed

    def execute(self):
        val = self.v.evaluate()

        if isinstance(val, str):
            print('\'' + val + '\'')
        else:
            print(val)


class NumberNode(Node):
    def __init__(self, v):
        if('.' in v):
            self.v = float(v)
        else:
            self.v = int(v)

    def evaluate(self):
        return self.v


class StringNode(Node):
    def __init__(self, v):
        self.v = v

    def evaluate(self):
        return self.v


class BooleanNode(Node):
    def __init__(self, v):
        if v == 'True':
            self.v = True
        else:
            self.v = False

    def evaluate(self):
        return self.v


class BinopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        try:
            if (self.op == '%'):
                return self.v1.evaluate() % self.v2.evaluate()
            elif (self.op == '-'):
                return self.v1.evaluate() - self.v2.evaluate()
            elif (self.op == '*'):
                return self.v1.evaluate() * self.v2.evaluate()
            elif (self.op == '/'):
                return self.v1.evaluate() / self.v2.evaluate()
            elif (self.op == '**'):
                return self.v1.evaluate() ** self.v2.evaluate()
            elif (self.op == '//'):
                return self.v1.evaluate() // self.v2.evaluate()
            if (self.op == '+'):
                return self.v1.evaluate() + self.v2.evaluate()
        except:
            print("SEMANTIC ERROR")
            raise Exception

"""
class ConcatNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == '+'):
            return self.v1.evaluate() + self.v2.evaluate()
"""

class BoolopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        try:
            if (self.op == 'and'):
                return self.v1.evaluate() and self.v2.evaluate()
            elif (self.op == 'or'):
                return self.v1.evaluate() or self.v2.evaluate()
            elif (self.op == '>'):
                return self.v1.evaluate() > self.v2.evaluate()
            elif (self.op == '<'):
                return self.v1.evaluate() < self.v2.evaluate()
            elif (self.op == '>='):
                return self.v1.evaluate() >= self.v2.evaluate()
            elif (self.op == '<='):
                return self.v1.evaluate() <= self.v2.evaluate()
            elif (self.op == '=='):
                return self.v1.evaluate() == self.v2.evaluate()
            elif (self.op == '<>'):
                return self.v1.evaluate() != self.v2.evaluate()

        except:
            print('SEMANTIC ERROR')
            raise Exception



class NotNode(Node):
    def __init__(self, v):
        self.v = v

    def evaluate(self):
        try:
            return not self.v.evaluate()
        except:
            print('SEMANTIC ERROR')
            raise Exception


class ListNode(Node):
    def __init__(self, l):
        self.l = [l]

    def evaluate(self):
        try:
            #print('did you even try?')
            new_l = []
            for i in self.l:
                new_l.append(i.evaluate())
            #print('ahhhhhhhhhhhhhhhhh')
            return new_l
        except:
            print('SEMANTIC ERROR')
            raise Exception


class ListIndex(Node):
    def __init__(self, l, index):
        self.l = l
        self.index = index

    def evaluate(self):
        #print('evaliating index')
        try:
            listt = self.l.evaluate()
            #print(listt)
            #print('YERR')
            return listt[self.index.evaluate()]
        except:
            print('SEMANTIC ERROR')
            raise Exception



class InNode(Node):
    def __init__(self, l, item):
        self.l = l
        self.item = item

    def evaluate(self):
        try:
            return self.item.evaluate() in self.l.evaluate()
        except:
            print('SEMANTIC ERROR')
            raise Exception


class ListItemNode(Node):
    def __init__(self, v):
        self.v = v

    def evaluate(self):
        try:
            return self.v.evaluate()
        except:
            print('SEMANTIC ERROR')
            raise Exception

tokens = (
    'LBRACE', 'RBRACE',
    'COMMA','LPAREN', 'RPAREN',
    'NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE',
    'AND', 'OR', 'POW', 'MOD', 'NOT', 'FLOOR',
    'GT', 'GE', 'EQ', 'NE', 'LT', 'LE', 'STRING', 'BOOL','IN'
    )

# Tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_RBRACE = r'\]'
t_LBRACE = r'\['
t_COMMA = r','
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_AND = 'and'
t_OR = 'or'
t_POW = r'\*\*'
t_MOD = r'%'
t_NOT = 'not'
t_GT = r'\>'
t_GE = r'\>\='
t_EQ = r'\=\='
t_LT = r'\<'
t_LE = r'\<\='
t_NE = r'\<\>'
t_FLOOR = r'\/\/'
t_IN = r'in'

def t_BOOL(t):
    r'True|False'
    try:
        t.value = BooleanNode(t.value)
    except ValueError:
        print("Something went wrong with string  %s", t.value)
        t.value = ''
    return t


def t_STRING(t):
    r'("[^"]*")|(\'[^\']*\')'

    t.value = t.value.strip('\"')
    t.value = t.value.strip('\'')

    try:
        t.value = StringNode(t.value)
    except ValueError:
        print("Something went wrong with string  %s", t.value)
        t.value = ''
    return t


def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t\n"


def t_error(t):
    print("Syntax error at '%s'" % t.value)


# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'LT', 'LE', 'EQ', 'NE', 'GT', "GE"),
    ('left', 'IN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'FLOOR'),
    ('left', 'MOD'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POW'),
    ('left', 'LBRACE')
#    ('left', 'LPAREN', 'RPAREN')
)


def p_root(t):
    '''
    root : expr
    '''
    t[0] = RootNode(t[1])


def p_expression_binop(t):
    '''
    expr : expr PLUS expr
         | expr MINUS expr
         | expr TIMES expr
         | expr DIVIDE expr
         | expr FLOOR expr
         | expr MOD expr
         | expr POW expr
    '''
    t[0] = BinopNode(t[2], t[1], t[3])


def p_expression_bincomp(t):
    '''
    expr : expr AND expr
         | expr OR expr
         | expr GT expr
         | expr GE expr
         | expr EQ expr
         | expr LT expr
         | expr LE expr
         | expr NE expr
    '''
    t[0] = BoolopNode(t[2], t[1], t[3])


def p_expression_list(t):
    '''
    expr : LBRACE items RBRACE
    '''
    t[0] = t[2]


def p_expression_list_item(t):
    '''
    items : items COMMA expr
    '''
    t[0] = t[1]
    t[0].l.append(t[3])


def p_expression_last_item(t):
    '''
    items : expr
    '''
    t[0] = ListNode(t[1])


def p_expression_index(t):
    '''
    expr : expr LBRACE expr RBRACE
         | STRING LBRACE expr RBRACE
    '''
    t[0] = ListIndex(t[1], t[3])


def p_expression_empty_list(t):
    '''
    expr : LBRACE RBRACE
    '''
    t[0] = ListNode(None)


def p_expression_paren(t):
    '''
    expr : LPAREN expr RPAREN
    '''
    t[0] = t[2]


def p_expression_not(t):
    '''
    expr : NOT expr
    '''
    t[0] = NotNode(t[2])


def p_expression_string(t):
    '''
    expr : STRING
    '''
    t[0] = t[1]


def p_expression_number(t):
    '''
    expr : NUMBER
    '''
    t[0] = t[1]


def p_expression_bool(t):
    '''
    expr : BOOL
    '''
    t[0] = t[1]


def p_expression_in_list(t):
    '''
    expr : expr IN expr
    '''
    t[0] = InNode(t[3], t[1])


def p_error(p):
 
    print("SYNTAX ERROR")
    raise Exception


import ply.yacc as yacc

import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')
code = ""
for line in fd:
    yacc.yacc()
    code = line.strip()
#    print(code)

    try:
        lex.input(code)
        while True:
            token = lex.token()
            if not token: break
#            print(token)
        ast = yacc.parse(code)
        ast.execute()
    except Exception:
        pass
       # print("ERROR")
#        raise Exception

