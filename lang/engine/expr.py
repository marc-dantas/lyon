from .memory import Num
from .data_models import *
from re import match

STR, NUM = (String.SYNTAX, Number.SYNTAX)

OPERATORS = {
    # TODO: Add more operators and improve the regexes
    '=': rf'({STR}|{NUM})(\s+)?\=(\s+)?({STR}|{NUM})',
    '!=': rf'({STR}|{NUM})(\s+)?\!\=(\s+)?({STR}|{NUM})',
    '>': rf'({STR}|{NUM})(\s+)?>(\s+)?({STR}|{NUM})',
    '<': rf'({STR}|{NUM})(\s+)?<(\s+)?({STR}|{NUM})',
    '>=': rf'({STR}|{NUM})(\s+)?>\=(\s+)?({STR}|{NUM})',
    '<=': rf'({STR}|{NUM})(\s+)?<\=(\s+)?({STR}|{NUM})',
}


class ExpressionParser:
    
    def eq(self, left: object, right: object) -> bool:
        try:
            return left == right
        except Exception:
           return False
        
    def ne(self, left: object, right: object) -> bool:
        try:
            return left != right
        except Exception:
            return False
        
    def lt(self, left: object, right: object) -> bool:
        try:
            return left < right
        except Exception:
            return False
        
    def gt(self, left: object, right: object) -> bool:
        try:
            return left > right
        except Exception:
            return False
        
    def le(self, left: object, right: object) -> bool:
        try:
            return left <= right
        except Exception:
            return False
        
    def ge(self, left: object, right: object) -> bool:
        try:
            return left >= right
        except Exception:
            return False
        
    def evaluate(self, expr: str) -> bool:
        left, right, op = self.tokenize_expr(expr)
        # TODO: Make this better (TEMPORARY)
        if not all([left, right, op]):
            return False
        if op == '=':
            return self.eq(left, right)
        elif op == '!=':
            return self.ne(left, right)
        elif op == '>':
            return self.gt(left, right)
        elif op == '<':
            return self.lt(left, right)
        elif op == '<=':
            return self.le(left, right)
        elif op == '>=':
            return self.ge(left, right)
        return True

    def tokenize_expr(self, expr: str) -> tuple[str, str, str]:
        if not expr:
            return ('', '', '')
        for op, regex in OPERATORS.items():
            if (regexp := match(regex, expr)):
                left, right = regexp.groups()[0], regexp.groups()[4]
                return (left, right, op)
        return ('', '', '')


class ConditionalExpression:
    
    def __init__(self, string: str) -> None:
        self._string = string
    
    @property
    def string(self) -> str:
        return self._string        

    def evaluate(self) -> bool:
        return ExpressionParser().evaluate(self._string)
    
    def __repr__(self) -> str:
        return self._string
    
    def __str__(self) -> str:
        return self._string
