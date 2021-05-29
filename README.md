# theory_of_computing_Parser HW4

*Write a small parser to evaluate any legitimate expression consisting of a, b, c, +, *, (,), 
using the following CFG: 


>({EXPR, TERM, FACTOR}, {a, b, c, +, *, (, )}, R, EXPR), where R contains 
>
>>EXPR -> EXPR + TERM | TERM
>
>>TERM -> TERM * FACTOR | FACTOR
>
>>FACTOR -> (EXPR)|a|b|c


&nbsp; &nbsp; &nbsp; &nbsp;For example, ((a + b) * a + c) * a + b * c should be evaluated to 12 when a=1, b=2, c=3.


## Strucure of files
* lex_token.py (tokenize input string)
* main_parser.py (parse language syntax)
* parsetab.py (auto-generated, yacc reloads the table from parsetab.py when change is detected in the underlying grammar)
* parser.out (auto-generated, debugging file for yacc)


## Usage


```
python3 main_parser.py
```


This will start the parser. You can test it by yourself. The output is a number.

![image](https://github.com/oh-hi-yo/theory_of_computing_Parser/blob/main/result_picture1.png)
