# Edwin Alvarez 109448839
# First I will define the classes that my parser is going to use

variables = {}

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
        self.v.evaluate()



class StmtNode(Node):
    def __init__(self, stmt, stmt_list):
        #print('Makes stmt node')
        self.stmt = stmt
        self.stmt_list = stmt_list

    def evaluate(self):
        self.stmt.evaluate()
        if self.stmt_list != None:
            self.stmt_list.evaluate()



class NumberNode(Node):
    def __init__(self, v):
        if '.' in v:
            self.v = float(v)
        else:
            self.v = int(v)

    def evaluate(self):
        return self.v


class BlockNode(Node):
    def __init__(self, v):
        self.v = v

    def evaluate(self):
        if self.v != None:
            self.v.evaluate()


class StringNode(Node):
    def __init__(self, v):
        self.v = v

    def evaluate(self):
        return self.v



class NameNode(Node):
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


class PrintNode(Node):
    def __init__(self, v):
        self.v = v

    def evaluate(self):
        try:
            print(self.v.evaluate())
        except:
            print('SEMANTIC ERROR')
            raise Exception




class AssignNode(Node):
    def __init__(self, name, v):
        self.name = name
        self.v = v

    def evaluate(self):
        try:
            variables[self.name.evaluate()] = self.v.evaluate()
        except:
            print('SEMANTIC ERROR')
            raise Exception



class VariableNode(Node):
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        try:
            return variables[self.name.evaluate()]
        except:
            print('SEMANTIC ERROR')
            raise Exception



class AssignVar2VarNode(Node):
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def evaluate(self):
        try:
            variables[self.name1.evaluate()] = variables[self.name2.evaluate()]
        except:
            print('SEMANTIC ERROR')
            raise Exception



class WhileNode(Node):
    def __init__(self, condition, stmt_list):
        self.condition = condition
        self.stmt_list = stmt_list

    def evaluate(self):
        try:
            while self.condition.evaluate():
                self.stmt_list.evaluate()

        except:
            print('SEMANTIC ERROR')
            raise Exception



class IfNode(Node):
    def __init__(self, condition, stmt_list):
        self.condition = condition
        self.stmt_list = stmt_list

    def evaluate(self):
        try:
            if self.condition.evaluate():
                self.stmt_list.evaluate()
        except:
            print('SEMANTIC ERROR')
            raise Exception



class IfElseNode(Node):
    def __init__(self, condition, stmt_list1, stmt_list2):
        self.condition = condition
        self.stmt_list1 = stmt_list1
        self.stmt_list2 = stmt_list2

    def evaluate(self):
        try:
            if self.condition.evaluate():
                self.stmt_list1.evaluate()
            else:
                self.stmt_list2.evaluate()
        except:
            print('SEMANTIC ERROR')
            raise Exception



class ListVarIndexNode(Node):
    def __init__(self, list_name, index):
        self.list_name = list_name
        self.index = index

    def evaluate(self):
        try:
            return variables[self.list_name.evaluate()][self.index.evaluate()]
        except:
            print('SEMANTIC ERROR')
            raise Exception



class ListVarAssignNode(Node):
    def __init__(self, list_name, index, v):
        self.list_name = list_name
        self.index = index
        self.v = v

    def evaluate(self):
        try:
            variables[self.list_name.evaluate()][self.index.evaluate()] = self.v.evaluate()
        except:
            print('SEMANTIC ERROR')
            raise Exception



class ListAssignNode(Node):
    def __init__(self, expr, index, v):
        self.expr = expr
        self.index = index
        self.v = v

    def evaluate(self):
        try:
            self.expr.evaluate()[self.index.evaluate()] = self.v.evaluate()
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
    'LBRACKET', 'RBRACKET',
    'COMMA','LPAREN', 'RPAREN',
    'NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE',
    'AND', 'OR', 'POW', 'MOD', 'NOT', 'FLOOR',
    'GT', 'GE', 'EQ', 'NE', 'LT', 'LE', 'STRING', 'BOOL','IN',
    'IF', 'WHILE', 'LBRACE', 'RBRACE', 'ELSE', 'VARNAME', 'SEMI',
    'ASSIGN', 'PRINT'
    )

# Tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_RBRACKET = r'\]'
t_LBRACKET = r'\['
t_COMMA = r','
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_POW = r'\*\*'
t_MOD = r'%'
t_GT = r'\>'
t_GE = r'\>\='
t_EQ = r'\=\='
t_LT = r'\<'
t_LE = r'\<\='
t_NE = r'\<\>'
t_FLOOR = r'\/\/'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r'\;'
t_ASSIGN = r'\='

def t_IN(t):
    r'in'
    return t

def t_IF(t):
    r'if'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_OR(t):
    r'or'
    return t

def t_AND(t):
    r'and'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_NOT(t):
    r'not'
    return t

def t_BOOL(t):
    r'True|False'
    try:
        t.value = BooleanNode(t.value)
    except ValueError:
        print("Something went wrong with string  %s", t.value)
        t.value = ''
    return t


def t_VARNAME(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    try:
        t.value = NameNode(t.value)
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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    t.lexer.skip()
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
    ('left', 'LBRACKET'),
    ('left', 'LBRACE')
)


def p_root(t):
    '''
    root : LBRACE stmt_list RBRACE
    '''
    t[0] = RootNode(t[2])


def p_block_statement(t):
    '''
    stmt : LBRACE stmt_list RBRACE
    '''
    t[0] = BlockNode(t[2])


def p_statement_list(t):
    '''
    stmt_list : stmt stmt_list
    '''
    t[0] = StmtNode(t[1], t[2])


def p_statement_list_empty(t):
    '''
    stmt_list :
    '''
    
    t[0] = None


def p_print_statement(t):
    '''
    stmt : PRINT LPAREN expr  RPAREN SEMI
    '''
    t[0] = PrintNode(t[3])


def p_assign_statement(t):
    '''
    stmt : VARNAME ASSIGN expr SEMI
    '''
    t[0] = AssignNode(t[1], t[3])


def p_assign_var_to_var_statement(t):
    '''
    stmt : VARNAME ASSIGN VARNAME SEMI
    '''
    t[0] = AssignVar2VarNode(t[1], t[3])


def p_assign_var_list(t):
    '''
    stmt : VARNAME LBRACKET expr RBRACKET ASSIGN expr SEMI
    '''
    t[0] = ListVarAssignNode(t[1], t[3], t[6])


def p_assign_list_statement(t):
    '''
    stmt : expr LBRACKET expr RBRACKET ASSIGN expr SEMI
         | STRING  LBRACKET expr RBRACKET ASSIGN expr SEMI
    '''
    t[0] = ListAssignNode(t[1], t[3], t[6])


def p_while_statement(t):
    '''
    stmt : WHILE LPAREN expr RPAREN LBRACE stmt_list  RBRACE
    '''
    t[0] = WhileNode(t[3], t[6])



def p_if_statement(t):
    '''
     stmt : IF LPAREN expr RPAREN LBRACE stmt_list RBRACE
    '''
    t[0] = IfNode(t[3], t[6])



def p_if_else_statement(t):
    '''
    stmt : IF LPAREN expr RPAREN LBRACE stmt_list RBRACE ELSE LBRACE stmt_list RBRACE
    '''
    t[0] = IfElseNode(t[3], t[6], t[10])



def p_name_expression_index(t):
    '''
    expr : VARNAME LBRACKET expr RBRACKET
    '''
    t[0] = ListVarIndexNode(t[1], t[3])


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
    expr : LBRACKET items RBRACKET
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
    expr : expr LBRACKET expr RBRACKET
         | STRING LBRACKET expr RBRACKET
    '''
    t[0] = ListIndex(t[1], t[3])


def p_expression_empty_list(t):
    '''
    expr : LBRACKET RBRACKET
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


def p_expression_variable(t):
    '''
    expr : VARNAME
    '''
    t[0] = VariableNode(t[1])


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
    #print(traceback.format_exc())
    raise Exception


import ply.yacc as yacc

import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')
code = ""
for line in fd:
    code += line

yacc.yacc()
code = code.strip()
#    print(code)


code = code.replace("\n", "")
code = code.replace("\t", "")
#code = code.replace(" ", "")
try:
    lex.input(code)
    while True:
        token = lex.token()
        if not token: break
        #print(token)
    #ast = yacc.parse(code, debug=1, tracking=1)
    ast = yacc.parse(code)
    #print(ast)
    ast.execute()
except Exception:
    #pass
    None
    print("ERROR")
    raise Exception

