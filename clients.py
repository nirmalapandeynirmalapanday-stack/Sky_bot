from pyrogram import Client
from pytgcalls import PyTgCalls
from config import *

source_app = Client(
    "source_bot",
    api_id=SOURCE_API_ID,
    api_hash=SOURCE_API_HASH,
    phone_number=SOURCE_PHONE
)

target_app = Client(
    "target_bot",
    api_id=TARGET_API_ID,
    api_hash=TARGET_API_HASH,
    phone_number=TARGET_PHONE
)

source_calls = PyTgCalls(source_app)
target_calls = PyTgCalls(target_app)
