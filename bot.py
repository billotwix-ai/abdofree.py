import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 30242201          
api_hash = '78259592286cda3680f631835e9d503a'  

SESSION_STRING = os.environ.get('SESSION_STRING')

client = TelegramClient(StringSession(SESSION_STRING), api_id, api_hash)

welcomed_users = set()

# النص مرتب بشكل عمودي وجميل (كل قسم لوحده تحت بعضه)
ad_message = """🔥 ──━ [ عروض خدمات فري فاير الرسمية ] ━── 🔥

🤖 [ 1️⃣ قسم الأندرويد - بانل دريب كلين بدون روت ]
• المميزات: (ايم بوت + ايم دراغ + قتل تلقائي + كشف أماكن + سرعة / بدون بند ولا بلاك ليست)
🔑 يوم: 50 ألف 
🔑 أسبوع: 100 ألف 
🔑 15 يوم: 200 ألف 
🔑 30 يوم: 300 ألف

──────────────────────────────────────

💎 [ 2️⃣ قسم آيفون - ميجيل برو / الحساب الأساسي ]
• المميزات: (كشف أماكن + ايم بوت + ايم دراغ + OBB + مود ستريم)
🔑 يوم: 130 ألف 
🔑 أسبوع: 410 ألف   
🔑 شهر + يومين: 700 ألف + شهادة Gbox لمدة عام (365 يوم) لحمايتك وتفعيل نمط المطور.
⚠️ ملاحظة: شراء (يوم أو أسبوع) يتطلب حاسوب لتفعيل نمط المطور، أما (الشهر) فلا يحتاج حاسوب.

──────────────────────────────────────

🍏 [ 3️⃣ قسم آيفون - ملفات فيلزا FILZA ]
• المدى المداعم: (من ios 14.0 إلى 16.6.1) - (بدون بند ولا بلاك ليست)
• ايم دراغ: 250 ألف
• هيد شوت بطن OBB: 350 ألف (مضمون في الرومات فقط)
• سرعة Speed: 400 ألف (مضمون 100% في جميع الأوضاع)

──────────────────────────────────────

📌 [ معلومات التركيب والدفع ]:
• طريقة التركيب: عبر انستغرام بعد فتح مشاركة شاشة.
• طريقة الدفع: 💳 بريدي موب أو CCP.
• للتواصل والدعم المباشر: @LAZERXx1"""

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handle_private_message(event):
    sender_id = event.sender_id
    
    if sender_id in welcomed_users:
        await event.reply("⏳ انتظر قليلا سارد عليك عندما اعود 🦅🔥")
        return
        
    welcomed_users.add(sender_id)
    await event.reply(ad_message)

print("UserBot is running and listening to your private chats...")
client.start()
client.run_until_disconnected()
