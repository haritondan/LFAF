from collections import defaultdict

def fa_to_rg(Q, Sigma, delta, q0, F):
    # Step 1: Initialize the productions and nonterminals
    productions = defaultdict(list)
    nonterminals = set()
    for q in Q:
        nonterminals.add(q)

    # Step 2: Add the productions for the starting state
    start_productions = []
    for symbol, next_state in delta[q0].items():
        if next_state in F:
            start_productions.append(symbol + "S'")
        else:
            start_productions.append(symbol + "S")
        productions[q0].append(symbol + "S")

    if start_productions:
        nonterminals.add("S'")
        productions["S'"].extend(start_productions)

    # Step 3: Add the productions for the remaining states
    for q in Q:
        for symbol, next_state in delta[q].items():
            if next_state in F:
                productions[q].append(symbol + "S'")
            else:
                productions[q].append(symbol + next_state)

    # Step 4: Convert the productions to strings and return the grammar
    grammar = {}
    for nonterminal in nonterminals:
        grammar[nonterminal] = list(set(productions[nonterminal]))
    return grammar

def is_deterministic(Q, Sigma, delta):
    for state in Q:
        next_states = [delta[state][symbol] for symbol in Sigma]
        if len(set(next_states)) != len(Sigma):
            return False
    return True


# Example usage
Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b'}
delta = {'q0': {'a': 'q1', 'b': 'q0'}, 'q1': {'b': 'q1', 'a': 'q2'}, 'q2': {'a': 'q2', 'b': 'q3'}, 'q3': {'a': 'q3', 'b': 'q3'}}
q0 = 'q0'
F = {'q3'}

# Convert the FA to a regular grammar
grammar = fa_to_rg(Q, Sigma, delta, q0, F)
print("Regular grammar:")
for nonterminal, productions in grammar.items():
    for production in productions:
        print(nonterminal + " -> " + production)

# Check if the FA is deterministic or non-deterministic
if is_deterministic(Q, Sigma, delta):
    print("The FA is deterministic")
else:
    print("The FA is non-deterministic")