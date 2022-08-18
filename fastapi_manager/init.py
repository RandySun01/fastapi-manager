# sys
import typing as t

# project
from .helper import dynamic_import


class InitApp:
    """ Encapsulates the FASTAPI initialization procedure
    """

    def __init__(self, app: t.Optional['FastAPI'], setting: t.Any):
        """ ...

        :param app: FastApi initialized object;
        :param setting: The object must be accessible
        to getattr for the specified configuration.
        """
        # Add a setting to the fastapi.state object
        self.app = app
        if not setting:
            raise ValueError('Setting cannot be None')
        self.app.state.setting = setting

        # Extension initialized by default
        self._init_middleware(self.app)
        self._init_router(self.app)
        self._init_extend(self.app)

    def __enter__(self) -> t.Optional['FastAPI']:
        return self.app

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Remove setting from the fastapi.state object
        del self.app.state.setting

    @staticmethod
    def _init_middleware(app: t.Optional['FastAPI']):
        """ Initialize the FastAPI middleware
        """
        # setting: Configuration variables
        setting = app.state.setting
        middlewares = getattr(setting, 'MiddleWare', {})

        # Init middleware
        for import_middleware, params in middlewares.items():
            middleware = dynamic_import(import_middleware)
            params = params or {}
            app.add_middleware(middleware, **params)

    @staticmethod
    def _init_router(app: t.Optional['FastAPI']):
        """ Initialize the FastAPI router
        """
        # setting: Configuration variables
        setting = app.state.setting
        routers = getattr(setting, 'Router', [])

        # Init router
        for import_router in routers:
            router = dynamic_import(import_router)
            app.include_router(router)

    @staticmethod
    def _init_extend(app: t.Optional['FastAPI']):
        """ Initializing the extension
        """
        # setting: Configuration variables
        setting = app.state.setting
        extends = getattr(setting, 'Extend', [])

        # Init router
        for extend in extends:
            extend = dynamic_import(extend)
            extend(app)
