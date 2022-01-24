# Memory module for lyon.
from .errs import INVALID_ARG, VAR_ERR
from .util import throw


class Space:

    def __init__(self) -> None:
        self._value: str = "None"

    @property
    def value(self) -> object:
        return self._value

    def set(self, value: object) -> None:
        self._value = value

    def clear(self) -> None:
        self._value = "None"

    @property
    def repr(self) -> str:
        return '@SPACE'


class Num:

    def __init__(self) -> None:
        self._num = 0.0

    @property
    def value(self) -> float:
        return self._num

    @staticmethod
    def is_number(val: object) -> bool:
        return val.replace('.', '', 1).isdigit()

    def check_number(self, val: object) -> float:
        if self.is_number(val):
            return float(val)
        throw(INVALID_ARG)
        return 0.0

    def add(self, val: float) -> None:
        self._num += self.check_number(val)

    def sub(self, val: float) -> None:
        self._num -= self.check_number(val)

    def mul(self, val: float) -> None:
        self._num *= self.check_number(val)

    def div(self, val: float) -> None:
        self._num /= self.check_number(val)

    def clear(self) -> None:
        self._num = 0.0

    @property
    def repr(self) -> str:
        return '@NUM'


class Var:

    def __init__(self) -> None:
        self._var: dict = {}
        self._last_var: str = ""

    def new(self, name: str) -> None:
        self._var[name] = "None"
        self._last_var = name

    def set(self, value: object) -> None:
        if not self._last_var or self._last_var != "None":
            self._var[self._last_var] = value
        else:
            throw(VAR_ERR)

    def get(self, key: str) -> object:
        return self._var.get(key, "None")

    def clear(self) -> None:
        self._var = {}
        self._last_var = ""

    def __str__(self) -> str:
        return str(self._var)
