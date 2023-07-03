from .base import BaseDataRule
from modules.registry import DATARULES
import random
from datetime import datetime, timedelta

@DATARULES.register_module
class RANDOMDATE(BaseDataRule):
    def __init__(self, **kwds) -> None:
        super().__init__()
        pass

    def generate_random_date(self):
        start_time = datetime(2022, 1, 1, 0, 0, 0)
        end_time = datetime(2022, 12, 31, 23, 59, 59)
        delta = random.randint(
                0, int((end_time - start_time).total_seconds()))
        date = (
                start_time + timedelta(seconds=delta)).strftime("%Y-%m-%d %H:%M:%S")
        return date
    
    def run(self,**kwds):
        return self.generate_random_date()