# sys
import typing as t

# project
from .init import InitApp

__version__ = '1.0.0rc'


def manager(
        app: t.Optional['FastAPI'],
        setting: t.Any,
        extends: t.Optional[list] = None
):
    """ Simple initialization

    :param app: FastAPI instantiates the object
    :param setting: Any object that can be executed by getattr
    :param extends: A list of functions in a fixed format
    """
    with InitApp(app, setting) as a:
        for extend in extends:
            extend(a)
    return app
