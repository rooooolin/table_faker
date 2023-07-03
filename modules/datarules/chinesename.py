from .base import BaseDataRule
import random
from modules.registry import DATARULES

@DATARULES.register_module
class CHINESENAME(BaseDataRule):
    def __init__(self,**kwds) -> None:
        super().__init__()
        pass

    def run(self,**kwds):
        return self.faker.name()