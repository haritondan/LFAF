# Laboratory Work 1

### Course: Formal Languages & Finite Automata
### Author: Hariton Dan

----


## Objectives:

* Understand what a language is and what it needs to have in order to be considered a formal one.

* Provide the initial setup for the evolving project that you will work on during this semester. I said project because usually at lab works, I encourage/impose students to treat all the labs like stages of development of a whole project. Basically you need to do the following:

    a. Create a local && remote repository of a VCS hosting service (let us all use Github to avoid unnecessary headaches);
    
    b. Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms;
    
    c. Create a separate folder where you will be keeping the report. This semester I wish I won't see reports alongside source code files, fingers crossed;

* According to your variant number (by universal convention it is register ID), get the grammar definition and do the following tasks:

    a. Implement a type/class for your grammar;
    
    b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;
    
    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
    
    d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;


## Implementation description

* Since I left comments on my code I didn't left any comments here.



* Grammar Code snippets
```
def generate_word(grammar, symbol):
    if symbol not in grammar:
        return symbol
    production = random.choice(grammar[symbol])
    return ''.join(generate_word(grammar, s) for s in production)
```
* FA Code snippets
```
def grammar_to_finite_automaton(grammar):
    states = set(grammar.keys()) | {'S0'}
    alphabet = set([s for rule in grammar.values() for s in rule if s.islower()])

    transitions = {}
    for state in states:
        for symbol in alphabet:
            dest_state = 'dead'
            for rule in grammar.get(state, []):
                if symbol in rule:
                    dest_state = ''.join([s if s.isupper() else '' for s in rule])
            transitions[(state, symbol)] = dest_state

    start_state = 'S0'
    accept_states = set(state for state in states if any(word == state for word in generate_word(grammar, 'S')))
    return (states, alphabet, transitions, start_state, accept_states)
```

## Conclusions / Screenshots / Results
* Results for the Grammar code

![alt text](images/img1.png)

* Results for the FA code

![alt text](images/img2.png)