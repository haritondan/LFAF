def nfa_to_dfa(Q, Sigma, delta, q0, F):
    # Compute the epsilon closure of each state
    epsilon_closure = {}
    for state in Q:
        epsilon_closure[state] = set()
        stack = [state]
        while stack:
            current_state = stack.pop()
            epsilon_closure[state].add(current_state)
            for next_state in delta[current_state].get('', []):
                if next_state not in epsilon_closure[state]:
                    stack.append(next_state)

    # Initialize the DFA
    dfa_states = []
    dfa_delta = {}
    dfa_q0 = frozenset(epsilon_closure[q0])
    dfa_F = set()
    queue = [dfa_q0]

    # Compute the DFA states and transitions
    while queue:
        current_state = queue.pop(0)
        dfa_states.append(current_state)
        dfa_delta[current_state] = {}
        for symbol in Sigma:
            next_state = set()
            for nfa_state in current_state:
                next_state.update(delta[nfa_state].get(symbol, []))
            next_state_closure = set()
            for nfa_state in next_state:
                next_state_closure.update(epsilon_closure[nfa_state])
            next_state = frozenset(next_state_closure)
            if next_state:
                dfa_delta[current_state][symbol] = next_state
                if next_state not in dfa_states:
                    queue.append(next_state)

        # Check if the current state is an accepting state
        for nfa_state in current_state:
            if nfa_state in F:
                dfa_F.add(current_state)
                break

    return dfa_states, Sigma, dfa_delta, dfa_q0, dfa_F


    print("DFA states:", dfa_states)
    print("DFA transitions:", dfa_delta)
    print("DFA initial state:", dfa_q0)
    print("DFA accepting states:", dfa_F)

# Example usage
Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b'}
delta = {'q0': {'a': 'q1', 'b': 'q0'}, 'q1': {'b': 'q1', 'a': 'q2'}, 'q2': {'a': 'q2', 'b': 'q3'}, 'q3': {'a': 'q3', 'b': 'q3'}}
q0 = 'q0'
F = {'q3'}

nfa_to_dfa(Q, Sigma, delta, q0, F)
