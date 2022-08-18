# sys
import typing as t

# project
from .init import InitApp
from .helper import dynamic_import

__version__ = '1.0.0rc2'


def manager(
        app: t.Optional['FastAPI'],
        setting: t.Any,
        extends: t.Optional[list] = None
):
    """ Simple initialization

    :param app: FastAPI instantiates the object
    :param setting: Any object that can be executed by getattr
    :param extends: A list of fixed-format functions
    or a list of strings that can be imported dynamically
    """
    # Obtaining the Configuration Object
    if isinstance(setting, str):
        setting = dynamic_import(setting)

    # Init
    with InitApp(app, setting) as a:

        # You can use this if you don't want to
        # configure in a configuration object
        for extend in extends or []:
            if isinstance(extend, str):
                extend = dynamic_import(extend)
            if extend:
                extend(a)

    return app
