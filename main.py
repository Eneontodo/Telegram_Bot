from os import getenv
from aiogram import Bot, executor, types
from aiogram.dispatcher.dispatcher import Dispatcher
from dotenv import load_dotenv
import inline

load_dotenv()
bot = Bot(getenv("TOKEN"))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f"Привет! {message.from_user.first_name}, добро пожаловать в магазин Earldom",
                         reply_markup=inline.explor)


@dp.callback_query_handler()
async def catalogue(callback: types.CallbackQuery):
    if callback.data == "Холодильник":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"вы выбрали:\t{callback.data},\nмодель:\tKit fort КТ–3159–1\nстоимость:\t<s>{getenv('PRICE_HOLOD')}</s>/ 0$\nза "
                                    f"доставку:{getenv('PRICE_DOST')}", parse_mode=types.ParseMode.HTML)
    elif callback.data == "Микроволновка":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"вы выбрали:\t{callback.data},\nмодель:\tHi M020B03 Black\nстоимость:\t<s>{getenv('PRICE_MICRO')}</s>/ 0$\nза "
                                    f"доставку:{getenv('PRICE_DOST')}", parse_mode=types.ParseMode.HTML)
    elif callback.data == "Тостер":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"вы выбрали:\t{callback.data},\nмодель:\tHi HTS–002\nстоимость:\t<s>{getenv('PRICE_TOSTER')}</s>/ 0$\nза "
                                    f"доставку:{getenv('PRICE_DOST')}", parse_mode=types.ParseMode.HTML)
    elif callback.data == "Стиральная машина":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"вы выбрали:\t{callback.data},\nмодель: indent EWSB 5085 CIS\nстоимость:\t<s>{getenv('PRICE_STIR')}</s>/ 0$\nза "
                                    f"доставку:{getenv('PRICE_DOST')}", parse_mode=types.ParseMode.HTML)
    elif callback.data == "Морозильная камера":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"вы выбрали:\t{callback.data},\nмодель:\tIndent DFZ 5175\nстоимость:\t<s>{getenv('PRICE_MOROZ')}</s>/ 0$\nза "
                                    f"доставку:{getenv('PRICE_DOST')}", parse_mode=types.ParseMode.HTML)
    elif callback.data == "Телевизор":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"вы выбрали:\t{callback.data},\nмодель:\tHi IPHIX-32H181MSY\nстоимость:\t<s>{getenv('PRICE_TV')}</s>/ 0$\nза "
                                    f"доставку:{getenv('PRICE_DOST')}", parse_mode=types.ParseMode.HTML)
    elif callback.data == "Вибратор":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"вы выбрали:\t{callback.data},\nстоимость:\t<s>{getenv('PRICE_VIBER')}</s>/ 0$\nза "
                                    f"доставку:{getenv('PRICE_DOST')}", parse_mode=types.ParseMode.HTML)
    elif callback.data == "Телефон":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"вы выбрали:\t{callback.data},\nмодель:\t15 Pro Maximum\nстоимость:\t<s>{getenv('PRICE_PHONE')}</s>/ 0$\nза "
                                    f"доставку:{getenv('PRICE_DOST')}", parse_mode=types.ParseMode.HTML)
    elif callback.data == "Духовка":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"вы выбрали:\t{callback.data},\nмодель:\tGoren BOS6737E13FBG\nстоимость:\t<s>{getenv('PRICE_DUN')}</s>/ 0$\nза "
                                    f"доставку:{getenv('PRICE_DOST')}", parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Каталог")
async def assort(message: types.Message):
    await message.answer("*" * 10 + "каталог" + "*" * 10, reply_markup=inline.ass)


@dp.message_handler(text="Контакты")
async def contact(message: types.Message):
    await  message.answer("Консультант–продавец:\n\t@nostaz09\nРазработчик:\n\t@Pontooned")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)