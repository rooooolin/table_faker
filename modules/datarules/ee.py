
from .base import BaseDataRule
from modules.registry import DATARULES
import random

@DATARULES.register_module
class EE(BaseDataRule):
    def __init__(self, **kwds) -> None:
        super().__init__()
        pass

    def generate_random_products(self):
        device_words = ['手机', '电脑', '平板', '耳机', '相机', '路由器', '音箱', '手表', '游戏机', '显示器']
        company_name = ['苹果', '华为', '小米', '联想','索尼', '戴尔', '谷歌', '惠普', '夏普', 'LG']
        return random.choice(company_name) + ' '+ random.choice(device_words)
    
    def run(self,**kwds):
        return self.generate_random_products()