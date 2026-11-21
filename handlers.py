from typing import Dict, Optional
from maxapi.filters import F
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder
from maxapi.types.attachments.buttons import CallbackButton
from keyboards import builder_admin
from state import ProcessExcel
from test import mes_test_oper
from utils import GROUP_CHAT_TEST_ID, GROUP_CHAT_WORK_ID, bot, logger, file_path_report, file_path_month
from maxapi import Dispatcher, types
from maxapi.types import Command, BotStarted, MessageCreated, MessageCallback
from function import read_repot_file, get_str_stat, get_str_month, get_str_total, get_message_new, get_brigade
import io
import logging
from maxapi.context import MemoryContext, StatesGroup, State
import aiohttp

dp = Dispatcher()
dp_admin = Dispatcher()


@dp.message_created()
async def echo_handler(event: MessageCreated):
    """
    Обработка команды '/send'
    """

    user_text = event.message.body.text

    if user_text == '/send':
        operator_dict, total_dict = read_repot_file(file_path_report, file_path_month)

        str_month = get_str_month()
        str_total_month = get_str_total(total_dict, operator_dict)
        str_stat_operator = get_str_stat(operator_dict)
        # message_news = get_message_new()

        # await bot.send_message(chat_id=GROUP_CHAT_ID, text=message_news)
        await bot.send_message(chat_id=GROUP_CHAT_WORK_ID, text=str_month)

        await bot.send_message(chat_id=GROUP_CHAT_WORK_ID, text=str_total_month)
        await bot.send_message(chat_id=GROUP_CHAT_WORK_ID, text=str_stat_operator)
        await event.message.answer(f"Файлы обработаны. Итоги отправлены в чат")

    else:
        await event.message.answer("Введена неверная команда!")


@dp_admin.bot_started()
async def begin(event: BotStarted):

    await event.message.answer(text="Нажми на кнопку:",
                                 attachments=[builder_admin.as_markup()])

@dp_admin.message_created(Command('start'))
async def cmd_start(event: MessageCreated):

    await event.message.answer(text="Нажми на кнопку:",
                                 attachments=[builder_admin.as_markup()])






@dp_admin.message_callback(F.callback.payload == "clicked_start")
async def clicked_start(event: MessageCallback, context: MemoryContext):
    await context.clear()
    await event.message.answer("Привет! Отправь мне первый Excel-файл.")
    await context.set_state(ProcessExcel.waiting_first_file)


# @dp_admin.message_created(
#     state=ProcessExcel.waiting_first_file,
# )
# async def process_first_file(event: MessageCreated, context: MemoryContext):
#     document = event.message.body.attachments[0]
#     if not (
#         document.filename.endswith(".xlsx")
#         or document.filename.endswith(".xls")
#     ):
#         await event.message.answer(
#             "Это не Excel-файл. Пожалуйста, отправьте файл .xlsx или .xls."
#         )
#         return
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(document.payload.url) as resp:
#                 file_bytes = await resp.read()
#         # file_bytes = await bot.download_file(document.payload.url)
#         file = io.BytesIO(file_bytes)
#         brigade_list = get_brigade(file)
#         print(brigade_list)
# # Сохраняем значение в контекст FSM (память состояния)
#         await context.update_data(brigade=brigade_list)
# #         await message.reply(
# #             f"Первый файл принят! Значение ячейки A1: {first_val}\n\n"
# #             "Теперь отправь второй Excel-файл."
# #         )
# # Переводим пользователя в следующее состояние
# #         await ProcessExcel.waiting_for_second_file.set()
#     except Exception as e:
#         logging.error(f"Ошибка при обработке первого файла: {e}")
#         await event.message.answer("Ошибка чтения первого файла. Попробуйте снова.")
