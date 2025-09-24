import re
token_specification = [
    ('FORALL', r'∀'),        
    ('EXISTS', r'∃'),         
    ('AND', r'∧'),            
    ('OR', r'∨'),             
    ('IMPLIES', r'→'),        
    ('NOT', r'¬'),            
    ('LPAREN', r'\('),        
    ('RPAREN', r'\)'),        
    ('COMMA', r','),          
    ('PREDICATE', r'[A-Z][a-zA-Z0-9_]*'),  
    ('VARIABLE', r'[a-z][a-zA-Z0-9_]*'),   
    ('SKIP', r'\s+'),         
    ('MISMATCH', r'.'),       
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

def tokenize(expression):
    tokens = []
    for mo in re.finditer(token_regex, expression):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected token: {value}')
        tokens.append((kind, value))
    return tokens


expression = "∀x (P(x) → ∃y Q(x,y))"
tokens = tokenize(expression)
print("Tokens:")
for t in tokens:
    print(t)
