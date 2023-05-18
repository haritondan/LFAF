# Laboratory work no.3: Lexer & Scanner
### Course: Formal Languages & Finite Automata
### Author: Dan Hariton, FAF-211

----

## Objectives:

1. Understand what lexical analysis is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

## Overview of theory

The process of converting a string of characters or symbols, such as the source code of a computer program, into a string of meaningful symbols or tokens is known as lexical analysis, also referred to as lexing. A parser uses these tokens to create a syntax tree, which is used to examine the program's structure and find any syntax errors.

A program called a lexer, also referred to as a tokenizer or scanner, divides a string of characters or symbols, such as source code, into smaller units called lexmes.  The lexer creates a stream of tokens that the parser can use to examine the program's syntax and find any mistakes.


The process of lexical analysis involves reading in the input source code, dividing it into lexemes, identifying the token type, generating the token, and repeating for the entire input. The lexer may also perform additional tasks such as skipping whitespace or removing comments.

The goal of the lexer is to break down the input source code into a stream of tokens that can be easily processed by the parser. By doing so, the lexer makes it easier for the parser to analyze the program's syntax and detect any errors.

## Implementation description

For this laboratory work, I implemented a lexer using the Python programming language. The purpose of this lexer is to break down an input string into individual tokens that can be further processed by a parser. 

Firstly, this code block defines several token types as string constants. These token types are used in a lexer to categorize different types of lexemes that may appear in a mathematical expression.
```
# Token types
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
EOF = 'EOF'
]
```
Then, we create the class Token() which takes as input an object. 


```
 class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )
    
    def __repr__(self):
        return self.__str__()
```
Then in the class Lexer we check our object(the whole class can be found in the source code):
```
class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
```
The main functionality of it is to check the input string until the end is reached. It then tries to match each possible token type to the input string using regular expressions. If a match is found, it creates a token and adds it to the list of tokens. It also updates the current position in the input string to the end of the matched token. If no match is found, it returns none.

```
text = '3 + 4 * 2 / ( 1 - 5 )'
lexer = Lexer(text)

while True:
    token = lexer.get_next_token()
    if token.type == EOF:
        break
    print(token)
input_string = '3 + 4 * ( 2 - 1 )'
tokens = lex(input_string)
print(tokens)
```

Lastly, the code from above calls the lex function and passes it the input string '3 + 4 * 2 / ( 1 - 5 )'. The resulting tokens are stored in the tokens variable, which is then printed to the console.

For more detailed explanations, refer to the documented source code.

## Screenshots

```
Token(INTEGER, 3)
Token(PLUS, '+')
Token(INTEGER, 4)
Token(MULTIPLY, '*')
Token(INTEGER, 2)
Token(DIVIDE, '/')
Token(LPAREN, '(')
Token(INTEGER, 1)
Token(MINUS, '-')
Token(INTEGER, 5)
Token(RPAREN, ')')
```

## Conclusions 

To sum up, in this laboratory work, I developed a lexer that converts an input text into a series of tokens, which can be analyzed by the parser to build an abstract syntax tree. The implementation used a collection of regular expressions to match the various sorts of tokens we were interested in, and it raised a SyntaxError if no match was discovered.

There are various advantages to employing a lexer to handle input strings. For starters, it abstracts away the intricacy of pattern matching, which can be a time-consuming and error-prone operation when done manually. Second, it offers a formal method of decomposing an input string into its constituent pieces, making it easier to reason about and manipulate. Finally, it can assist us in detecting mistakes early in the processing pipeline, before they propagate to subsequent stages and make debugging more difficult.

One prospective enhancement to our lexer would be to include support for dealing with white space and comments, which are generally disregarded by the lexer but might impair the readability and maintainability of the source code. Another enhancement would be to provide error recovery functionality, which would allow the lexer to continue processing an input string even if it encountered a syntax problem.

Generally, developing a lexer is a critical stage in the process of developing a compiler or interpreter, and it necessitates careful consideration of the language's syntax and semantics. Therefore, this laboratory work has helped me understand the fucntionalities and detailed inner workings of a lexer.