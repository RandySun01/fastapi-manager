# sys
import importlib
import typing as t


def orm_extend(app: t.Optional['FastAPI']):
    """ The orm extension
    """
    # setting: Configuration variables
    setting = app.state.setting
    database = getattr(setting, 'Database', {})

    if not database:
        raise KeyError('The Database key is not configured in the configuration object')

    tortoise = importlib.import_module('tortoise')
    register_tortoise = tortoise.contrib.fastapi.register_tortoise

    register_tortoise(app, **database)
