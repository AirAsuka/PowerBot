import botpy
from botpy.message import Message

from configs import settings


class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        await message.reply(
            content=f"机器人{self.robot.name}收到你的@消息了: {message.content}"
        )


if __name__ == "__main__":

    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=settings.BOT_APPID, token=settings.BOT_TOKEN)
