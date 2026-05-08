# import asyncio
# import aiohttp
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.filters import CommandStart
#
# TOKEN = "8640053993:AAGSM_Ig_qwBZcnEveNETLuUsDkW05pR7lw"
# # O'zbekiston Markaziy Banki API'si (namuna uchun)
# API_URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# async def get_currency_rate():
#     """Tashqi API'dan kurslarni olib keluvchi funksiya"""
#     async with aiohttp.ClientSession() as session:
#         async with session.get(API_URL) as response:
#             data = await response.json()
#             # Markaziy bank barcha kurslarni list ko'rinishida beradi
#             # Bizga faqat USD (Dollar) kerak bo'lsa:
#             for item in data:
#                 if item['Ccy'] == 'USD':
#                     return item['Rate']
#     return "Xatolik yuz berdi"
#
# @dp.message(CommandStart())
# async def start_cmd(message: types.Message):
#     rate = await get_currency_rate()
#     await message.answer(f"Assalomu alaykum! 🇺🇿\n\nBugungi 1 AQSH dollari kursi: {rate} so'm")
#
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())