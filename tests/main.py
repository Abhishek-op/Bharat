from bharat.interpreter import *
from bharat.lexer import BharatLexer
from bharat.parser import BharatParser
if __name__ == '__main__':
    lexer = BharatLexer()
    parser = BharatParser()
    env = {}
    if len(sys.argv) < 2:
        while True:
            try:
                terminal = input('भाऱत >>> ')

                if terminal in ("exit", "निकले"):
                    print('धन्यवाद')
                    break

                else:
                    tokens = lexer.tokenize(terminal)
                    tree = parser.parse(tokens)
                    BharatExecute(tree, env)
            except EOFError:
                           		pass
    else:
        if not os.path.exists(sys.argv[1]):
            print("यह फ़ाइल मौजूद नहीं है")
            sys.exit(1)
        if os.path.isdir(sys.argv[1]):
            print("यह एक फ़ोल्डर है, फ़ाइल नहीं")
            sys.exit(1)
        with open(sys.argv[1], encoding="utf-8") as fp:
            line = "# somecomment"
            while line:
                try:
                    tokens = lexer.tokenize(line)
                    tree = parser.parse(tokens)
                    BharatExecute(tree, env)
                    line = fp.readline()
                except:
                    print(f"पंक्ति में त्रुटि: " +Line)
                    sys.exit(1)