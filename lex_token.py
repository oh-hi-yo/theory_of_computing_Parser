#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:32:53 2021

@author: kevinxie
"""

# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'ID',
   'PLUS',
   'TIMES',
   'LPAREN',
   'RPAREN',
)

# Regular expression rules for simple tokens
t_ID = r'[a-c]'
t_PLUS    = r'\+'
t_TIMES   = r'\*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'



# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# if want runs this code, refer to : https://ply.readthedocs.io/en/latest/ply.html#lex 
# # Test it out
# data = '''
# 3 + 4 * 10 +
#  -20 * 2
# '''

# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     # print(tok)
#     # type, value,  location of the token,  index of the token relative to the start of the input text
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)

# # Lexers also support the iteration protocol. So, you can write the above loop as follows:
# # for tok in lexer:
# #     print(tok)
