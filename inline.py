from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

ass = InlineKeyboardMarkup(row_width=2)
ass.add(InlineKeyboardButton(text="Холодильник", callback_data="Холодильник"),
        InlineKeyboardButton(text="Тостер",  callback_data="Тостер"),
        InlineKeyboardButton(text="Микроволновка", callback_data="Микроволновка"),
        InlineKeyboardButton(text="Морозильная камера", callback_data="Морозильная камера"),
        InlineKeyboardButton(text="Стиральная машина", callback_data="Стиральная машина"),
        InlineKeyboardButton(text="Телевизор", callback_data="Телевизор"),
        InlineKeyboardButton(text="Духовка", callback_data="Духовка"),
        InlineKeyboardButton(text="Мобильный телефон", callback_data="Телефон")
        )

explor = ReplyKeyboardMarkup(resize_keyboard=True)
explor.add("Каталог").add("Контакты")
