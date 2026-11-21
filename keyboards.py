from maxapi.utils.inline_keyboard import InlineKeyboardBuilder
from maxapi.types.attachments.buttons import (

    ClipboardButton,

    LinkButton,

    CallbackButton,
)

builder_admin = InlineKeyboardBuilder()

builder_admin.row(CallbackButton(text="Начать", payload="clicked_start"))

# await event.message.answer(
#
#     text="Выберите действие:",
#
#     attachments=[builder.as_markup()],
# )