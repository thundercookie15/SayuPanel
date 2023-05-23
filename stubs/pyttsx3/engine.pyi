from _typeshed import Incomplete
from typing import Literal, overload


class Engine:
    proxy: Incomplete

    def __init__(self, driverName: Incomplete | None = ..., debug: bool = ...) -> None: ...

    def connect(self, topic, cb): ...

    def disconnect(self, token) -> None: ...

    def say(self, text: str, name: str | None = ...) -> None: ...

    def stop(self) -> None: ...

    def save_to_file(self, text: str, filename: str, name: str | None = ...) -> None: ...

    def isBusy(self): ...

    @overload
    def getProperty(self, name: Literal['voice']) -> str: ...

    @overload
    def getProperty(self, name: Literal['rate']) -> int: ...

    @overload
    def getProperty(self, name: Literal['volume']) -> float: ...

    @overload
    def setProperty(self, name: Literal['voice'], value: str) -> None: ...

    @overload
    def setProperty(self, name: Literal['rate'], value: int) -> None: ...

    @overload
    def setProperty(self, name: Literal['volume'], value: float) -> None: ...

    def runAndWait(self) -> None: ...

    def startLoop(self, useDriverLoop: bool = ...) -> None: ...

    def endLoop(self) -> None: ...

    def iterate(self) -> None: ...
