import abc

from tempora import schedule


class IScheduler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute_every(self, period, func): ...

    @abc.abstractmethod
    def execute_at(self, when, func): ...

    @abc.abstractmethod
    def execute_after(self, delay, func): ...

    @abc.abstractmethod
    def run_pending(self): ...


class DefaultScheduler(schedule.InvokeScheduler, IScheduler, metaclass=abc.ABCMeta):
    def execute_every(self, period, func) -> None: ...

    def execute_at(self, when, func) -> None: ...

    def execute_after(self, delay, func) -> None: ...
