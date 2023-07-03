from .base import BaseDataRule
from modules.registry import DATARULES
import random

@DATARULES.register_module
class PRICE(BaseDataRule):
    '''price of related products'''
    def __init__(self, **kwds) -> None:
        super().__init__()
        self.device2price = {'手机':(3000,10000), '电脑':(5000,20000), '平板':(2000,5000), '耳机':(50,1000), '相机':(1000,20000), '路由器':(100,1000), '音箱':(100,2000), '手表':(50,1000), '游戏机':(50,10000), '显示器':(200,20000)}
    
    def run(self,**kwds):
        hg = kwds['hg']
        product_name = hg['ProductName']
        device = product_name.split()[-1]
        
        low,high = self.device2price[device]
        return round(random.uniform(low, high), 2)