import sys
import os
from sly import Parser
from bharat.lexer import BharatLexer
class BharatParser(Parser):
    tokens = BharatLexer.tokens
    debugfile = "parser.out"

    precedence = (
        ('left', '.'),
        ('left', ADD, '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS')
    )

    def __init__(self):
        self.env = {}

    @_('')
    def statement(self, p):
        pass
    @_('expr')
    def statement(self, p):
        return p.expr
    @_('array')
    def statement(self, p):
        return (p.array)

    @_('expr "." expr')
    def expr(self, p):
        return ('addstr', p.expr0, p.expr1)

    @_('expr ADD expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)

    @_('expr "*" expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)

    @_('expr "/" expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)
    

    @_("expr NOT_EQEQ expr")
    def expr(self, p):
        return ("NOT_EQEQ", p.expr0, p.expr1)
    
    @_("expr EQ_LESS expr")
    def expr(self, p):
        return ("EQ_LESS", p.expr0, p.expr1)

    @_("expr EQ_GREATER expr")
    def expr(self, p):
        return ("EQ_GREATER", p.expr0, p.expr1)

    @_("expr OR expr")
    def expr(self, p):
        return ("OR", p.expr0, p.expr1)

    @_("expr AND expr")
    def expr(self, p):
        return ("AND", p.expr0, p.expr1)

    @_("NOT expr")
    def expr(self, p):
        return ("NOT", p.expr)

    @_("expr '<' expr")
    def expr(self, p):
        return ("LESS", p.expr0, p.expr1)

    @_("expr '>' expr")
    def expr(self, p):
        return ("GREATER", p.expr0, p.expr1)

    @_('RAW_INPUT')
    def expr(self, p):
        return ('raw_input',)

    @_('NUM_INPUT')
    def expr(self, p):
        return ('num_input',)

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr

    @_('NAME')
    def expr(self, p):
        return ('var', p.NAME)

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)

    @_('STRING')
    def expr(self, p):
        return ('str', p.STRING)
    @_('FLOAT')
    def expr(self, p):
        return ('float', p.FLOAT)
    

    @_('PRINT expr')
    def expr(self, p):
        return ('print', p.expr)
    
    
    
   

    
    @_('NAME RUN')
    def statement(self, p):
        return ('fun_call', p.NAME)

    @_('expr EQEQ expr')
    def condition(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)

    @_('expr SHOMARANDE expr')
    def condition(self, p):
        return ('condition_shomarande', p.expr0, p.expr1)

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('NAME "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)
    @_('NAME "=" array')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.ARRAY)
    
    
    @_('NAME "=" statement')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.statement)
    @_("WHILE condition statement")
    def statement(self, p):
        return ('while', p.condition, p.statement)

    @_('FOR NAME FROM expr TO expr DO statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', ('var_assign', p.NAME, p.expr0), p.expr1), p.statement)
    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        return ('if_stmt', p.condition, p.statement0, p.statement1)
        
    @_('IF condition THEN statement')
    def statement(self, p):
        return ('if_stmt1', p.condition, p.statement)
        
    @_('IF condition THEN statement ELIF condition THEN statement ELSE statement')
    def statement(self, p):
        return ('if_stmt2', p.condition0, p.condition1, p.statement0, p.statement1, p.statement2)
    
    @_('FUNCTION NAME statement')
    def statement(self, p):
        return ('fun_def', p.NAME, p.statement)
    
    @_('CLASS NAME ":" statement')
    def statement(self, p):
        return ('class_def', p.NAME, p.statement)
    @_('NAME "(" ")"')
    def statement(self, p):
        return ('class_call', p.NAME)
    
    @_('RETURN NAME')
    def var_assign(self, p):
        return ('return', p.NAME)
    
    
        
    @_('TIME')
    def statement(self, p):
    	r = datetime.datetime.now()
    	return r
    	
    @_('PRINT TIME')
    def expr(self, p):
        return ('printti', p.TIME)
        
    @_('BOOLEAN')
    def bool(self, p):
        return ('str', p.BOOLEAN)
    @_('NAME "=" bool')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.bool)
    @_('bool ANDALSO bool')
    def bool(self, p):
        return ('AND', p.bool0, p.bool1)
    
    @_('NOT bool')
    def bool(self, p):
        return ('NOT', p.bool)
        
        
    @_("RANDOMRANGE FROM expr TO expr")
    def expr(self, p):
        return ("randomrange", p.expr0, p.expr1)
    @_('DO statement WHILE condition')
    def statement(self, p):
        return ('while', p.statement, p.condition)
    @_('TYPE NAME')
    def statement(self, p):
        return ('type', p.NAME)
#++++++++++++++++++++++++++
   
    @_('"[" elements "]"')
    def array(self, p):
        return ('arr', p.elements)

    @_('statement')
    def elements(self, p):
        return [p.statement]

    @_('statement "," elements')
    def elements(self, p):
        return [p.statement] + p.elements
    
    @_('NAME')
    def array(self, p):
        return ('var', p.NAME)     
    @_('array "+" array')
    def array(self, p):
        return ('add', p.array0, p.array1)

    @_('array "+" expr')
    def array(self, p):
        return ('add', p.array, p.expr)

    @_('array "+" STRING')
    def array(self, p):
        return ('add', p.array, p.str)
    
    @_('array "[" expr "]"')
    def array(self, p):
        return ('index', p.array, p.expr)

   
        
if __name__ == '__main__':
    lexer = BharatLexer()
    parser = BharatParser()

    while True:
        try:
            text = input('bharat > ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break