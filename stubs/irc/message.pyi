class Tag:
    @staticmethod
    def parse(item): ...

    @classmethod
    def from_group(cls, group): ...


class Arguments(list):
    @staticmethod
    def from_group(group): ...
