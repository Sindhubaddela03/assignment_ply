import forloop_lex
data='''
3 + 4 * 10
'''
forloop_lex.lexer.input(data)
while True:
    tok=forloop_lex.lexer.token()
    if not tok:
        break
    print(tok)    

