class ERROR(Exception):
    def __init__(self, message):
        self.message = message

class NoFileProvided(ERROR):
    def __init__(self):
        self.message = "No File Name Provided"
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class UnknownArgumentProvided(ERROR):
    def __init__(self, command):
        self.message = "Unknown Argument Supplied"
        self.com = command
        super().__init__(self.message)
    def __str__(self):
        return f'''{self.message} -> '{self.com}' '''
    
class UnknownParameterProvided(ERROR):
    def __init__(self, command, param):
        self.message = "Unknown Parameter Supplied for command"
        self.com = command
        self.param = param
        super().__init__(self.message)
    def __str__(self):
        return f'''{self.message} {self.com} -> '{self.param}' '''
    
class UnknownTokenInFile(ERROR):
    def __init__(self, tok, file):
        self.message = "Unknown Token Supplied in file"
        self.tok = tok
        self.file = file
        super().__init__(self.message)
    def __str__(self):
        return f'''{self.message} {self.file} -> '{self.tok}' '''
    
class UnhandeledStack(ERROR):
    def __init__(self, stack, name):
        self.message = "Unhandled Stack in stack"
        self.stack = stack
        self.name = name
        super().__init__(self.message)
    def __str__(self):
        return f'''{self.message} {self.name}, values left: {len(self.stack)}'''
    
class NotEnoughOnStack(ERROR):
    def __init__(self):
        self.message = "Not Enough things on Stack to remove"
        super().__init__(self.message)
    def __str__(self):
        return f'''{self.message}.'''
    
class NotANumericString(ERROR):
    def __init__(self, string):
        self.message = "Not A Numeric String"
        self.string = string
        super().__init__(self.message)
    def __str__(self):
        return f'''{self.message}. '{self.string}' '''
    
class TestError(ERROR):
    def __init__(self):
        self.message = ""
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'