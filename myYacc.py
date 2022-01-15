from __future__ import print_function
from nis import match
from myLex import tokens
import ply.yacc as yacc
import re
import sys


def p_Program(p):
    "Program : HEAD Decls ENDHEAD Bodys END"
    print(p[2] + "START\n" + p[4] + "STOP\n", end = "")

def p_Decls(p):         #caso Decls seja vazio: erro de syntaxe no ENDHEAD, START e STOP aparecem consecutivamente
    "Decls : Decls Decl"
    p[0] = p[1] + p[2]

def p_Bodys(p):
    "Bodys : Bodys Body"
    p[0] = p[1] + p[2]

def p_DeclId(p):   
    "Decl : ID"         
    if p[1] in parser.idTab:
        p[0] = """PUSHS "Error variable already in use"\n""" + "WRITES" + "\n"
    else:
        p[0] = "PUSHI 0 " + "\n" + "STOREG " + str(parser.proxAddr) + "\n"
        parser.idTab[p[1]] = (parser.proxAddr, "INT", 1)     
        parser.proxAddr += 1

def p_Decl(p):              
    "Decl : ID '=' Expression"
    if p[1] in parser.idTab:
        p[0] = """PUSHS "Error variable already in use"\n""" + "WRITES" + "\n"
    else:
        p[0] = p[3] + "STOREG " + str(parser.proxAddr) + "\n"
        parser.idTab[p[1]] = (parser.proxAddr, "INT", 1)
        parser.proxAddr += 1

def p_Simple(p):
    """Bodys : Body
       Decls : Decl
       Body : Expression
       Body : Atrib
       Expression : Term
       Term : Factor"""
    p[0] = p[1]

def p_Empty(p):
    "Body : "
    "Decl : "
    p[0] = ""

def p_Atrib(p):
    "Atrib : ID '=' Expression"
    if (p[1] in parser.idTab):
        p[0] = p[3] + "STOREG " + str(parser.idTab[p[1]][0]) + "\n"
    else:
        p[0] = """PUSHS "Error variable not declared"\n""" + "WRITES" + "\n"

def p_ExpressionOperations(p):
    """Expression : Expression '+' Term
                  | Expression '-' Term
                  | Expression EQ Term
                  | Expression NEQ Term
                  | Expression '>' Term
                  | Expression MOREEQ Term
                  | Expression '<' Term
                  | Expression LESSEQ Term"""

    if (p[2] == '+'):
        p[0] = p[1] + p[3] + "ADD \n"
    elif (p[2] == '-'):
        p[0] = p[1] + p[3] + "SUB \n"
    elif (p[2] == "=="):
        p[0] = p[1] + p[3] + "EQUAL \n"
    elif (p[2] == "!="):
        p[0] = p[1] + p[3] + "NEQ \n"           #qual e o codigo assembly?   
    elif (p[2] == '>'):
        p[0] = p[1] + p[3] + "SUP \n"
    elif (p[2] == ">="):
        p[0] = p[1] + p[3] + "SUPEQ \n"
    elif (p[2] == '<'):
        p[0] = p[1] + p[3] + "INF \n"
    elif (p[2] == "<="):
        p[0] = p[1] + p[3] + "INFEQ \n"
    elif(p[2] == '='):
        p[0] = p[3] + p[1]

def p_TermOperations(p):
    """Term : Term '*' Factor
            | Term '/' Factor
            | Term '%' Factor"""
    if p[2] == '*':
        p[0] = p[1] + p[3] + "MUL \n"
    elif p[2] == '/':
        p[0] = p[1] + p[3] + "DIV \n"
    elif p[2] == '%':
        p[0] = p[1] + p[3] + "MOD \n"

def p_FactorNum(p):
    "Factor : NUM"
    p[0] = "PUSHI " + str(p[1]) + "\n"

def p_FactorID(p):
    "Factor : ID"
    if (p[1] in parser.idTab):
        p[0] = "PUSHG " + str(parser.idTab[p[1]][0]) + "\n"
    else:
        p[0] = """PUSHS "Error variable not declared"\n""" + "WRITES" + "\n"

def p_FactorExpression(p):
    "Factor : '(' Expression ')'"
    p[0] = p[2]

def p_error(p):
    print('Syntax errorr: ', p)
    parser.success = False



# Build the parser
parser = yacc.yacc()
#parser.success = True
parser.proxAddr = 0
parser.idTab = {}           #'name':(endereco, tipo, tamanho)

with open("input.txt", 'r') as file:
    text = file.read()

print(text)
parser.parse(text)

#for line in sys.stdin:
#    parser.success = True
#    result = parser.parse(line)

#"""
###Program : HEAD Decls ENDHEAD Bodys END
###Decls : Decls Decl
###      | Decl
###Bodys : Bodys Body
###      | Body
###Decl : ID
###     | ID '=' Expression
###     | "
###Body : Expression
###     | Atrib
#     | Condicion
#     | Logics
#     | Cicle
#     | "
#Atrib : ID '=' Expression 
##Expression : Term
###           | Expression '+' Term
###           | Expression '-' Term
###           | Expression EQ Term
##           | Expression NEQ Term
###           | Expression MORE Term
###           | Expression MOREEQ Term
###           | Expression LESS Term
###           | Expression LESSEQ Term
###Term : Factor
###     | Term '*' Factor
###     | Term '/' Factor
###     | Term '%' Factor
###Factor : NUM
##       | ID
###       | '(' Expression ')' 
#Logics : Logics '&' Expression
#       | Logics '|' Expression
#       | Expression
#Condicion : IF '(' Expression ')' '{' body '}' ELSE '{' body '}'
#cicle : WHILE '(' Logics ')' DO '{' body '}'
#"""
