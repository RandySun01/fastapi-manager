# sys
import typing as t


class SettingCore:
    """ Fastapi extended configuration.

    You can omit the configuration as long as
     the Routers and MiddleWare variables are
     configured in the configuration object.
    """

    # Fastapi Indicates the module corresponding to the route
    Router: list = []

    # Fastapi middleware and its parameters
    MiddleWare: t.Dict[str, t.Any] = {}

    # If you are not using extend.Logger,
    # you do not need to define these configurations
    IgnoreLogger: list
    LogLevel: int
    LogFormatter: str

    class Meta:
        path: str

    def __init__(self):
        path = getattr(self.Meta, 'path')
        if path:
            conf = self._load_conf(path)

    def _load_conf(self, path: str) -> dict:
        """ Load the configuration file configuration
        """
        pass
