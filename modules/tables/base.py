
from typing import Any
from loguru import logger
from collections import defaultdict

class BaseTable:
    def __init__(self, **table) -> None:
        self.table = table
        dt = defaultdict(list)
        et = None
        for field, val in self.table['fields'].items():
            if isinstance(val, list):
                tn = val[1]
                pi = self.get_index(val,'primary')
                if not pi:
                    dt[tn].append(field)
                elif pi ==  2:et= tn
        dt = dict(dt)
        self.table.update({'et':et,'dt':dt})
        msg = f"{self.table['name']}[{','.join(list(self.table['fields'].keys()))}]"
        if et:
            msg='('+msg+'<->'+str(et)+')'
        if dt:
            msg+='->('
            for tn,fs in dt.items():
                msg+=f"{tn}[{','.join(fs)}],"
            msg=(msg.strip(',')+")")
        logger.info(msg)
        
    def get_index(self,_list,key):
        if key in _list:
            return _list.index(key)
        else:
            return None
            
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.run(*args, **kwds)

    def run(self,*args, **kwds):
        pass
