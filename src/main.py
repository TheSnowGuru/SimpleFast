"""
This file is the entry point of the SimpleFast compiler. It uses the Lexer, Parser, Translator, 
and Compiler classes to compile a .sfast file into an executable.
"""

from lexer import Lexer
from parser import Parser
from translator import Translator
from compiler import Compiler

def compile_sfast_file(filename):
    with open(filename, 'r') as file:
        code = file.read()

    lexer = Lexer()
    tokens = lexer.tokenize(code)

    parser = Parser()
    ast = parser.parse(tokens)

    translator = Translator()
    cpp_code = translator.translate(ast)

    compiler = Compiler()
    compiler.compile(cpp_code)

if __name__ == "__main__":
    # Assume the .sfast file to compile is provided as a command-line argument
    import sys
    filename = sys.argv[1]
    compile_sfast_file(filename)
