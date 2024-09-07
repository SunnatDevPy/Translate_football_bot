from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, Bot
from aiogram.enums import ChatMemberStatus
from aiogram.types import Message

from bot.buttuns.inline import make_channels
from bot.handlers.add_channels import channels_db
from db.models.model import Channels


# class JoinChannelMiddleware(BaseMiddleware):
#     async def __call__(
#             self,
#             handler,
#             event: Message,
#             data
#     ):
#         if event.callback_query and event.callback_query.data == 'confirm_channel' or event.message:
#             if event.callback_query:
#                 user = event.callback_query.from_user
#             else:
#                 user = event.message.from_user
#             bot: Bot = data['bot']
#             form_kb = []
#             for channel_id in channels_db.keys():
#                 member = await bot.get_chat_member(channel_id, user.id)
#                 if member.status == ChatMemberStatus.LEFT:
#                     form_kb.append(channel_id)
#             if form_kb:
#                 if event.callback_query:
#                     try:
#                         await event.callback_query.message.edit_text('Barchasiga obuna boling', reply_markup=await make_channels(form_kb, bot))
#                     except:
#                         await event.callback_query.message.answer('Barchasiga obuna boling', reply_markup=await make_channels(form_kb, bot))
#
#                 else:
#                     await event.message.answer('Kanallarga azo bolmagansiz', reply_markup=await make_channels(form_kb, bot))
#                 return
#
#             return await handler(event, data)


# class Middleware(BaseMiddleware):
#     async def __call__(
#             self,
#             handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
#             event: Message,
#             data: Dict[str, Any],
#     ) -> Any:
#         unsubscribe_channels = [channel_id.id for channel_id in await Channels.get_all() if (
#             await event.bot.get_chat_member(channel_id.id, event.from_user.id)).status == ChatMemberStatus.LEFT]
#         if unsubscribe_channels:
#             await event.answer('Kanalga azo boling', reply_markup=make_channels_button(unsubscribe_channels))
#             return
#         return await handler(event, data)
#
# class ConfirmChannelMiddleware(BaseMiddleware):
#     async def __call__(
#             self,
#             handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
#             event: CallbackQuery,
#             data: Dict[str, Any],
#     ) -> Any:
#         unsubscribe_channels = [channel_id for channel_id in CHANNEL_IDS if (
#             await event.bot.get_chat_member(channel_id, event.from_user.id)).status == ChatMemberStatus.LEFT]
#         if unsubscribe_channels:
#             await event.message.edit_text('Hammasiga obuna bolmadiz', reply_markup=make_channels_button(unsubscribe_channels))
#             return
#         return await handler(event.message, data)