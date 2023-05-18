# Lab 1 ------------------
print(" Lab 1")
from Labs.code.RegularGrammarAndFA.finite import grammar_to_finite_automaton, grammar
from Labs.code.RegularGrammarAndFA.generatewords import generate_word

grammar_to_finite_automaton(grammar)
generate_word(grammar, 'S')




# Lab 2-------------------
print("\n Lab 2")
from Labs.code.FiniteAutomata.grammarHierarchy import chomsky_hierarchy
from Labs.code.FiniteAutomata.finiteToRegular import fa_to_rg, Q, Sigma, delta,q0, F
chomsky_hierarchy(grammar)
print('\n')
fa_to_rg(Q, Sigma, delta, q0, F)





# Lab 3-------------------
from Labs.code.Lexer.lexer import Lexer, EOF
print("\n Lab 3")
text = '3 + 4 * 2 / ( 1 - 5 )'
lexer = Lexer(text)




# Lab 4-------------------
print("\n Lab 4")
from Labs.code.CNF import grammarAndCnfClass

V_N = {'S', 'A', 'B', 'C'}
V_T = {'a', 'b'}
P = {
    "S": {"abAB"},
    "A": {"aSab", "BS", "aA","b"},
    "B": {"b", "BA", "ababB", ""},
    "C": {"AS"},
}
grammar = grammarAndCnfClass.Grammar(V_N, V_T, P)
grammar.cnf()
print(V_N)
print(V_T)
print(P)


# Lab 5--------------------
print("\n Lab 5")
from Labs.code.Lexer.lexer import Lexer, Parser, Interpreter


text = '3 + 4 * 2 / (1 - 5)'
lexer = Lexer(text)
parser = Parser(lexer)
interpreter = Interpreter(parser)
result = interpreter.interpret()
print("Result:", result)  # Output: Result: 5.0

print("Expression Tree:")
parser.print_tree(parser.expr())
# 