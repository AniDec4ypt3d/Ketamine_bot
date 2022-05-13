from dotenv import load_dotenv

from .client import TgClient
from .logger import logging


LOGS = logging.getLogger(__name__)
load_dotenv()

tgbot = TgClient(
    "tgbot", api_id=19863616, api_hash="3b24e34face45fa5acae85141e82a01b"
).start(bot_token="5164649274:AAHsbQYwYsbpw0EsJxMHQ8Oaj_0y6MYHEns")
LOGS.info("Bot has started successfully!")
