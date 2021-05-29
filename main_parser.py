#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 19:06:32 2021

@author: kevinxie
"""

from ply import yacc as yacc
from lex_token import tokens

'''
The lex.py module is used to break input text into a collection of tokens specified by a collection of regular expression rules. 
yacc.py is used to recognize language syntax that has been specified in the form of a context free grammar.
'''


# EXPR
def p_expression_plus(p):
    'expression : expression PLUS term'
    #   ^            ^        ^    ^
    #  p[0]         p[1]     p[2] p[3]

    p[0] = p[1] + p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

# TERM
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

# FACTOR
def p_factor_ID(p):
    'factor : ID'
    'because p[1] is value, so do this judge'
    if p[1] == 'a':
        p[0] = a_value
    elif p[1] == 'b':
        p[0] = b_value
    elif p[1] == 'c':
        p[0] = c_value
        
        
        
# p_factor_ID refer this

# def p_binary_operators(p):
#     '''expression : expression PLUS term
#                   | expression MINUS term
#        term       : term TIMES factor
#                   | term DIVIDE factor'''
#     if p[2] == '+':
#         p[0] = p[1] + p[3]
#     elif p[2] == '-':
#         p[0] = p[1] - p[3]
#     elif p[2] == '*':
#         p[0] = p[1] * p[3]
#     elif p[2] == '/':
#         p[0] = p[1] / p[3]
        

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
       a_value = int(input('   a > '))
       b_value = int(input('   b > '))
       c_value = int(input('   c > '))
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   
   print('answer is %d' %result)