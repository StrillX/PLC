'''
 def t_PRINT(t):
 r’print’
 return t

 def t_RETURN(t):
 r’return’
 return t

 def t_READ(t):
 r’read()’
 return t
def t_WHILE(t):
 r’while’
 return t

 def t_INT(t):
 r’int’
 return t

 def t_IF(t):
 r’if’
 return t

 def t_ELSE(t):
 r’else’
 return t

 def t_NOME(t):
 r’[A-Za-z]+()’
 return t

 def t_STRING(t):
 r’"[A-Za-z]+(:)?"’
 return t

 def t_id(t):
 r’[a-z]’
 return t

 def t_num(t):
 r’(-)?\d+’
 return t
'''

import ply.lex as lex

INT = 1
FLOAT = 2
ARRAY = 3
STRING = 4


class Lexer:
    def __init__(self, var: dict):
        self.var = var

    tokens = [
        'INT',
        'FLOAT',
        'ID',
        'VARINT'
        'VARFLOAT',
        'VARSTRING',
        'VARARRAY',
        'GEQUAL',
        'LEQUAL',
        'EQUAL',
        'DIFF',
        'PP',
        'MM'
    ]
    literais = [
        '+',
        '-',
        '*',
        '/',
        '%',
        '(',
        ')',
        '[',
        ']',
        '{',
        '}',
        '=',
        '>',
        '<',
        ',',
        ';'
    ]
    reservadas = {
        'int': 'INTR',
        'float': 'FLOATR',
        'str': 'STRR',
        'or': 'OR',
        'and': 'AND',
        'not': 'NOT',
        'if': 'IF',
        'else': 'ELSE',
        'for': 'FOR',
        'while': 'WHILE',
        'print': 'PRINT',
    }

    def t_FLOAT(self, t):
        r'(\d*)?\.\d+(e(?:\+|-)\d+)?'
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    t_GEQUAL = r'>='
    t_LEQUAL = r'<='
    t_EQUAL = r'=='
    t_DIFF = r'!='
    t_PP = r'++'
    t_MM = r'--'
    t_AND = r'&&'
    t_OR = r'\|\|'

    def t_ID(self, t):
        r'[a-zA-Z][a-zA-Z0-9_\']*'
        t.type = Lexer.reservadas.get(t.value, 'ID')
        v = self.var.get(t.value, None)
        if v is not None:
            tipo = v[1]
            if tipo == INT:
                t.type = 'VARINT'
            elif tipo == FLOAT:
                t.type = 'VARFLOAT'
            elif tipo == ARRAY:
                t.type = 'VARARRAY'
            elif tipo == STRING:
                t.type = 'VARSTRING'
        return t

    t_ignore = ' \t'

    def t_error(self, t):
        print(rf"Illegal char {t.value[0]}")
        t.lexer.skip(1)

    def t_newline(self, t):
        r'\n'
        t.lexer.numline += 1

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
