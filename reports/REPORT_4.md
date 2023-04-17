# Laboratory work no.4: Chomsky Normal Form

### Course: Formal Languages & Finite Automata
### Author: Dan Hariton, FAF-211

----

## Objectives:
1. Learn about Chomsky Normal Form (CNF) [1].
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    2. The implemented functionality needs executed and tested.
    3. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    4. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.
## Implementation 
This code searches the grammar for any instances of epsilon productions, which are production rules that convert non-terminal symbols into empty strings.
The code initially obtains all production rules related to each non-terminal symbol in the language using the function 'P[symbol]', which produces a list of strings that represent every conceivable production for that non-terminal.
Then, using the "for production in productions" loop, it goes through each production for that non-terminal and determines whether the current production is an epsilon production by determining whether the string 'production' equals the character 'ε' .
If the current production is an epsilon production, then the code adds the '(symbol, production)' tuple to a list called 'epsilon_productions', indicating that the non-terminal symbol can produce an empty string. It then removes the epsilon production from the set of productions for that non-terminal using 'P[symbol].remove(production)' to ensure that the grammar is in Chomsky normal form, which prohibits epsilon productions.
```
        epsilon_productions = []
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if production == 'ε':
                    epsilon_productions.append((symbol, production))
                    self.P[symbol].remove(production)
```
The code retrieves the set of productions connected to each symbol in the grammar by iterating over each one. It determines whether an epsilon string is present in each production. If it does, the code creates a fresh production by substituting an empty string for the epsilon string. The set of productions connected to the same symbol is then expanded to include the new production.
```
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                for epsilon in epsilon_productions:
                    new_production = production.replace(epsilon[0], '')
                    if new_production != production:
                        self.P[symbol].add(new_production)
```
The code checks that no productions in the grammar rules contain even a single non-terminal symbol by repeatedly running through the dictionary's "P" entry. 
If such a production is found, the code removes the discovered production from the set of productions for that symbol and updates the set with the productions of the non-terminal symbol that were found in the production.

```
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if len(production) == 1 and production.isupper():
                    self.P[symbol].remove(production)
                    self.P[symbol].update(self.P[production])
```
This code is a part of an algorithm used to find the set of all unreachable non-terminals in a context-free grammar.
As long as no additional non-terminals are added to reachable during an iteration, the while loop continues to loop. To keep track of whether any new non-terminals were added to reachable in the most recent iteration, use the changed variable.
In each iteration, the loop goes through all the non-terminals in the grammar, and for each non-terminal nonterm, it checks whether it is already in reachable. If it is, then it looks at each of its production rules of production, and for each symbol in the production rule, it checks whether it is a non-terminal.
```
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
```
The code scans through the production rules of a grammar and identifies any productions that have more than two symbols. For each such production, it generates new intermediate symbols to split it into smaller pieces. These intermediate symbols are given new names starting with 'X' and an increasing index number. The code replaces the original production rule with the new intermediate symbols, resulting in a grammar with only two symbols on the right-hand side of each production rule.
```
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
                    self.P[new_symbol].add(production[-1])
                    self.P[symbol].remove(production)
                    self.P[symbol].add(new_symbol)
                    self.V_N.add(new_symbol)
```
## Output
```
{'X5', 'B', 'X1', 'X6', 'A', 'X3', 'X8', 'X7', 'X0', 'S', 'X9', 'X4', 'X2'}
{'a', 'b'}
{
'S': {'X0'}, 'A': {'BS', 'aA', 'b', 'X3'}, 'B': {'', 'BA', 'X6', 'b'}, 
'X0': {'B', 'a', 'X1', 'X2'}, 'X1': {'b'}, 'X2': {'A'}, 
'X3': {'X5', 'X4', 'a', 'b'}, 'X4': {'S'}, 'X5': {'a'}, 
'X6': {'B', 'X8', 'X7', 'X9', 'a'}, 'X7': {'b'}, 'X8': {'a'}, 'X9': {'b'}
}
```

## Conclusion
In this laboratory, we did create a function in Python that turns a grammar into CNF. 
It can be really helpful for language processing tasks. 
Using CNF makes it easier to work with complex grammars by simplifying how they are read and allowing for more efficient processing. If you make your own function for this, it can save you time and make your code more accurate.
The laboratory offers a step-by-step user interface that enables users to view the process of converting a language to Chomsky normal form in real-time, aiding us in understanding the algorithm and its application.
## References
[1] [Chomsky Normal Form Wiki](https://en.wikipedia.org/wiki/Chomsky_normal_form)
                 