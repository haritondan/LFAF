# Laboratory work no.5: Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata
### Author: Dan Hariton, FAF-211

----

## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed.
2. Get familiar with the concept of AST. 
3. In addition to what has been done in the 3rd lab work do the following:
      * In case you didn't have a type that denotes the possible types of tokens you need to:
        * Have a type TokenType (like an enum) that can be used in the lexical analysis to categorize the tokens.
        * Please use regular expressions to identify the type of the token.
     *   Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
     *   Implement a simple parser program that could extract the syntactic information from the input text.

* The Lexer class is responsible for tokenizing the input string into individual tokens. It scans the input text character by character and matches them against predefined regular expressions to identify different token types such as integers, operators, parentheses, etc. It generates a list of tokens that the parser will use to construct the abstract syntax tree (AST).
```
  class Lexer:
    def __init__(self, text):
        self.tokens = []
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        TOKENS = {
            INTEGER: r'\d+',
            PLUS: r'\+',
            MINUS: r'-',
            MULTIPLY: r'\*',
            DIVIDE: r'/',
            LPAREN: r'\(',
            RPAREN: r'\)',
        }
        self.token_regex = re.compile('|'.join(f'(?P<{name}>{regex})' for name, regex in TOKENS.items()))
```
The AST class serves as the base class for different types of nodes in the abstract syntax tree. It does not have any specific functionality but is used as a common interface for nodes such as Num (representing a numeric value) and BinOp (representing a binary operation).
```

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
```
The Parser class performs syntax analysis by parsing the stream of tokens produced by the Lexer. It uses a technique called recursive descent parsing to build an abstract syntax tree (AST) from the tokens. The parser follows a set of grammar rules to recognize and combine tokens into higher-level structures, such as expressions, terms, and factors. The resulting AST represents the syntactic structure of the input expression.
```
 class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
```
* The Lexer scans the input text and generates a list of tokens.
* The Parser receives the list of tokens from the Lexer and constructs an abstract syntax tree (AST) by applying grammar rules and recursively building nodes.
* The Interpreter visits each node in the AST and evaluates the expression based on the type of node and the corresponding operation.
* Finally, the result of the expression evaluation is printed, along with the tree structure of the expression.
## Output
```
Result: 5.0
Expression Tree:
PLUS
  INTEGER(3)
  DIVIDE
    MULTIPLY
      INTEGER(4)
      INTEGER(2)
    MINUS
      INTEGER(1)
      INTEGER(5)
```

## Conclusion
In this laboratory, In conclusion, the process of tokenizing, parsing, and evaluating arithmetic expressions involves three key components: the Lexer, Parser, and Interpreter.

The Lexer plays the role of scanning the input text and breaking it down into individual tokens. It identifies different token types, such as integers and operators, using regular expressions. The Lexer generates a list of tokens that represent the fundamental building blocks of the expression.

The Parser receives the list of tokens from the Lexer and constructs an abstract syntax tree (AST). It applies grammar rules and recursively builds nodes in the AST, representing the syntactic structure of the expression. The Parser ensures that the expression adheres to the specified grammar and captures the relationships between different elements of the expression.

The Interpreter visits each node in the AST and evaluates the expression based on the type of node and the corresponding operation. It recursively traverses the AST, performing the required computations for each node. By evaluating the expression, the Interpreter computes the final result.

Finally, the result of the expression evaluation is printed, providing the outcome of the arithmetic expression. Additionally, the tree structure of the expression is printed to visualize the hierarchical organization of the expression and the relationships between its components.

Together, the Lexer, Parser, and Interpreter form a pipeline for handling arithmetic expressions. This process enables the transformation of an input expression into an AST, which is then used to evaluate the expression and produce the desired result.
## References
[1] [Parsing Wiki](https://en.wikipedia.org/wiki/Parsing)

[2] [Abstract Syntax Tree Wiki](https://en.wikipedia.org/wiki/Abstract_syntax_tree)               