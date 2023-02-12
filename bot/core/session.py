

from .client import TgClient  , my
import logging , asyncio
from veriable.veriable import API_HASH , API_ID , BOT_TOKEN
from .logger import log


LOGS = logging.getLogger(__name__)


# tgbot = TgClient(
#     "tg", api_id=22617364, api_hash="c8670439ede9d5cdd354ec06df474698"
# ).start(bot_token="5801605605:AAE4_dUVMoc7T2wme7lVTf2I_614PTiszkI")
# loop=asyncio.get_event_loop()

client = my(
    "tgv",
    API_ID,
    API_HASH,
    BOT_TOKEN,
    LOGS,
)
LOGS.info("Bot has started successfully!")
