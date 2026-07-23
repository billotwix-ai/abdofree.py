import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 30242201          
api_hash = '78259592286cda3680f631835e9d503a'  

SESSION_STRING = os.environ.get('SESSION_STRING')

client = TelegramClient(StringSession(SESSION_STRING), api_id, api_hash)

welcomed_users = set()

# نص الإعلان مرتب ومنظم (أندرويد - آيفون وفيلزا - الحساب الأساسي)
ad_message = """WELCOME ⚙️📜🔐💎

🤖 [ قسم أندرويد ] - بانل دريب كلين (Drip Client) بدون روت:
• يوم: 50 ألف
• أسبوع: 100 ألف
• 15 يوم: 200 ألف
• 30 يوم: 300 ألف
(المميزات: ايم بوت + ايم دراغ + قتل تلقائي + كشف اماكن + سرعة / بدون بند ولا بلاك ليست)

🍏 [ قسم آيفون وملفات فيلزا FILZA ] - (من ios 14.0 إلى 16.6.1):
• ايم دراغ: 250 ألف (بدون بند وبدون بلاك ليست)
• هيد شوت بطن OBB: 350 ألف (مضمون في الرومات فقط)
• سرعة Speed: 400 ألف (مضمون 100% في جميع الأوضاع)

💎 [ قسم الحساب الأساسي ] (كشف أماكن + ايم بوت + ايم دراغ + OBB + مود ستريم):
• يوم: 130 ألف
• أسبوع: 410 ألف
• شهر + يومين: 700 ألف + شهادة Gbox لمدة عام (365 يوم) لتفعيل نمط المطور وحمايتك من البلاك ليست.
(ملاحظة: شراء يوم أو أسبوع يتطلب تفعيل نمط المطور بالحاسوب، أما شهر فلا يحتاج حاسوب).

💳 [ معلومات إضافية ]:
• طريقة التركيب: عبر انستغرام أو تيليجرام بعد فتح مشاركة شاشة.
• طريقة الدفع: بريدي موب أو CCP.
• للتواصل والاستفسار: @LAZERXx1"""

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handle_private_message(event):
    sender_id = event.sender_id
    if sender_id not in welcomed_users:
        welcomed_users.add(sender_id)
        await event.reply(ad_message)

print("UserBot is running and listening to your private chats...")
client.start()
client.run_until_disconnected()
