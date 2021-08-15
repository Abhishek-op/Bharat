from sly import Lexer


class BharatLexer(Lexer):
    """
    Bharat language Lexer
    """
    tokens = {ID, INT, FLOAT, ASSIGN, STRING, LET,
              IF, ELSE, EQEQ, SEP, NOTEQ, LESS,
              GREATER, LESSEQ, GREATEREQ, NIL, WHILE,
              FOR, FN, RETURN, LAMBDA, ARROW, TRUE, FALSE,
              AND, OR, SHR, SHL, INC, DEC, PLUSASGN,
              MINUSASGN, STARASGN, SLASHASGN, MODULOASGN,
              ANDASGN, ORASGN, XORASGN, SHLASGN, SHRASGN,
              IMPORT, STRUCT, INT_TYPE, FLOAT_TYPE, BOOL_TYPE,
              LIST_TYPE, DICT_TYPE, STRING_TYPE, TYPEOF,
              LEFTARROW, PIPE, CLASS, DOUBLECOLON, PRINT, RAW_INPUT, TO, ADD, SUB, MUL,DIV, PERSENT}
    ignore = ' \t'
    ignore_comment_slash = r'//.*'

    literals = {'=', '+', '-', '/', '*',
                '(', ')', ',', '{', '}',
                '%', '[', ']', '!', '&',
                '|', '^', '?', ':', '~',
                '.'}
    
    INC = r'\+\+'
    DEC = r'--'
    PIPE = r'\|>'
    PLUSASGN = r'\+='
    MINUSASGN = r'-='
    STARASGN = r'\*='
    SLASHASGN = r'/='
    MODULOASGN = r'%='
    ANDASGN = r'&='
    ORASGN = r'\|='
    XORASGN = r'^='
    SHLASGN = r'<<='
    SHRASGN = r'>>='
    ARROW = r'=>'
    LESSEQ = r'<='
    GREATEREQ = r'>='
    LEFTARROW = r'<-'
    SHR = r'>>'
    SHL = r'<<'
    LESS = r'<'
    GREATER = r'>'
    NOTEQ = r'!='
    EQEQ = r'=='
    ASSIGN = r'='
    SEP = r';'
    DOUBLECOLON = r'::'
    PRINT = r'दिखाओ'
    RAW_INPUT = r'इनपुट'
    
    ID = r'[ौैाीूोे्िुॉंँृःमनवलसय़परकतचटडजदगहबऔऐआईऊभघधझढओएअइउफऱखथछठऑणऩळशषञस्ट्रक्टव्यक्ति]+'
    ID['लेट'] = LET
    ID['योग'] = ADD
    ID['घटाना'] = SUB
    ID['गुणा'] = MUL
    ID['प्रतिशत'] = PERSENT
    ID['भाग'] = DIV
    ID['यदि'] = IF
    ID['से'] = TO
    ID['नहीतो'] = ELSE
    ID['शून्य'] = NIL
    ID['जब'] = WHILE
    ID['केलिये'] = FOR
    ID['फंसन'] = FN
    ID['वापस'] = RETURN
    ID['लेम्डा'] = LAMBDA
    ID['सही'] = TRUE
    ID['गलत'] = FALSE
    ID['और'] = AND
    ID['या'] = OR
    ID['इम्पोर्ट'] = IMPORT
    ID['स्ट्रक्ट'] = STRUCT
    ID['इन्ट'] = INT_TYPE
    ID['फ्लोट'] = FLOAT_TYPE
    ID['पंक्ति'] = STRING_TYPE
    
    ID['बूल'] = BOOL_TYPE
    ID['लिस्ट'] = LIST_TYPE
    ID['डिक्ट'] = DICT_TYPE
    ID['प्रकार'] = TYPEOF
    ID['क्लास'] = CLASS
    
    @_(r'#.*', r'//.*.//')
    def COMMENT(self, t):
        pass
        
    @_(r'\d+\.\d+')
    def FLOAT(self, t):
        """
        Parsing float numbers
        """
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def INT(self, t):
        """
        Parsing integers
        """
        t.value = int(t.value)
        return t

    @_(r'\".*?(?<!\\)(\\\\)*\"')
    def STRING(self, t):
        """
        Parsing strings (including escape characters)
        """
        t.value = t.value[1:-1]
        t.value = t.value.replace(r"\n", "\n")
        t.value = t.value.replace(r"\t", "\t")
        t.value = t.value.replace(r"\\", "\\")
        t.value = t.value.replace(r"\"", "\"")
        t.value = t.value.replace(r"\a", "\a")
        t.value = t.value.replace(r"\b", "\b")
        t.value = t.value.replace(r"\r", "\r")
        t.value = t.value.replace(r"\t", "\t")
        t.value = t.value.replace(r"\v", "\v")
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print("पंक्ति %d: विशुद्ध अक्षर %s" % (self.lineno, t.value[0]))
        self.index += 1
        
if __name__ == '__main__':
    data = input()
    lexer = BharatLexer()
    for tok in lexer.tokenize(data):
        print('टाइप=%r, वैल्यू=%r' % (tok.type, tok.value))