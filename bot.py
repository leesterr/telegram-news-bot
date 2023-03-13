from aiogram import Dispatcher, Bot, executor, types
from aiogram.utils.exceptions import MessageIsTooLong
from news_sources.durovs_code.durovs import durov_source
from news_sources.malawi.malawi24 import malawi_news
from news_sources.malawi.malawi24 import malawi_news_short
from news_sources.bbc.bbc_news import bbc_world


token = 'telegram_api_token_here'
bot = Bot(token=token)
disp = Dispatcher(bot)


def main():
    @disp.message_handler(commands='durov')
    async def durovs_news(msg: types.Message):
        news = durov_source()
        await msg.bot.send_message(chat_id=-1001534611726, text=news, parse_mode='HTML')

    @disp.message_handler(commands='malawi')
    async def malawi_24_news(msg: types.Message):
        news = malawi_news()
        short = malawi_news_short()
        try:
            await msg.bot.send_message(chat_id=-1001534611726, text=news, parse_mode='HTML')
        except MessageIsTooLong:
            await msg.bot.send_message(chat_id=-1001534611726, text=short, parse_mode='HTML')

    @disp.message_handler(commands='bbc')
    async def bbc_world_news(msg: types.Message):
        news = bbc_world()
        await msg.bot.send_message(chat_id=-1001534611726, text=news, parse_mode='HTML')

    executor.start_polling(disp)


if __name__ == '__main__':
    main()
