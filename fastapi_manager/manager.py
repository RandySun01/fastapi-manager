# sys
import typing as t

# project
from .init import InitApp
from .helper import dynamic_import

# Global Static Configuration
static_setting: t.Any


def manager(
        app: t.Optional['FastAPI'],
        setting: t.Any,
        extends: t.Optional[list] = None
):
    """ Simple initialization.

    :param app: FastAPI instantiates the object
    :param setting: Any object that can be executed by getattr
    :param extends: A list of fixed-format functions
    or a list of strings that can be imported dynamically
    """
    # Obtaining the Configuration Object
    if isinstance(setting, str):
        setting = dynamic_import(setting)

    # static allocation
    global static_setting
    static_setting = setting

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
