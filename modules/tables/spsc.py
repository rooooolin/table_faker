from modules.registry import TABLES
from .base import BaseTable

@TABLES.register_module
class SPSC(BaseTable):
    def __init__(self,**table) -> None:
        self.table = table
        super().__init__(**self.table)
        pass