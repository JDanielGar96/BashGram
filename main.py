import logging
import subprocess

from aiogram import Bot, Dispatcher, executor, types

ID = 1158986483
API_TOKEN = '1898906802:AAHkASvca63CCKlmKIC-xe2rJKOgzGTqAIU'
ERROR_MESSAGE = 'Ocurrio un error ejecutando el comando'
BLANK_RESPONSE = 'El comando se ejecuto con exito, pero no arrojo ningún resultado'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    if message.from_user.id == ID:
        logging.info(message.text)
        try:
            result = subprocess.check_output(message.text, shell=True,stderr=subprocess.STDOUT)
            if result:
                await message.answer(f"`{result.decode('utf-8')}`", parse_mode='markdown')
            else:
                await message.answer(BLANK_RESPONSE)
        except subprocess.CalledProcessError as e:
            await message.answer("Command '{}' return with error (code {}): \n{}".format(e.cmd, e.returncode, e.output.decode('utf-8')))

        # except Exception:
        #     await message.answer(ERROR_MESSAGE)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
