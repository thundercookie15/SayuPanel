class DriverProxy:
    def __init__(self, engine, driverName, debug) -> None: ...

    def __del__(self) -> None: ...

    def notify(self, topic, **kwargs) -> None: ...

    def setBusy(self, busy) -> None: ...

    def isBusy(self): ...

    def say(self, text, name) -> None: ...

    def stop(self) -> None: ...

    def save_to_file(self, text, filename, name) -> None: ...

    def getProperty(self, name): ...

    def setProperty(self, name, value) -> None: ...

    def runAndWait(self) -> None: ...

    def startLoop(self, useDriverLoop) -> None: ...

    def endLoop(self, useDriverLoop) -> None: ...

    def iterate(self) -> None: ...
