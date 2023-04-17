import grammarAndCnfClass

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