from .errs import ARG_SYNTAX_ERR, EXPR_ERR
from .util import throw
from re import fullmatch


class Type:
    
    SYNTAX = r'.+'

    def __init__(self, value: object) -> None:
        self._value = value
        
    def get_value(self):
        return self._value
    
    @staticmethod
    def match_syntax(value: str) -> bool:
        return fullmatch(Type.SYNTAX, value) is not None


class String(Type):
    
    SYNTAX = r'"([^"]*)"'
    
    def __init__(self, value) -> None:
        self._value = value
    
    @staticmethod
    def match_syntax(val: object) -> bool:
        return fullmatch(String.SYNTAX, val) is not None
    
    def get_value(self) -> str:
        if m := fullmatch(String.SYNTAX, self._value):
            return m.groups()[0]
        throw(ARG_SYNTAX_ERR, '(string parsing)', 'Invalid string syntax.')
        return ''
    
    def __repr__(self) -> str:
        return self.val
    
    def __str__(self) -> str:
        return self.val
    

class Number:
    
    SYNTAX = r'[+-]?\d+(?:\.\d+)?'
    
    def __init__(self, value: object) -> None:
        self._value = float(value) if self.match_syntax(value) else 0.0
    
    def get_value(self) -> object:
        return self._value
    
    @staticmethod
    def match_syntax(value: str) -> bool:
        return fullmatch(Number.SYNTAX, value) is not None
