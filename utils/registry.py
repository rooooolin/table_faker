
import inspect
from collections import defaultdict

class Registry(object):

    def __init__(self, name):
        self._name = name
        self._module_dict = dict()

    def __repr__(self):
        format_str = self.__class__.__name__ + '(name={}, items={})'.format(
            self._name, list(self._module_dict.keys()))
        return format_str

    @property
    def name(self):
        return self._name

    @property
    def module_dict(self):
        return self._module_dict

    def get(self, key):
        return self._module_dict.get(key, None)

    def _register_module(self, module_class):
        """Register a module.

        Args:
            module (:obj:`nn.Module`): Module to be registered.
        """
        if not inspect.isclass(module_class):
            raise TypeError('module must be a class, but got {}'.format(
                type(module_class)))
        module_name = module_class.__name__
        if module_name in self._module_dict:
            raise KeyError('{} is already registered in {}'.format(
                module_name, self.name))
        self._module_dict[module_name] = module_class

    def register_module(self, cls):
        self._register_module(cls)
        return cls
    
def build_from_cfg(cfg, registry):
    assert isinstance(cfg, dict) and 'class_' in cfg
    args = cfg.copy()
    obj_type = args.pop('class_')
    if isinstance(obj_type, str):
        aa=obj_type
        obj_type = registry.get(obj_type)
        if obj_type is None:
            raise KeyError('{} is not in the {} registry'.format(
                obj_type, registry.name))
    elif not inspect.isclass(obj_type):
        raise TypeError('type must be a str or valid type, but got {}'.format(
            type(obj_type)))
    
    return obj_type(**args)

def build(cfg, registry):
    if isinstance(cfg, list):
        modules= defaultdict(list)
        for cfg_ in cfg:
            modules[cfg_['name']]=build_from_cfg(cfg_, registry)
            
        return modules
    else:
        return build_from_cfg(cfg, registry)