from dotenv import load_dotenv

from .core.session import tgbot
from .core.logger import logging
from . import handlers, commands

load_dotenv()

LOGS = logging.getLogger("TgBot")


tgbot.run_until_disconnected()
