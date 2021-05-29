# theory_of_computing_Parser HW4

*Write a small parser to evaluate any legitimate expression consisting of a, b, c, +, *, (,), 
using the following CFG: ({EXPR, TERM, FACTOR}, {a, b, c, +, *, (, )}, R, EXPR), where R contains 


ˋEXPR -> EXPR + TERM | TERMˋ
&nbsp; &nbsp;TERM -> TERM * FACTOR | FACTOR
&nbsp; &nbsp;FACTOR -> (EXPR)|a|b|c


*For example, ((a+b)*a+c)*a+b*c should be evaluated to 12 when a=1, b=2, c=3.


## install
