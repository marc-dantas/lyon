from re import match
from .errs import ARG_SYNTAX_ERR, INVALID_ARG
from .util import throw


class String:
    
    SYNTAX = r'"(.+)"'
    
    def __init__(self, value) -> None:
        self._value = value
    
    @staticmethod
    def is_string(val: object) -> bool:
        return match(String.SYNTAX, val) is not None
    
    def get_value(self) -> str:
        if m := match(String.SYNTAX, self._value):
            return m.groups()[0]
        throw(ARG_SYNTAX_ERR, 'run (string parsing)')
        return ''
    
    def __repr__(self) -> str:
        return self.val
    
    def __str__(self) -> str:
        return self.val
    

class Number:
    
    SYNTAX = r'[+-]?\d+(?:\.\d+)?'
    
    def __init__(self, number: object) -> None:
        self._value = float(number) if self.is_number(number) else 0.0
    
    def get_value(self) -> object:
        return self._value
    
    @staticmethod
    def is_number(value: str) -> bool:
        return match(Number.SYNTAX, value) is not None
