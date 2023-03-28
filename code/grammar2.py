import random

# Define the grammar
grammar = {
    'S': ['bS', 'dA'],
    'A': ['aA', 'dB', 'b'],
    'B': ['cB', 'a']
}

# Define the function to generate words from the grammar
def generate_word(grammar, symbol):
    if symbol not in grammar:
        return symbol
    production = random.choice(grammar[symbol])
    return ''.join(generate_word(grammar, s) for s in production)


# Generate 5 words from the grammar
for i in range(5):
    word = generate_word(grammar, 'S')
    print(word)


# Classify the grammar
def chomsky_hierarchy(grammar):
    # Check if the grammar is Type 3 (regular)
    if all(len(production) <= 2 and (production[0].islower() or production[0].isupper()) and
           (len(production) == 1 or production[1].isupper() or production[1] == 'ε') for symbol in grammar for
           production in grammar[symbol]):
        return "Type 3 (regular)"

    # Check if the grammar is Type 2 (context-free)
    if all(len(production) <= 2 and all(s.isupper() for s in production) for symbol in grammar for production in
           grammar[symbol]):
        return "Type 2 (context-free)"

    # Check if the grammar is Type 1 (context-sensitive)
    for symbol in grammar:
        for production in grammar[symbol]:
            if len(production) < len(symbol) and not any(s.islower() for s in production):
                return "Type 1 (context-sensitive)"

    # Check if the grammar is Type 0 (unrestricted)
    for symbol in grammar:
        for production in grammar[symbol]:
            if symbol in production:
                continue
            if not all(s in grammar for s in production):
                return "Type 0 (unrestricted)"

    # If the grammar does not fit into any of the above categories, it is not a context-free grammar
    return "Not context-free"


print(chomsky_hierarchy(grammar))
