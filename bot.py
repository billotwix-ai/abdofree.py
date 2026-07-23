import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 30242201          
api_hash = '78259592286cda3680f631835e9d503a'  

SESSION_STRING = os.environ.get('SESSION_STRING')

client = TelegramClient(StringSession(SESSION_STRING), api_id, api_hash)

welcomed_users = set()

# النص الجديد مرتب أفقياً وعمودياً مع رموز تعبيرية خارقة 🔥
ad_message = """🔥 ──━ [ عروض خدمات فري فاير الرسمية ] ━── 🔥

🤖 [ قسم الأندرويد - دريب كلين ]   ⚔️   🍏 [ قسم آيفون - ملفات فيلزا ]
──────────────────────────────────────
• بانل Drip Client (بدون روت)         • من iOS 14.0 إلى 16.6.1
🔑 يوم: 50 ألف                       • ايم دراغ: 250 ألف
🔑 أسبوع: 100 ألف                     • هيد شوت بطن OBB: 350 ألف
🔑 15 يوم: 200 ألف                   • سرعة Speed: 400 ألف 
🔑 30 يوم: 300 ألف                   
(ايم بوت+دراغ+كشف أماكن+سرعة)       (ضمان تام بدون بلاك ليست)
──────────────────────────────────────

💎 ──━ [ القسم الثالث: آيفون ميجيل برو - الحساب الأساسي ] ━── 💎
• المميزات: (كشف أماكن + ايم بوت + ايم دراغ + OBB + مود ستريم)
🔑 يوم: 130 ألف 
🔑 أسبوع: 410 ألف   
🔑 شهر + يومين: 700 ألف + شهادة Gbox لمدة عام (365 يوم) لحمايتك وتفعيل نمط المطور.

📌 ملاحظات وطرق الدفع:
• التركيب: عبر انستغرام بعد فتح مشاركة شاشة.
• ملاحظة الشراء: (يوم أو أسبوع يحتاج حاسوب لتفعيل نمط المطور، أما الشهر فلا يحتاج).
• الدفع: 💳 بريدي موب أو CCP.
• للتواصل والدعم: @LAZERXx1"""

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handle_private_message(event):
    sender_id = event.sender_id
    
    # إذا كان المستخدم قد استلم رسالة الترحيب من قبل
    if sender_id in welcomed_users:
        await event.reply("⚡ انتظر قليلاً يا خويا، سيتم الرد عليك في أقرب وقت ممكن! 🦅🔥")
        return
        
    # إذا كانت أول مرة يرسل فيها رسالة
    welcomed_users.add(sender_id)
    await event.reply(ad_message)

print("UserBot is running and listening to your private chats...")
client.start()
client.run_until_disconnected()
