from .base import BaseDataRule
from modules.registry import DATARULES
import random


@DATARULES.register_module
class NUMERICAL(BaseDataRule):
    def __init__(self, **kwds) -> None:
        super().__init__()
        pass

    def run(self, **kwds):
        if kwds['_type'].lower() == 'int':
            return random.randint(kwds['low'], kwds['high'])
        elif kwds['_type'].lower() == 'float':
            return round(random.uniform(kwds['low'], kwds['high']), 2)
