# Memory module for lyon.
from .errs import CMP_ERR, INVALID_ARG, VAR_ERR
from .util import throw
    

class MemoryObject:
    
    def __init__(self) -> None:
        self._value: str = '"None"'

    @property
    def value(self) -> object:
        return self._value

    def set(self, value: object) -> None:
        self._value = value

    def clear(self) -> None:
        self._value = '"None"'

    @property
    def repr(self) -> str:
        return '@OBJECT'


class Space(MemoryObject):

    def __init__(self) -> None:
        self._value: str = '"None"'

    @property
    def value(self) -> object:
        return self._value

    def set(self, value: object) -> None:
        self._value = value

    def clear(self) -> None:
        self._value = '"None"'

    @property
    def repr(self) -> str:
        return '@SPACE'


class Param(MemoryObject):
    
    def __init__(self) -> None:
        self._value: str = '"None"'

    @property
    def value(self) -> object:
        return self._value

    def set(self, value: object) -> None:
        self._value = value

    def clear(self) -> None:
        self._value = '"None"'

    @property
    def repr(self) -> str:
        return '@PARAM'


class Num(MemoryObject):

    def __init__(self) -> None:
        self._value = 0.0

    @property
    def value(self) -> float:
        return self._value

    @staticmethod
    def is_number(val: object) -> bool:
        return str(val).replace('.', '', 1).isdigit()

    def check_number(self, val: object, cmd_name: str) -> float:
        if self.is_number(val):
            return float(val)
        throw(INVALID_ARG, cmd_name)
        return 0.0

    def add(self, val: float) -> None:
        self._value += self.check_number(val, 'add')

    def sub(self, val: float) -> None:
        self._value -= self.check_number(val, 'sub')

    def mul(self, val: float) -> None:
        self._value *= self.check_number(val, 'mul')

    def div(self, val: float) -> None:
        self._value /= self.check_number(val, 'div')

    def clear(self) -> None:
        self._value = 0.0

    @property
    def repr(self) -> str:
        return '@NUM'


class Cmp(MemoryObject):
    
    def __init__(self) -> None:
        self._left = ''
        self._right = ''

    @property
    def value(self) -> object:
        return self._value

    def set(self, value: int) -> None:
        if not self._left:
            self._left = value
        elif not self._right:
            self._right = value
        else:
            throw(CMP_ERR, 'setcmp', 'Too many comparison values.')
    
    def compare(self, op: str) -> int:
        if not self._left or not self._right:
            return 0
        match op:
            case 'eq':
                return self._left == self._right
            case 'ne':
                return self._left != self._right
            case 'lt':
                return self._left < self._right
            case 'gt':
                return self._left > self._right
            case 'le':
                return self._left <= self._right
            case 'ge':
                return self._left >= self._right
            case _:
                throw(CMP_ERR, message='Invalid Operator')
                return 0
    
    def get_values(self) -> tuple:
        return (self._left, self._right)

    def clear(self) -> None:
        self._left = ''
        self._right = ''


class Var(MemoryObject):

    def __init__(self) -> None:
        self._var: dict = {}
        self._last_var: str = ""

    def new(self, name: str) -> None:
        self._var[name] = '"None"'
        self._last_var = name

    def set(self, value: object) -> None:
        if self._last_var:
            self._var[self._last_var] = value
        else:
            throw(VAR_ERR, 'val')

    def get(self, key: str) -> object:
        return self._var.get(key, "None")

    def clear(self) -> None:
        self._var = {}
        self._last_var = ""

    def __str__(self) -> str:
        return str(self._var)
