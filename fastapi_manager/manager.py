# sys
import importlib
import typing as t

# 3p
from fastapi import FastAPI

# project
from .setting import SettingCore


class Manager:
    """ Encapsulates the FASTAPI initialization procedure

    >>> Usage:
        from fastapi import FastAPI
        from fastapi_app import Manager, SettingCore
        from fastapi_app.extend import logger_extend

        class YouSetting(SettingCore):
            ...

        setting = YouSetting()
        app = FastAPI()

        with Manager(app, setting) as app:
            logger_extend(app)
            ...
    """

    def __init__(self, app: t.Optional['FastAPI'], setting: t.Optional['SettingCore']):
        self.app = app
        self.app.state.setting = setting

        # Extension initialized by default
        self._init_middleware(self.app)
        self._init_router(self.app)

    def __enter__(self):
        return self.app

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.app.state.setting

    @staticmethod
    def _init_middleware(app: FastAPI):
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
    def _init_router(app: FastAPI):
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
