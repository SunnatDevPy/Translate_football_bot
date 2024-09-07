from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.buttuns.inline import main_menu, make_channels
from bot.handlers.admin import mandatory_channel
from config import BOT
from db import User

start_router = Router()


@start_router.message(CommandStart())
async def command_start(message: Message, bot: Bot):
    # if message.from_user.id in [1353080275, 5649321700] + [i for i in await User.get_admins()]:
    #     await message.answer(f'Hush kelibsiz Admin {message.from_user.first_name}', reply_markup=main_menu(admin=True))
    # else:
        channels = await mandatory_channel(message.from_user.id, bot)
        if channels:
            try:
                await message.edit_text('Barchasiga obuna boling',
                                        reply_markup=await make_channels(channels, bot))
            except:
                await message.answer('Barchasiga obuna boling',
                                        reply_markup=await make_channels(channels, bot))
        else:
            user_data = {'id': message.from_user.id, 'username': message.from_user.username,
                         'full_name': message.from_user.full_name}
            user = await User.get(message.from_user.id)
            if not user:
                await User.create(**user_data)
                await message.answer(f'Hush kelibsiz {message.from_user.first_name}', reply_markup=main_menu())
                await bot.send_message(int(BOT.ADMIN),
                                       f'Yangi user qo\'shildi @{message.from_user.username}!')
                await bot.send_message(1353080275,
                                       f'Yangi user qo\'shildi @{message.from_user.username}!')
            else:
                await message.answer(f'Hush kelibsiz {message.from_user.first_name}', reply_markup=main_menu())
