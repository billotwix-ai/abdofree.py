import os
import time
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 30242201          
api_hash = '78259592286cda3680f631835e9d503a'  

SESSION_STRING = os.environ.get('SESSION_STRING')

client = TelegramClient(StringSession(SESSION_STRING), api_id, api_hash)

# قواميس لتتبع حالة المستخدمين وأوقات حظرهم المؤقت
user_states = {}  # لتتبع هل أخذ رسالة الأقسام أم لا (0: لم يرسل شيئاً، 1: أخذ الأقسام، 2: أخذ رسالة الانتظار وتم حظره لمدة شهر)
user_timers = {}  # لتسجيل وقت الرد الأخير لحساب مدة شهر (30 يوماً)

# اليوزر المستثنى الذي لا يجب أن يرد عليه البوت أبداً
EXCLUDED_USERNAME = "rivairhack"

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
    sender = await event.get_sender()
    
    # 1. إذا كان المرسل هو أنت أو الحساب المستثنى، تجاهله تماماً
    if sender and sender.username:
        if sender.username.lower() == EXCLUDED_USERNAME.lower():
            return

    sender_id = event.sender_id
    current_time = time.time()
    ONE_MONTH_SECONDS = 30 * 24 * 60 * 60  # مدة شهر بالثواني

    # التحقق مما إذا كان المستخدم في فترة الحظر (شهر كامل لا يرد عليه البوت)
    if sender_id in user_states and user_states[sender_id] == 2:
        last_time = user_timers.get(sender_id, 0)
        # إذا لم تمر شهر بعد، تجاهل الرسالة تماماً
        if current_time - last_time < ONE_MONTH_SECONDS:
            return
        else:
            # إنقضاء الشهر، إعادة تعيين الحالة للبداية إذا عاد بعد شهر
            user_states[sender_id] = 0

    # الحالة الأولى: لم يراسلك من قبل (أو مر شهر) -> أرسل رسالة الأقسام
    if sender_id not in user_states or user_states[sender_id] == 0:
        user_states[sender_id] = 1
        user_timers[sender_id] = current_time
        await event.reply(ad_message)
        return

    # الحالة الثانية: أرسل رسالة ثانية بعد رسالة الأقسام -> أرسل رسالة الانتظار واقفل الرد لمدة شهر
    if user_states[sender_id] == 1:
        user_states[sender_id] = 2  # الانتقال لحالة الحظر المؤقت لشهر
        user_timers[sender_id] = current_time
        await event.reply("⏳ انتظر قليلا سارد عليك عندما اعود 🦅🔥")
        return

print("UserBot is running and listening to private chats with smart filtering...")
client.start()
client.run_until_disconnected()
