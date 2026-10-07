import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

BOT_TOKEN = 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- Клавтуры ---
def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💰 Прайс и Объемы", callback_data="pricing")],
            [InlineKeyboardButton(text="🤝 Сотрудничество", callback_data="coop")],
            [InlineKeyboardButton(text="📊 Арбитраж трафика", callback_data="arbitrage")]
        ]
    )
    return keyboard

# --- Обработчики команд ---
@dp.message(CommandStart())
async def cmd_start(message: Message):
    text = (
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я бот по вопросам сотрудничества и арбитража трафика.\n"
        "Выберите нужный раздел в меню ниже или задайте свой вопрос напрямую."
    )
    await message.answer(text, reply_markup=get_main_keyboard())

@dp.message(Command("help"))
async def cmd_help(message: Message):
    text = (
        "ℹ️ **Справка по командам:**\n\n"
        "/start — Перезапустить бота / Главное меню\n"
        "/help — Показать эту справку\n\n"
        "Вы также можете просто написать в чат слова: **'трафик'**, **'цена'**, **'объем'** или **'сотрудничество'**."
    )
    await message.answer(text, parse_mode="Markdown")

# --- Обработчики нажатий на кнопки ---
@dp.callback_query(F.data == "pricing")
async def process_pricing(callback: types.CallbackQuery):
    text = (
        "💳 **Условия и стоимость наливания трафика:**\n\n"
        "• **Минимальный тест:** от 500 лидов / $1.5 за лид\n"
        "• **Стандартный объем:** 1 000 – 5 000 лидов / $1.2 за лид\n"
        "• **VIP / Масштаб:** от 10 000+ лидов / индивидуальный KPI и цена от $0.9 за лид\n\n"
        "Для согласования источников (FB, Google, TikTok, PPC) напишите нашему менеджеру."
    )
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "coop")
async def process_coop(callback: types.CallbackQuery):
    text = (
        "🤝 **Варианты сотрудничества:**\n\n"
        "1. Работа по модели CPA / CPL / RevShare.\n"
        "2. Прием вашего трафика на наши офферы.\n"
        "3. Закупка готовых связок и приватных офферов.\n\n"
        "Напишите ваши источники и текущий суточный объем, чтобы обсудить детали."
    )
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "arbitrage")
async def process_arbitrage(callback: types.CallbackQuery):
    text = (
        "📊 **Арбитраж трафика:**\n\n"
        "Мы работаем с ключевыми вертикалями (Nutra, Crypto, Gambling, Finance).\n"
        "Предоставляем прилы, агенты, клоакинг и быструю выплатную аналитику."
    )
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()

# --- Обработчик текстовых сообщений (Ключевые слова) ---
@dp.message(F.text)
async def handle_text(message: Message):
    user_text = message.text.lower()

    if any(word in user_text for word in ["сколько", "цена", "стоимость", "объем", "лить", "прайс"]):
        text = (
            "💰 **Информация по объемам и ценам:**\n\n"
            "• Минимальный тестовый кап: **500 лидов**.\n"
            "• Базовая ставка: **$1.2 - $1.5** за квалифицированный лид.\n"
            "• Скидки и повышенные ставки обсуждаются при объемах от **2 000 лидов/день**.\n\n"
            "Хотите забронировать СРА-капу?"
        )
        await message.answer(text, parse_mode="Markdown")

    elif any(word in user_text for word in ["сотрудничество", "партнерство", "работать"]):
        text = (
            "🤝 Мы открыты к партнерству с медиабайерскими командами и соло-арбитражниками.\n"
            "Оставьте контакты вашего Telegram или описание истоков, и мы свяжемся с вами."
        )
        await message.answer(text)

    elif any(word in user_text for word in ["арбитраж", "связка", "оффер"]):
        text = (
            "🎯 В наличии приватные офферы под бурж и СНГ с высоким ROI.\n"
            "Для получения списка актуальных кап напишите команду /start и выберите нужный раздел."
        )
        await message.answer(text)

    else:
        await message.answer(
            "Я пока не понял ваш вопрос. Воспользуйтесь меню /start или спросите про объемы и цены!",
            reply_markup=get_main_keyboard()
        )

# --- Запуск бота ---
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
