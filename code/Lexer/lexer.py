import re

# Token types
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
EOF = 'EOF'

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.type}({self.value})"
        return f"{self.type}"

class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

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

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):
        while self.current_char is not None:
            match = self.token_regex.match(self.text, self.pos)
            if match:
                token_type = match.lastgroup
                token_value = match.group(token_type)
                if token_type == INTEGER:
                    token_value = int(token_value)
                token = Token(token_type, token_value)
                self.tokens.append(token)
                self.pos = match.end()
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                continue

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            self.error()

        return Token(EOF)

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

    def factor(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        else:
            self.error()

    def term(self):
        node = self.factor()

        while self.current_token.type in (MULTIPLY, DIVIDE):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(left=node, op=token, right=self.term())

        return node

    def print_tree(self, node, level=0):
        if isinstance(node, Num):
            print("  " * level + repr(node))
        elif isinstance(node, BinOp):
            print("  " * level + repr(node.op))
            self.print_tree(node.left, level + 1)
            self.print_tree(node.right, level + 1)

class NodeVisitor:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIVIDE:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.expr()
        return self.visit(tree)





