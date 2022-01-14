from email.headerregistry import Address
from myLex import tokens
import ply.yacc as yacc
import re
import sys

# Build the parser
parser = yacc.yacc()
#parser.success = True
parser.proxAddr = 0
parser.idTab = {}


def p_Program(p):          #quando se reconhece o codigo significa que esta no fim entao da se print
    "Program : Body"         
    print("START\n" + p[1] + "STOP\n")

def p_HeadId(p):
    "Head : ID"

def p_Head(p):
    "Head : ID '=' Expression"
    if p[1] in parser.idTab:
        p[0] = """PUSHS "Error variable already in use"\n""" + "WRITES"
        

def p_BodyExpression(p):
    "Body : Expression"
    p[0] = p[1]

def p_ExpressionTerm(p):
    "Expression : Term"
    p[0] = p[1]

def p_Sum(p):
    "Expression : Expression PLUS Term"
    p[0] = p[1] + p[3] + "ADD \n"

def p_Sub(p):
    "Expression : Expression MINUS Term"
    p[0] = p[1] + p[3] + "SUB \n"

def p_TermFactor(p):
    "Term : Factor"
    p[0] = p[1]

def p_FactorNum(p):
    "Factor : NUM"
    p[0] = "PUSHI " + str(p[1]) + "\n"

def p_FactorID(p):
    "Factor : ID"
    p[0] = "PUSHG " + str(p[1]) + "\n"



#"""
##Program : HEAD Head ENDHEAD Body EXIT
#Head : ID '=' Expression
##Body : Expression
#     | Condicion
#     | Logics
#     | Cicle
#     | "
##Expression : Term
##           | Expression '+' Term
##           | Expression '-' Term
#           | EQ Expression Term
#           | NE Expression Term
#           | MORE Expression Term
#           | MOREEQ Expression Term
#           | LESS Expression Term
#           | LESSEQ Expression Term
##Term : Factor
#     | '*' Term Factor
#     | '/' Term Factor
#     | '%' Term Factor
##Factor : NUM
##       | ID
#       | '(' Expression ')' 
#Logics : Logics '&' Expression
#       | Logics '|' Expression
#       | Expression
#Condicion : IF '(' Expression ')' '{' body '}' ELSE '{' body '}'
#cicle : WHILE '(' Logics ')' DO '{' body '}'
#"""


def p_error(p):
    print('Syntax errorr: ', p)
    parser.success = False


for line in sys.stdin:
    parser.success = True
    result = parser.parse(line)