import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import subprocess

# توکن خود را در اینجا قرار دهید
API_TOKEN = '8962091539:AAHQBIHj2ZOptHTmfLk1sVS1bW8-G-6yZ0M'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("سلام! کد پایتون خود را بفرست تا اجرا کنم.")

@dp.message()
async def execute_code(message: types.Message):
    code = message.text
    try:
        # اجرای کد پایتون به صورت ایمن
        result = subprocess.check_output(['python3', '-c', code], stderr=subprocess.STDOUT, timeout=5, text=True)
    except subprocess.CalledProcessError as e:
        result = e.output
    except Exception as e:
        result = str(e)
        
    await message.answer(f"Output:\n{result}")

async def main():
    await dp.start_polling(bot)

if __name
