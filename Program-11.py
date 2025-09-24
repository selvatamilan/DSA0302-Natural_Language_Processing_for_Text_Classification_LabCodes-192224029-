grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the'], ['a']],
    'N': [['dog'], ['cat'], ['fox']],
    'V': [['chased'], ['saw']]
}

def parse(symbol, tokens):
    if not tokens:
        return None
    if symbol not in grammar:
        if tokens[0] == symbol:
            return (symbol, tokens[0]), tokens[1:]
        else:
            return None
    for production in grammar[symbol]:
        remaining_tokens = tokens
        children = []
        for sym in production:
            result = parse(sym, remaining_tokens)
            if result:
                subtree, remaining_tokens = result
                children.append(subtree)
            else:
                break
        else:
            return (symbol, children), remaining_tokens
    return None

sentence = "the dog chased a cat".split()
result = parse('S', sentence)

if result and result[1] == []:
    print("Parse successful!")
    print(result[0])
else:
    print("Parse failed.")
