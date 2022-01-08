class CommandToken:
    
    def __init__(self, type: object, value: object) -> None:
        super().__init__()
        self._type = type
        self._value = value

    @property
    def type(self) -> object:
        return self._type

    @property
    def value(self) -> object:
        return self._value

    def __str__(self) -> str:
        return f'{self.type}.{self.value}'


