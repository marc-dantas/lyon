from re import match
from unittest.util import three_way_cmp
from .errs import ARG_SYNTAX_ERR, EXPR_ERR
from .util import throw
from re import fullmatch


class String:
    
    SYNTAX = r'"([^"]*)"'
    
    def __init__(self, value) -> None:
        self._value = value
    
    @staticmethod
    def is_string(val: object) -> bool:
        return fullmatch(String.SYNTAX, val) is not None
    
    def get_value(self) -> str:
        if m := match(String.SYNTAX, self._value):
            return m.groups()[0]
        throw(ARG_SYNTAX_ERR, '(string parsing)')
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
        return fullmatch(Number.SYNTAX, value) is not None


class Expr:
    
    SYNTAX = r'(.+)(\s+)?(>|<|=|!=|>=|<=)(\s+)?(.+)'
    
    def __init__(self, value: str) -> None:
        self._value = value
    
    def get_value(self) -> object:
        return self.evaluate()
           
    def evaluate(self) -> bool:
        return ExpressionParser().evaluate(self._value)

    @staticmethod
    def is_expression(value: str) -> bool:
        return fullmatch(Expr.SYNTAX, value) is not None
    

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
            return 1 if left == right else 0
        except Exception:
            throw(EXPR_ERR)
            return 0
        
    def ne(self, left: object, right: object) -> bool:
        try:
            return 1 if left != right else 0
        except Exception:
            throw(EXPR_ERR)
            return 0
        
    def lt(self, left: object, right: object) -> bool:
        try:
            return 1 if left < right else 0
        except Exception:
            throw(EXPR_ERR)
            return 0
        
    def gt(self, left: object, right: object) -> bool:
        try:
            return 1 if left > right else 0
        except Exception:
            throw(EXPR_ERR)
            return 0
        
    def le(self, left: object, right: object) -> bool:
        try:
            return 1 if left <= right else 0
        except Exception:
            throw(EXPR_ERR)
            return 0

    def ge(self, left: object, right: object) -> bool:
        try:
            return 1 if left >= right else 0
        except Exception:
            throw(EXPR_ERR)
            return 0
        
    def evaluate(self, expr: str) -> bool:
        left, right, op = self.tokenize_expr(expr)
        # TODO: Make this better (TEMPORARY)
        if not all([left, right, op]):
            throw(EXPR_ERR)
            return 0
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
        return 1

    def tokenize_expr(self, expr: str) -> tuple[str, str, str]:
        if not expr:
            return ('', '', '')
        for op, regex in OPERATORS.items():
            if (regexp := match(regex, expr)):
                left, right = regexp.groups()[0], regexp.groups()[4]
                return (left, right, op)
        return ('', '', '')
