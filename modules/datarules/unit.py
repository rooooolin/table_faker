from .base import BaseDataRule
from modules.registry import DATARULES


@DATARULES.register_module
class UNIT(BaseDataRule):
    def __init__(self, **kwds) -> None:
        super().__init__()
        pass

    def run(self,**kwds):
        return '元'