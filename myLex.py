import ply.lex as lex

reserved = {
    'head' : 'HEAD',
    'endhead' : 'ENDHEAD',
    'exit' : 'EXIT',
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE'
}

# List of token names.
tokens = (
  'LPAREN',
  'RPAREN',
  'LBRACK',
  'RBRACK',
  'LCP',
  'RCP',
  'NUM',
  'ID',
  'EQ',
  'NE',
  'PLUS',
  'MINUS',
  'TIMES',
  'DIVIDE',
  'MORE',
  'MOREEQ',
  'LESS',
  'LESSEQ',
  'AND',
  'OR',
  'COMMA',
  'IF',
  'THEN',
  'ELSE',
  'WHILE',
  'DO',
  
) + tuple(reserved.values())

literals = ['(' , ')' , '=' , '?' , '!' , '%' , '{' , '}']


# Regular expression rules for simple tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACK  = r'\['
t_RBRACK  = r'\]'
t_LCP     = r'\{'
t_RCP     = r'\}'
t_EQ      = r'=='
t_NE      = r'!='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LESS    = r'<'
t_LESSEQ  = r'<='
t_MORE    = r'>'
t_MOREEQ  = r'>='
t_AND     = r'&'
t_OR      = r'\|'
t_COMMA   = r','
t_EXIT    = r'EXIT'

def t_NUM(t):
    r'\d+'
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
        
