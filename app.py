import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# ТВОЙ ТОКЕН (прямо в коде)
TOKEN = "8611461483:AAHk3o1EaSh0JZ1XygsKOYdS-BcGzZox19k"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("🚀 Бот работает! (токен в коде)")

@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer("Просто отправь любое сообщение, я отвечу!")

@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())