# sys
import os
import typing as t

# 3p
import yaml


class SettingBasic:
    """ Fastapi extended configuration.

    tips:
        - You can omit the configuration as long as
        the Routers and MiddleWare variables are
        configured in the configuration object.

        - This class can only read YAML files.

        - No exceptions are handled and an error is
        reported if the load is not successful.

        - There are no custom exceptions.
    """

    # Fastapi Indicates the module corresponding to the route
    Router: list

    # Fastapi middleware and its parameters
    MiddleWare: t.Dict[str, t.Any]

    # Fastapi third party extension
    Extend: list

    # If you are not using extend.Logger,
    # you do not need to define these configurations
    IgnoreLogger: list
    LogLevel: int
    LogFormatter: str

    class Meta:
        # Configuration file address
        conf_env: str
        path: str

    def __init__(self):
        # The address set by the environment
        # variable has a greater weight than
        # the address set by the path variable.
        conf_env = getattr(self.Meta, 'conf_env')
        path = getattr(self.Meta, 'path')
        if conf_env:
            path = os.environ.get(conf_env)

        if path:
            # Obtain the corresponding configuration in the configuration file
            conf = self._load_conf(path)

            # Replace the default configuration
            for conf_key, conf_value in conf.items():
                setattr(self, conf_key, conf_value)

    @staticmethod
    def _load_conf(path: str) -> dict:
        """ Load the configuration file configuration
        """
        # Check whether the configuration file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f'No {path} found')

        # Reading a Configuration File
        with open(path, 'r', encoding='utf-8') as stream:
            yaml_config = yaml.load(stream, Loader=yaml.SafeLoader)

        return yaml_config
