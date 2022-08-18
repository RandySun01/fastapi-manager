# sys
import typing as t


def cache_extend(app: t.Optional['FastAPI']):
    """ Cache extension
    """
    # setting: Configuration variables
    setting = app.state.setting
    cache = getattr(setting, 'Cache', {})

    import aioredis

    @app.on_event("startup")
    async def startup_event():
        app.state.redis = await aioredis.from_url(**cache)

    @app.on_event("shutdown")
    async def shutdown_event():
        await app.state.redis.close()
