import asyncio
from telethon import TelegramClient, events
from telethon.errors import FloodWaitError

from .logger import logging

LOGS = logging.getLogger(__name__)


class TgClient(TelegramClient):
    def on_cmd(self, command, pattern=None):
        """Decorator for cc check cmd."""

        if pattern is None:
            pattern = command

        pattern = rf"\/{command}"

        def decorator(func):
            async def wrapper(event):
                tmp = event.raw_text.split(" ")
                try:
                    event.card = tmp[1].strip()
                except IndexError:
                    return await event.reply(
                        "**Please provide card.**\n\n`cc|month|year|cvc`"
                    )

                card_details = event.card.split("|")
                try:
                    event.ccn, event.month, event.year, event.cvc = card_details
                    print(event.ccn)
                except ValueError:
                    return await event.reply(
                        "**Please provide valid input.**\n\n`cc|month|year|cvc`"
                    )

                try:
                    await func(event)
                except FloodWaitError as e:
                    LOGS.warning(f"FloodWaitError, sleeping for {e.seconds}.")
                    await asyncio.sleep(e.seconds)

                return wrapper

            self.add_event_handler(wrapper, events.NewMessage(pattern=pattern))

        return decorator
