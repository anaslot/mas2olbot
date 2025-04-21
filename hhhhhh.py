from telethon import TelegramClient
import asyncio
import os

# معلومات الحساب
api_id = int(os.getenv("API_ID", 23720496))  # API ID الخاص بك
api_hash = os.getenv("API_HASH", "4cefa25bb037a7bc9a7796286a0ce19b")  # API Hash الخاص بك
group_link = os.getenv("GROUP_LINK", "https://t.me/chbjhdbchsbdchbjkqbcQDCBSDVH")  # رابط المجموعة

# إنشاء جلسة Telethon
client = TelegramClient("session_name", api_id, api_hash)

async def send_messages():
    await client.start()

    # الحصول على كيان المجموعة من الرابط
    group = await client.get_entity(group_link)
    
    while True:
        # إرسال الرسالة إلى المجموعة
        await client.send_message(group, "تدريب")
        print("✅ تم إرسال الرسالة إلى المجموعة!")
        await asyncio.sleep(620)  # 620 ثانية = 10 دقائق و20 ثانية

# تشغيل السكربت
with client:
    client.loop.run_until_complete(send_messages())
