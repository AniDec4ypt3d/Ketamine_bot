

from .client import TgClient  , my
import logging , asyncio
from veriable.veriable import API_HASH , API_ID , BOT_TOKEN
from .logger import log


LOGS = logging.getLogger(__name__)




client = my(
    "tgv",
    API_ID,
    API_HASH,
    BOT_TOKEN,
    LOGS,
)
LOGS.info("Bot has started successfully!")
