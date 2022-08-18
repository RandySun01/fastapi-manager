# sys
import typing as t


class SettingBasic:
    """ Fastapi extended configuration.

    You can omit the configuration as long as
     the Routers and MiddleWare variables are
     configured in the configuration object.
    """

    # Fastapi Indicates the module corresponding to the route
    Router: list

    # Fastapi middleware and its parameters
    MiddleWare: t.Dict[str, t.Any]

    # If you are not using extend.Logger,
    # you do not need to define these configurations
    IgnoreLogger: list
    LogLevel: int
    LogFormatter: str

    class Meta:
        path: str

    def __init__(self):
        # 获取配置文件地址
        path = getattr(self.Meta, 'path')
        if path:
            # 检查配置文件是否存在

            # 获取配置文件中对应的配置
            conf = self._load_conf(path)

            # 替换默认配置

    def _load_conf(self, path: str) -> dict:
        """ Load the configuration file configuration
        """
        pass
