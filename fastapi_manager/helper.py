# sys
import importlib


def dynamic_import(import_str: str):
    """ Dynamic import module
    """
    if '.' in import_str:
        module_str, imported = import_str.rsplit('.', 1)
        module_obj = importlib.import_module(module_str)
        obj = getattr(module_obj, imported, None)
    else:
        obj = importlib.import_module(import_str)
    return obj
