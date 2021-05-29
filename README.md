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


&nbsp; &nbsp; &nbsp; &nbsp;For example, ((a+b)*a+c)*a+b*c should be evaluated to 12 when a=1, b=2, c=3.


## install
