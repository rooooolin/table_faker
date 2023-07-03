from .base import BaseDataRule
from modules.registry import DATARULES
import random
from datetime import datetime, timedelta

@DATARULES.register_module
class INVOICEDATE(BaseDataRule):
    ''' the customized rules of InvoiceDate: 
        1) later than OrderDate
        2) 60% that it will be later than the orderdate within 30 days
        2) 30% that it will be later than the orderdate between 30 and 180 days
        2) 10% that it will be later than the orderdate between 180 and 365 days
        '''
    def __init__(self, **kwds) -> None:
        super().__init__()
        self.seconds_one_day = 86400

    def second_delta(self, r):
        if r < 0.6:
            return 0, 30*86400
        elif r > 0.1:
            return 180*86400, 365*86400
        else:
            return 30*86400, 180*86400
        
    def run(self,**kwds):
        fsv = kwds['fsv']
        index = kwds['index']
        order_date=fsv['PurchaseOrder']['OrderDate'][index]
        order_date = datetime.strptime(order_date, "%Y-%m-%d %H:%M:%S")
        delta = random.randint(*self.second_delta(random.random()))
        invoice_date = (order_date + timedelta(seconds=delta)).strftime("%Y-%m-%d %H:%M:%S")
        
        return invoice_date