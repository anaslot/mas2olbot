from telethon import TelegramClient
import asyncio

# معلومات حسابك
api_id = 23720496  # API ID الخاص بك
api_hash = "4cefa25bb037a7bc9a7796286a0ce19b"  # API Hash الخاص بك
group_link = "https://t.me/chbjhdbchsbdchbjkqbcQDCBSDVH"  # رابط المجموعة

# إنشاء جلسة Telethon
client = TelegramClient("session_name", api_id, api_hash)

async def send_messages():
    await client.start()
    
    while True:
        await client.send_message(group_link, "تدريب")  # إرسال الرسالة
        print("✅ تم إرسال الرسالة إلى المجموعة!")
        await asyncio.sleep(620)  # 600 ثانية = 10 دقائق

# تشغيل السكربت
with client:
    client.loop.run_until_complete(send_messages())
