from .base import BaseDataRule
from modules.registry import DATARULES
import random

@DATARULES.register_module
class COMPANYNAME(BaseDataRule):
    def __init__(self, **kwds) -> None:
        super().__init__()
        pass
    
    def run(self,**kwds):
        return self.faker.company()