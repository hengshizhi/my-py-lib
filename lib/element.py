from abc import ABC,abstractmethod

class element(ABC):
    length = 8
    @abstractmethod
    def __init__(self, data:bytes) -> None:
        self._data = data
    @abstractmethod
    def get_data(self) -> bytes:
        return self._data
    @abstractmethod
    def __bytes__(self) -> bytes:
        return self._data
    @abstractmethod
    def __str__(self) -> str:
        return str(self._data)
    def __len__(self) -> int:
        return self.length
    def __repr__(self) -> str:
        return str(self._data)
    