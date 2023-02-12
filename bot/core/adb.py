from .aioredis import AioRedis
import logging
import asyncio
from ..core.logger import log
from veriable.veriable import REDIS_URL , REDIS_PASS , REDIS_PORT
loop = asyncio.get_event_loop()

adb = AioRedis(
        loop=loop,
        host=REDIS_URL,
        port=REDIS_PORT,
        password= REDIS_PASS if REDIS_PASS else None,
        logger=log
        )