from .base import BaseDataRule
from modules.registry import DATARULES
import random
from datetime import datetime, timedelta

@DATARULES.register_module
class RECEIPTDATE(BaseDataRule):
    ''' ReceiptDate should later than OrderDate about 3 to 5 days'''
    def __init__(self, **kwds) -> None:
        super().__init__()
        self.seconds_one_day = 86400

    def run(self,**kwds):
        fsv = kwds['fsv']
        index = kwds['index']
        order_date=fsv['PurchaseOrder']['OrderDate'][index]
        order_date = datetime.strptime(order_date, "%Y-%m-%d %H:%M:%S")
        delta = random.randint(3*self.seconds_one_day, 5*self.seconds_one_day)
        receipt_date = (
                order_date + timedelta(seconds=delta)).strftime("%Y-%m-%d %H:%M:%S")
        return receipt_date