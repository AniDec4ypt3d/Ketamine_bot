

from .core.session import client 
from .core.logger import logging
from . import database
from .plugins import checkers, commands



LOGS = logging.getLogger("client")


# tgbot.run_until_disconnected()
client.run_until_disconnected()

