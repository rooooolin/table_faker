
from .base import BaseDataRule
from modules.registry import DATARULES
import uuid


@DATARULES.register_module
class UUID(BaseDataRule):
    def __init__(self, **kwds) -> None:
        super().__init__()
        pass

    def run(self,**kwds):
        return str(uuid.uuid1())
