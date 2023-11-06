from antlr4 import *
from symbol_table import SymbolTable
from myListener import MyListener
from baby_duckLexer import baby_duckLexer
from baby_duckParser import baby_duckParser

#Directorio de funciones de variables locales y globales
def main():
    symbol_table = SymbolTable()

    input_stream = FileStream("ejemplo.txt")
    lexer = baby_duckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = baby_duckParser(stream)

    tree = parser.programRule()
    listener = MyListener(symbol_table)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()