# Variant 16:
# VN={S, A, B},
# VT={a, b, c, d},
# P={
#     S → bS
#     S → dA
#     A → aA
#     A → dB
#     B → cB
#     A → b
#     B → a
# }
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





