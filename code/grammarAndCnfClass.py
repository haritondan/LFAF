class Grammar:
    # Constructor of Grammar class
    def __init__(self, V_N, V_T, P):
        self.V_N = V_N
        self.V_T = V_T
        self.P = P

    # Method which generate words corresponding to rules
    def generate_string(self):
        import random
        # Start of the word
        word = "S"
        # Set of final states
        final_state = " "
        # While loop which create a random word
        while word[-1] not in final_state:
            options = []
            for vn, prod in self.P.items():
                if vn == word[-1]:
                    options += prod
            if not options:
                return None
            production = random.choice(options)
            word = word[:-1] + production
        return word


    def cnf(self):
        reachable = {'S'}
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if len(production) == 1 and production.isupper():
                    self.P[symbol].remove(production)
                    self.P[symbol].update(self.P[production])
        changed = True
        while changed:
            changed = False
            for nonterm, productions in self.P.items():
                if nonterm in reachable:
                    for prod in productions:
                        for symbol in prod:
                            if symbol in self.V_N:
                                if symbol not in reachable:
                                    reachable.add(symbol)
                                    changed = True
        inaccessible = self.V_N - reachable
        for nonterm in inaccessible:
            del self.P[nonterm]
        self.V_N.remove(nonterm)
        for nonterm, productions in self.P.items():
            new_productions = set()
            for prod in productions:
                if all(symbol in reachable.union(self.V_T) for symbol in prod):
                    new_productions.add(prod)
            self.P[nonterm] = new_productions

        new_symbol_index = 0
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if len(production) > 2:
                    new_symbol = f'X{new_symbol_index}'
                    new_symbol_index += 1
                    self.P[new_symbol] = set()
                    self.P[new_symbol].add(production[0])
                    for i in range(1, len(production) - 1):
                        intermediate_symbol = f'X{new_symbol_index}'
                        new_symbol_index += 1
                        self.P[intermediate_symbol] = set()
                        self.P[intermediate_symbol].add(production[i])
                        self.P[new_symbol].add(intermediate_symbol)
                        self.V_N.add(intermediate_symbol)
                        reachable.add(intermediate_symbol)
                    self.P[new_symbol].add(production[-1])
                    self.P[symbol].remove(production)
                    self.P[symbol].add(new_symbol)
                    self.V_N.add(new_symbol)
                    reachable.add(new_symbol)

        epsilon_productions = []
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if production == 'ε':
                    epsilon_productions.append((symbol, production))
                    self.P[symbol].remove(production)
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                for epsilon in epsilon_productions:
                    new_production = production.replace(epsilon[0], '')
                    if new_production != production:
                        self.P[symbol].add(new_production)

        return self.V_N, self.V_T, self.P
