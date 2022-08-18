# sys
import importlib


def dynamic_import(import_str: str):
    """ Dynamic import module
    """
    module_str, imported = import_str.rsplit('.', 1)
    module_obj = importlib.import_module(module_str)
    return getattr(module_obj, imported, None)
