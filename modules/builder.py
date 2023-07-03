from utils import build
from .registry import (TABLES, DATARULES)





def build_table(cfg):
    return build(cfg, TABLES)

def build_datarule(cfg):
    return build(cfg, DATARULES)
