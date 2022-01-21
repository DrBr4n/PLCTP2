import ply.lex as lex

reserved = {
    'head' : 'HEAD',
    'endhead' : 'ENDHEAD',
    'end' : 'END',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do' : 'DO',
    'print' : 'PRINT',
    'string' : "STRING",
    'input' : 'INPUT'
}

tokens = (
  'NUM',
  'ID',
  'EQ',
  'NEQ',
  'MOREEQ',
  'LESSEQ'
) + tuple(reserved.values())

literals = ['(',')','{','}','[',']','+','-','*','/','%','=','>','<','!','%',',','&','|','"']

t_EQ      = r'=='
t_NEQ     = r'!='
t_MOREEQ  = r'>='
t_LESSEQ  = r'<='

def t_HEAD(t):
    r'HEAD'
    return t

def t_ENDHEAD(t):
    r'ENDHEAD'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_STRING(t):
    r'\"[^"]*\" '
    return t

def t_INPUT(t):
    r'input'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

def t_END(t):
    r'END'
    return t

def t_NUM(t):
    r'-?\d+'
    t.value = int(t.value)    
    return t

def t_ID(t):
    r'[a-zA-Z0-9]+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore  = ' \r\t'

lexer = lex.lex()
