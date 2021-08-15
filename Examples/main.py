from Bharat.bharat_lexer import BharatLexer
from Bharat.bharat_parser import BharatParser
from Bharat.bharat_interpreter import Process
import sys
import os


def repl():
    lexer = BharatLexer()
    parser = BharatParser()
    env = {}
    program = Process((), env=env)
    while True:
        try:
            text = input('भाऱत >>> ')
            if text in ("exit", "निकले"):
                    print('धन्यवाद')
                    break
        except KeyboardInterrupt:
            break
        except EOFError:
            break
        if text:
            tokens = lexer.tokenize(text)

            try:
                tree = parser.parse(tokens)
                program.tree = tree
                program.run()
            except TypeError as e:
                if str(e).startswith("'NoneType' आब्जेक्ट iterable नही है"):
                    print("सिन्टैक्स इरर")
                else:
                    print(e)


def exec_file():
    lexer = BharatLexer()
    parser = BharatParser()
    if not os.path.exists(sys.argv[1]):
            print("यह फ़ाइल मौजूद नहीं है")
            sys.exit(1)
    if os.path.isdir(sys.argv[1]):
            print("यह एक फ़ोल्डर है, फ़ाइल नहीं")
            sys.exit(1)
    else:
        with open(sys.argv[1]) as opened_file:
        	tokens = lexer.tokenize(opened_file.read())
        	tree = parser.parse(tokens)
        	program = Process(tree)
        	program.run()
        # print(program.env)



if __name__ == "__main__":
    if len(sys.argv) == 1:
        repl()
    else:
        exec_file()
