import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "8659595370:AAFx26KVTCiD-X4NbJAiH_FkHSO6PkbbMmg"

# Savollar bazasi
QUESTIONS = [
    {
        "q": "Python-da ro'yxat (list) qaysi qavs bilan yaratiladi?",
        "options": ["[ ]", "{ }", "( )"],
        "a": "[ ]"
    },
    {
        "q": "Python asosan qaysi sohalarda kuchli?",
        "options": ["Ma'lumotlar fani (DS)", "O'yinlar yaratish", "Apparat ta'minoti"],
        "a": "Ma'lumotlar fani (DS)"
    }
]
# Bot holatlari
class Quiz(StatesGroup):
    answering = State()


bot = Bot(token=TOKEN)
dp = Dispatcher()


# /start komandasi
@dp.message(CommandStart())
async def start_quiz(message: types.Message, state: FSMContext):
    await state.update_data(current_q=0, score=0)  # Ma'lumotlarni nolga tushiramiz
    await message.answer("Assalomu alaykum! Python testiga tayyormisiz?")
    await send_question(message, state)


# Savolni yuborish funksiyasi
async def send_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    index = data['current_q']

    if index < len(QUESTIONS):
        item = QUESTIONS[index]

        # Tugmalarni yasash
        builder = ReplyKeyboardBuilder()
        for opt in item['options']:
            builder.add(types.KeyboardButton(text=opt))
        builder.adjust(2)  # Tugmalarni 2 qatorga taxlash

        await message.answer(f"{index + 1}-savol: {item['q']}",
                             reply_markup=builder.as_markup(resize_keyboard=True))
        await state.set_state(Quiz.answering)
    else:
        # Natija
        score = data['score']
        await message.answer(f"Test tugadi! To'g'ri javoblar: {score}/{len(QUESTIONS)}")
        await state.clear()


# Javobni qabul qilish
@dp.message(Quiz.answering)
async def handle_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()
    index = data['current_q']
    correct_answer = QUESTIONS[index]['a']

    if message.text == correct_answer:
        await state.update_data(score=data['score'] + 1)
        await message.answer("To'g'ri! ✅")
    else:
        await message.answer(f"Xato! ❌ To'g'ri javob: {correct_answer}")

    # Keyingi savolga o'tish
    await state.update_data(current_q=index + 1)
    await send_question(message, state)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())