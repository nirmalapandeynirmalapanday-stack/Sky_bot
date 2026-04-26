from pyrogram import filters
from clients import source_app
from config import OWNER_ID
from chat_state import (
    target_groups, authorized_users,
    update_volume, update_bass, update_eq,
    current_volume, current_bass, current_eq
)
from bridge import source_join, target_join, target_leave, leave_all_targets

def is_authorized(user_id):
    return user_id in authorized_users

@source_app.on_message(filters.command("join") & filters.group)
async def join_vc(client, message):
    if not is_authorized(message.from_user.id):
        await message.reply("❌ Permission nahi hai!")
        return
    group_id = message.chat.id
    await source_join()
    t = await target_join(group_id)
    if t:
        target_groups[group_id] = True
        await message.reply(
            f"✅ Live Relay Start!\n\n"
            f"🔊 Volume: {current_volume}%\n"
            f"🎸 Bass: {current_bass}\n"
            f"🎛️ EQ: {current_eq}\n"
            f"🎵 HD 320kbps"
        )
    else:
        await message.reply("❌ Error! Retry karo.")

@source_app.on_message(filters.command("leave") & filters.group)
async def leave_vc(client, message):
    if not is_authorized(message.from_user.id):
        await message.reply("❌ Permission nahi hai!")
        return
    await target_leave(message.chat.id)
    target_groups.pop(message.chat.id, None)
    await message.reply("✅ Left!")

@source_app.on_message(filters.command("leaveall") & filters.group)
async def leave_all(client, message):
    if not is_authorized(message.from_user.id):
        await message.reply("❌ Permission nahi hai!")
        return
    count = await leave_all_targets()
    target_groups.clear()
    await message.reply(f"✅ {count} Groups Left!")

@source_app.on_message(filters.command("vol") & filters.group)
async def set_volume(client, message):
    if not is_authorized(message.from_user.id):
        await message.reply("❌ Permission nahi!")
        return
    try:
        vol = int(message.command[1])
        if vol < 1 or vol > 20000:
            await message.reply("⚠️ 1 to 20000!")
            return
        update_volume(vol)
        await message.reply(f"🔊 Volume: {vol}%")
    except:
        await message.reply("❌ Use: /vol 1000")

@source_app.on_message(filters.command("bass") & filters.group)
async def set_bass(client, message):
    if not is_authorized(message.from_user.id):
        await message.reply("❌ Permission nahi!")
        return
    try:
        bass = int(message.command[1])
        if bass < 0 or bass > 20:
            await message.reply("⚠️ 0 to 20!")
            return
        update_bass(bass)
        await message.reply(f"🎸 Bass: {bass}")
    except:
        await message.reply("❌ Use: /bass 10")

@source_app.on_message(filters.command("eq") & filters.group)
async def set_eq(client, message):
    if not is_authorized(message.from_user.id):
        await message.reply("❌ Permission nahi!")
        return
    try:
        mode = message.command[1].lower()
        if mode not in ["normal", "bass", "treble", "clear", "vocal"]:
            await message.reply("⚠️ Modes: normal bass treble clear vocal")
            return
        update_eq(mode)
        await message.reply(f"🎛️ EQ: {mode}")
    except:
        await message.reply("❌ Use: /eq bass")

@source_app.on_message(filters.command("addadmin") & filters.group)
async def add_admin(client, message):
    if message.from_user.id != OWNER_ID:
        await message.reply("❌ Sirf owner!")
        return
    try:
        if message.reply_to_message:
            user = message.reply_to_message.from_user
            authorized_users.add(user.id)
            await message.reply(f"✅ {user.first_name} Added!")
        else:
            uid = int(message.command[1])
            authorized_users.add(uid)
            await message.reply(f"✅ {uid} Added!")
    except:
        await message.reply("❌ Reply karke ya /addadmin ID")

@source_app.on_message(filters.command("removeadmin") & filters.group)
async def remove_admin(client, message):
    if message.from_user.id != OWNER_ID:
        await message.reply("❌ Sirf owner!")
        return
    try:
        if message.reply_to_message:
            user = message.reply_to_message.from_user
            authorized_users.discard(user.id)
            await message.reply(f"✅ {user.first_name} Removed!")
        else:
            uid = int(message.command[1])
            authorized_users.discard(uid)
            await message.reply(f"✅ {uid} Removed!")
    except:
        await message.reply("❌ Reply karke ya /removeadmin ID")

@source_app.on_message(filters.command("admins") & filters.group)
async def admins_list(client, message):
    if not is_authorized(message.from_user.id):
        await message.reply("❌ Permission nahi!")
        return
    users = "\n".join([f"• `{uid}`" for uid in authorized_users]) or "None"
    await message.reply(f"👑 Admins:\n\n{users}")

@source_app.on_message(filters.command("status") & filters.group)
async def status_cmd(client, message):
    if not is_authorized(message.from_user.id):
        await message.reply("❌ Permission nahi!")
        return
    groups = "\n".join([f"• `{gid}`" for gid in target_groups.keys()]) or "None"
    await message.reply(
        f"📊 Status\n\n"
        f"🔊 Volume: {current_volume}%\n"
        f"🎸 Bass: {current_bass}\n"
        f"🎛️ EQ: {current_eq}\n"
        f"🎵 HD 320kbps\n"
        f"📢 Groups: {len(target_groups)}\n\n{groups}"
    )

@source_app.on_message(filters.command("help") & filters.group)
async def help_cmd(client, message):
    await message.reply(
        "🎙️ Live Voice Relay Bot\n\n"
        "/join — Relay start\n"
        "/leave — Leave group\n"
        "/leaveall — Leave all\n"
        "/vol 1000 — Volume (1-20000)\n"
        "/bass 10 — Bass (0-20)\n"
        "/eq bass — EQ mode\n"
        "/addadmin — Add admin\n"
        "/removeadmin — Remove admin\n"
        "/admins — List admins\n"
        "/status — Bot status\n"
        "/help — This message"
