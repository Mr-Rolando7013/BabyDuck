import antlr4
from baby_duckLexer import baby_duckLexer
from baby_duckParser import baby_duckParser

# Provide your input here
input_string = "..."  # Replace '...' with your input string

# Create an input stream from the input string
input_stream = antlr4.InputStream(input_string)

# Create a lexer using the input stream
lexer = baby_duckLexer(input_stream)

# Create a token stream from the lexer
token_stream = antlr4.CommonTokenStream(lexer)

# Create a parser from the token stream
parser = baby_duckParser(token_stream)

# Start parsing from the top-level rule
tree = parser.programRule()  # Replace 'programRule' with your start rule

# Optionally, perform further processing on the parse tree
# visitor = YourVisitorClass()
# result = visitor.visit(tree)

# Print the parse tree (for debugging)
print(tree.toStringTree(parser))
