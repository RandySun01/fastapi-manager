# sys
import typing as t


def orm_extend(app: t.Optional['FastAPI']):
    """ The orm extension
    """
    # setting: Configuration variables
    setting = app.state.setting
    database = getattr(setting, 'Database', {})

    from tortoise.contrib.fastapi import register_tortoise

    register_tortoise(app, **database)
