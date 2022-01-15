import ply.lex as lex

reserved = {
    'head' : 'HEAD',
    'endhead' : 'ENDHEAD',
    'end' : 'END',
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do' : 'DO'
}

# List of token names.
tokens = (
  'NUM',
  'ID',
  'EQ',
  'NEQ',
  'MOREEQ',
  'LESSEQ',
  'AND',
  'OR',
) + tuple(reserved.values())

literals = ['(',')','{','}','[',']','+','-','*','/','%','=','>','<','?','!','%',',','$']

# Regular expression rules for simple tokens
t_EQ      = r'=='
t_NEQ     = r'!='
t_MOREEQ  = r'>='
t_LESSEQ  = r'<='
t_AND     = r'&'
t_OR      = r'\|'

def t_HEAD(t):
    r'HEAD'
    return t

def t_ENDHEAD(t):
    r'ENDHEAD'
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

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \r\t'

# Build the lexer
lexer = lex.lex()

# Reading input
#for linha in sys.stdin:
#    lexer.input(linha) 
#    for tok in lexer:
#        print(tok)
        
