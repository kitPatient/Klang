import sys
from Errors import *


IotaDex = -1
def IOTA():
    global IotaDex
    IotaDex = IotaDex+1
    return IotaDex

#TYPES
INT = IOTA()
FLOAT = IOTA()
STRING = IOTA()

#OPERATORS
ADD = IOTA()
MINUS = IOTA()
MULTIPLY = IOTA()
DIVIDE = IOTA()
POWER = IOTA()

#STACK MANIPULATION
DUMP = IOTA()
TRASH = IOTA()
CLOSE = IOTA()
SWAP = IOTA()
DUPE = IOTA()
TWODUPE = IOTA()
STRINGTONUMBER = IOTA()
NUMBERTOSTRING = IOTA()

#STACK SWITCHING
STACKSTRING = IOTA()
STACKNUMBER = IOTA()

def isFloat(value):
    try:
        float(value)
        return True
    except:
        return False
    
def isInt(value):
    try:
        int(value)
        return True
    except:
        return False
    
def needInStack(stack , number):
    if len(stack) <= (number-1):
        raise NotEnoughOnStack()
    
def _help():
    print("--HelpingMode--")
    
def _sim(file):
    print("simulating mode with file name: %s" % file)
    print("----------------")
    print("\n")
    
    contents = open(file, "r")
    readContents = contents.read()
    contents.close()
    data = readContents.split()
    
    tokens = []
    NUMstack = []
    STRINGstack = []
    CURRENTstack = NUMstack
    
    
    for word in data:
        try: word = int(word) 
        except ValueError:pass
        try: word = float(word) 
        except ValueError:pass
        
        #TYPES
        if isinstance(word, int):
            tokens.append((INT,word))
        elif isinstance(word, float):
            tokens.append((FLOAT,word))
        elif (word.startswith('''"''') and word.endswith('''"''')):
            tokens.append((STRING,word))

        #OPERATORS
        elif word == "+":
            tokens.append((ADD,word))
        elif word == "-":
            tokens.append((MINUS,word))
        elif word == "*":
            tokens.append((MULTIPLY,word))
        elif word == "/":
            tokens.append((DIVIDE,word))
        elif word == "^":
            tokens.append((POWER,word))
            
        #STACK MANIPULATION
        elif word == ".":
            tokens.append((DUMP,word))
        elif word == "$":
            tokens.append((TRASH,word))
        elif word == "close":
            tokens.append((CLOSE,word))
        elif word == "swap":
            tokens.append((SWAP,word))
        elif word == "dup":
            tokens.append((DUPE,word))
        elif word == "2dup":
            tokens.append((TWODUPE,word))
        elif word == "n-s":
            tokens.append((NUMBERTOSTRING,word))
        elif word == "s-n":
            tokens.append((STRINGTONUMBER,word))
        
        #STACK SWITCHING
        elif word == "-s":
            tokens.append((STACKSTRING,word))
        elif word == "-n":
            tokens.append((STACKNUMBER,word))
            
        #ERROR
        else: raise UnknownTokenInFile(word, file)
        
        
    for token in tokens:
        tok = token[0]
            
        #TYPES
        if tok == INT:
            NUMstack.append(token[1])
        elif tok == FLOAT:
            NUMstack.append(token[1])
        elif tok == STRING:
            STRINGstack.append(token[1])
                
        #OPERATORS
        elif tok == ADD:
            needInStack(CURRENTstack,2)
            a = CURRENTstack.pop()
            b = CURRENTstack.pop()
            CURRENTstack.append(b+a)
        elif tok == MINUS:
            needInStack(CURRENTstack,2)
            a = CURRENTstack.pop()
            b = CURRENTstack.pop()
            CURRENTstack.append(b-a)
        elif tok == MULTIPLY:
            needInStack(CURRENTstack,2)
            a = CURRENTstack.pop()
            b = CURRENTstack.pop()
            CURRENTstack.append(b*a)
        elif tok == DIVIDE:
            needInStack(CURRENTstack,2)
            a = CURRENTstack.pop()
            b = CURRENTstack.pop()
            CURRENTstack.append(b/a)
        elif tok == POWER:
            needInStack(CURRENTstack,2)
            a = CURRENTstack.pop()
            b = CURRENTstack.pop()
            CURRENTstack.append(b**a)

        #STACK MANIPULATION
        elif tok == DUMP:
            needInStack(CURRENTstack,1)
            a = CURRENTstack.pop()
            if (type(a) == str):
                a = a[1:len(a)-1]
            print(a)  
        elif tok == TRASH:
            needInStack(CURRENTstack,1)
            a = CURRENTstack.pop()
        elif tok == CLOSE:
            CURRENTstack = []
        elif tok == SWAP:
            needInStack(CURRENTstack,2)
            a = CURRENTstack.pop()
            b = CURRENTstack.pop()
            CURRENTstack.append(a)
            CURRENTstack.append(b)
        elif tok == DUPE:
            needInStack(CURRENTstack,1)
            a = CURRENTstack.pop()
            CURRENTstack.append(a)
            CURRENTstack.append(a)
        elif tok == TWODUPE:
            needInStack(CURRENTstack,2)
            a = CURRENTstack.pop()
            b = CURRENTstack.pop()
            CURRENTstack.append(b)
            CURRENTstack.append(a)
            CURRENTstack.append(b)
        elif tok == STRINGTONUMBER:
            needInStack(STRINGstack,1)
            a = STRINGstack.pop()
            a = a[1:len(a)-1] 
            if isInt(a):
                NUMstack.append(int(a))
            elif isFloat(a):
                NUMstack.append(float(a))
            else:
                raise NotANumericString(a) 
        elif tok == NUMBERTOSTRING:
            needInStack(NUMstack,1)
            a = NUMstack.pop()
            STRINGstack.append(f"'{a}'") 
                
        #STACK SWITCHING
        elif tok == STACKSTRING:
            CURRENTstack = STRINGstack
        elif tok == STACKNUMBER:
            CURRENTstack = NUMstack
                
        #ERROR
        else:
            raise UnknownTokenInFile(token, file)
        
        
        
    if len(NUMstack) != 0:
        raise UnhandeledStack(NUMstack,"NUMSTACK")
    if len(STRINGstack) != 0:
        raise UnhandeledStack(STRINGstack, "STRINGSTACK")
        
    print("\n")
    print("----------------")
    print("Successfully Simulated!!")
    exit(1)

