from sly import Lexer


class BharatLexer(Lexer):
    tokens = {
        PRINT, 
        RAW_INPUT, 
        NUM_INPUT, 
        RUN,
        NUMBER, 
        STRING, 
        NAME, 
        FUNCTION,
        IF, 
        THEN, 
        ELSE , 
        ELIF,
        DO,
        FROM, 
        SHOMARANDE, 
        STRING, 
        FOR, 
        RANDOMRANGE,
        TO, 
        PRINT,
        TIME, 
        EQEQ,
        EQ_GREATER,
        NOT_EQEQ,
        EQ_LESS,
        WHILE,
        FOR,
        RETURN,
        RETURN,
        TYPE,
        AND,
        OR,
        NOT,
        ANDALSO,
        BOOLEAN,
        ADD,
        SUB,
        MUL,
        DIV,
        CLASS,
        FLOAT
    }
    ignore = '\t '

    literals = {
        "+",
        "-",
        "*",
        "/",
        "%",
        ">",
        "<",
        "=",
        "(",
        ")",
        "{",
        "}",
        ";",
        ",",
        ".",
        ":",
        "[",
        "]",
        ">>>"
        "<<<"
    }

    # Define tokens
    IF = r'यदि'
    WHILE = r'जब'
    THEN = r'तब'
    ELSE = r'नहीतो'
    ELIF = r'नहीतोयदि'
    FROM = r'से'
    DO = r'कर'
    FOR = r'केलिये'
    RUN = r'चलाए'
    TO = r"तक"
    RETURN = r'वापस'
    FUNCTION = r'फंसन'
    RANDOMRANGE = r'क्रमरहितसीमा'
    SHOMARANDE = r'काउन्टर'
    RAW_INPUT = r'इनपुट'
    NUM_INPUT = r'अंकइनपुट'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    TYPE = r'प्रकार'
    TIME = r'समय'
    STRING = r'"(""[a-zA-Z_][a-zA-Z0-9_]*|.)*?"'
    PRINT = r"दिखाओ"
    EQEQ = r"=="
    
    NOT_EQEQ = r"!="
    ADD = r'योग'
    SUB = r'घटाना'
    MUL= r'गुणा'
    DIV = r'भाग'
    ANDALSO = r"औरभी"
    AND = r"और"
    OR = r"या"
    NOT =r"नही"
    CLASS =r"क्लास"
    
    

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t
        
    @_(r'\d+\.\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t
        
    @_(r'(गलत|सही)')
    def BOOLEAN(self, t):
        if t.value == "न":
            t.value = False
        elif t.value == "हा":
            t.value = True
        return t
     
        
    @_(r'#.*', r'//.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')
        
        
    def error(self, t):
        print('पंक्ति %d: विशुद्ध अक्षर %r' % (self.lineno, t.value[0]))
        self.index += 1
        
        
if __name__ == '__main__':
    data = input()
    lexer = BharatLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))