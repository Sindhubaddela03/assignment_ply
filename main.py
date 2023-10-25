import ply.lex as lex

# List of token names
tokens = (
    'FOR',
    'ID',       # Identifier
    'NUMBER',   # Numeric literal
    'PLUS',     # Addition operator
    'MINUS',    # Subtraction operator
    'TIMES',    # Multiplication operator
    'DIVIDE',   # Division operator
    'LPAREN',
    'RPAREN',
    'ASSIGN',   # Assignment operator
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Define a rule for identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Define a rule for numeric literals
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule for the assignment operator
def t_ASSIGN(t):
    r'='
    return t

# Define and ignore whitespace characters
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Create the lexer
lexer = lex.lex()

# Test it out
data = '''
for i in range(8):
   print(i)
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
for tok in iter(lexer.token, None):
    print(tok)
