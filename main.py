import logging
from aiogram import Bot, Dispatcher, executor, types
import subprocess

# توکن ربات خود را اینجا قرار دهید
API_TOKEN = '8962091539:AAHQBIHj2ZOptHTmfLKlsVS1bMBrbfGpK1A'

# تنظیمات اولیه ربات
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    # کدی که کاربر می‌فرستد را در متغیر code قرار می‌دهیم
    code = message.text
    
    try:
        # اجرای کد پایتون ارسالی توسط کاربر در یک محیط ایزوله
        result = subprocess.run(['python3', '-c', code], capture_output=True, text=True, timeout=5)
        
        # تهیه خروجی (stdout اگر موفق بود، stderr اگر خطا داشت)
        output = result.stdout or result.stderr or "کد خروجی خاصی نداشت."
        
        # ارسال پاسخ به کاربر (محدودیت ۱۰۰۰ کاراکتر برای نمایش)
        await message.answer(f"خروجی:\n{output[:1000]}")
        
    except Exception as e:
        await message.answer(f"خطا در اجرا: {str(e)}")

if __name__ == '__main__':
    executor.start_polling(dp)
