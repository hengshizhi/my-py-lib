from lib.stapi import st

class element():
    length = 8
    def __init__(self, data:bytes) -> None:
        self._data = data
    def get_data(self) -> bytes:
        return self._data
    def __bytes__(self) -> bytes:
        return self._data
    def __str__(self) -> str:
        return str(self._data)
    def __len__(self) -> int:
        return self.length
    def __repr__(self) -> str:
        return str(self._data)
    
a = st(dict(),element)
print(a.get(b'iuhdu'))
a.put(b'iuhdu',element(b'hubueuu'))
print(a.get(b'iuhdu'))