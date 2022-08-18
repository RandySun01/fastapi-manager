# sys
import importlib
import typing as t


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
        self.app.state.setting = setting

        # Extension initialized by default
        self._init_middleware(self.app)
        self._init_router(self.app)

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
            # Dynamically import the defined middleware
            module, middleware_class = import_middleware.rsplit('.', 1)
            module_obj = importlib.import_module(module)
            middleware = getattr(module_obj, middleware_class)

            # Middleware Parameters
            params = params or {}
            app.add_middleware(middleware, **params)

    @staticmethod
    def _init_router(app: t.Optional['FastAPI']):
        """ Initialize the FastAPI router
        """
        # setting: Configuration variables
        setting = app.state.setting
        routers = getattr(setting, 'Router', {})

        # Init router
        for import_router in routers:
            # Dynamically import the defined router
            module, router_str = import_router.rsplit('.', 1)
            module_obj = importlib.import_module(module)
            router = getattr(module_obj, router_str)

            # Register the Router with the app
            app.include_router(router)