def _com(file):
    print("compiling mode with file name: %s" % file)
    
def _dump(file):
    print("dumping mode with file name: %s" % file)
    
def main():
    ARGS = sys.argv
    ARGS.pop(0)
    index = 0
    while index + 1 <= len(ARGS):
        
        subCommand = ARGS[index]
        if subCommand == ("-h" or "help"): 
            _help()
            if index + 1 <= len(ARGS):
                index += 1
        elif subCommand == "sim":
            if index + 1 != len(ARGS):
                if ARGS[index + 1].startswith("-"):
                    raise UnknownParameterProvided(ARGS[index], ARGS[index+1])
                _sim(ARGS[index + 1])
            else:
                raise NoFileProvided()
            
        elif subCommand == "com":
            if index + 1 != len(ARGS):
                if ARGS[index + 1].startswith("-"):
                    raise UnknownParameterProvided(ARGS[index], ARGS[index+1])
                _com(ARGS[index + 1])
            else:
                raise NoFileProvided()
        
            if index + 2 <= len(ARGS):
                index += 2
        elif subCommand == "dump":
            if index + 1 != len(ARGS):
                
                if ARGS[index + 1].startswith("-"):
                    _dump("output.klang")
                    if index + 1 <= len(ARGS):
                        index += 1
                else:
                    _dump(ARGS[index + 1])
                
                    if index + 2 <= len(ARGS):
                        index += 2
            else:
                _dump("output.klang")
                
                if index + 1 <= len(ARGS):
                    index += 2
        else:
            raise UnknownArgumentProvided(subCommand)
    
if __name__  == '__main__':
    main()