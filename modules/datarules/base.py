

from typing import Any
from faker import Faker

class BaseDataRule:
    def __init__(self) -> None:
        self.faker = Faker('zh_CN')

    def __call__(self, **kwds: Any) -> Any:
        return self.run(**kwds)

    def run(self,**kwds):
        pass