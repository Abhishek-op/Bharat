
from parser import *
import sys
import os
import datetime
import random
from math import sin, cos, tan, asin, acos, atan, sinh, cosh, tanh ,ceil, floor, sqrt, degrees, radians, log
from os.path import exists, dirname, join
from os import getenv
class BharatExecute:
    
    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
        # if result is not None:
        #     print(result)
  
    def walkTree(self, node):
  
        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node
  
        if node is None:
            return None
  
        if node[0] == 'program':
            if node[1] == None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])
        
        if node[0] == 'raw_input':
            return '"' + input() + '"'
            
        if node[0] == 'num_input':
            in_ = self.input_()
            if in_.isdigit():
                return int(in_)
            else:
                return 0
            
        if node[0] == 'num':
            return node[1]
        if node[0] == 'str':
            return node[1]
        if node[0] == 'bool':
            return node[1]
        if node[0] == 'arr':
            temp = []
            for e in node[1]:
                temp.append(self.walkTree(e))
            return temp

        if node[0] == 'block':
            for e in node[1]:
                self.walkTree(e)
        if node[0] == 'addstr':
            return str(self.walkTree(node[1])) + str(self.walkTree(node[2]))
        if node[0] == 'add':
            return self.walkTree(node[1]) + self.walkTree(node[2])
        elif node[0] == 'sub':
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == 'not':
            return not(self.walkTree(node[1]))
        elif node[0] == 'andalso':
            return self.walkTree(node[1]) and self.walkTree(node[2])
        if node[0] == 'if_stmt':
            result = self.walkTree(node[1])
            if result:
                return self.walkTree(node[2])
            if node[3]:
                return self.walkTree(node[3])
        if node[0] == 'if_stmt1':
            result = self.walkTree(node[1])
            if result:
            	return self.walkTree(node[2])
        if node[0] == 'if_stmt2':
            result = self.walkTree(node[1])
            if result:
                return self.walkTree(node[2])
            elif node[3]:
                return self.walkTree(node[4])
            if node[5]:
                return self.walkTree(node[5])
        elif node[0] == 'return':
                result = self.walkTree(node[1])
                self.should_return = True
                return result
        if node[0] == 'while':
            condition = self.walkTree(node[1])
            while condition:
                res = self.walkTree(node[2])
                print(res)
                return res
        if node[0] == 'condition_eqeq':
            return self.walkTree(node[1]) == self.walkTree(node[2])
        if node[0] == 'NOT_EQEQ':
            return self.walkTree(node[1]) != self.walkTree(node[2])
        if node[0] == 'LESS':
            return self.walkTree(node[1]) < self.walkTree(node[2])
        if node[0] == 'GREATER':
            return self.walkTree(node[1]) > self.walkTree(node[2])
        if node[0] == 'NOT':
            return not self.walkTree(node[1])
        if node[0] == 'AND':
            return self.walkTree(node[1]) & self.walkTree(node[2])
        if node[0] == 'OR':
            return self.walkTree(node[1]) | self.walkTree(node[2])
        if node[0] == 'EQ_GREATER':
            return self.walkTree(node[1]) == self.walkTree(node[2])
        if node[0] == 'EQ_LESS':
            return self.walkTree(node[1]) == self.walkTree(node[2])
      
       
        if node[0] == 'condition_shomarande':
            return self.walkTree(node[2]) % self.walkTree(node[1]) == 0
        
        if node[0] == 'fun_def':
            self.env[node[1]] = node[2]
        if node[0] == 'fun_call':
            try:
                return self.walkTree(self.env[node[1]])
            except LookupError:
                print(f'undefined function \'{node[1]}\'')
                return 0
 
        if node[0] == 'class_def':
            self.env[node[1]] = node[2]
        if node[0] == 'obj':
            return self.walkTree(node[1]).str(self.walkTree(node[2]))
        if node[0] == 'class_call':
            try:
                return self.walkTree(self.env[node[1]])
            except LookupError:
                return 0
        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]
        if node[0] == 'print':
            print(self.walkTree(node[1]))
            return
        if node[0] == 'index':
            array = self.walkTree(node[1])
            index = self.walkTree(node[2])
            return array[index]
        if node[0] == 'printti':
            result = datetime.datetime.now()
            print(result)
            return result   
        
        if node[0] == 'time':
            result = datetime.datetime.now()
            print(result)
            return result
        if node[0] == 'type':
            result = type(self.walkTree(node[1]))
            return result
        if node[0] == 'randomrange':
            result = random.randrange(self.walkTree(node[1]), self.walkTree(node[2]))
            return result

        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print("अपरिभाषित वैरिएबल '"+node[1]+"' मिला")
                return 0 

if __name__ == '__main__':
    lexer = BharatLexer()
    parser = BharatParser()
    env = {}
    if len(sys.argv) < 2:
        while True:
            try:
                terminal = input('भाऱत >>>')

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