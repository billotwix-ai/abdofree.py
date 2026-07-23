import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8834475874:AAGEFNQlgYQxa1BbGojcwX1Xvo1vfYmT3DU"
ADMIN_ID = 8198739841

bot = telebot.TeleBot(TOKEN)

bot_messages = {
    "welcome": "مرحباً بك في خدماتنا لبيع سكريبتات وبانل فري فاير 🎮🔥\n\nاختر ما يناسب جهازك بالرد برقم الطلب:\n\n1️⃣ - شراء بانل دريب كلين (أندرويد)\n2️⃣ - شراء بانل الحساب الأساسي / ميجيل برو\n3️⃣ - شراء ملفات فيلزا (أجهزة آيفون)\n4️⃣ - الاستفسار والتواصل المباشر",
    "android": "🤖 [ أسعار بانل دريب كلين - أندرويد بدون روت ]:\n• يوم: 50 ألف\n• أسبوع: 100 ألف\n• 15 يوم: 200 ألف\n• 30 يوم: 300 ألف\n\nللتواصل: @LAZERXx1",
    "miguel": "💎 [ أسعار بانل ميجيل برو / الحساب الأساسي ]:\n• يوم: 130 ألف\n• أسبوع: 410 ألف\n• شهر + يومين: 700 ألف\n\nللتواصل: @LAZERXx1",
    "filza": "🍏 [ أسعار ملفات فيلزا FILZA - آيفون ]:\n• ايم دراغ: 250 ألف\n• هيد شوت بطن: 350 ألف\n\nللتواصل: @LAZERXx1"
}

user_edit_state = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id == ADMIN_ID:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("⚙️ تعديل رسائل الأقسام", callback_data="edit_menu"))
        bot.send_message(message.chat.id, "مرحباً بك يا قائد 🛡️ لوحة التحكم:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, bot_messages["welcome"])

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    user_id = message.from_user.id
    text = message.text.strip()
    
    if user_id == ADMIN_ID and user_id in user_edit_state:
        section = user_edit_state[user_id]
        bot_messages[section] = text
        del user_edit_state[user_id]
        bot.send_message(message.chat.id, f"✅ تم تحديث قسم ({section}) بنجاح!")
        return

    if text == "1":
        bot.send_message(message.chat.id, bot_messages["android"])
    elif text == "2":
        bot.send_message(message.chat.id, bot_messages["miguel"])
    elif text == "3":
        bot.send_message(message.chat.id, bot_messages["filza"])
    elif text == "4" or text.lower() == "تواصل":
        bot.send_message(message.chat.id, "للتواصل المباشر:\n- تيليجرام: @LAZERXx1")
    else:
        bot.send_message(message.chat.id, bot_messages["welcome"])

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.from_user.id != ADMIN_ID:
        return
    if call.data == "edit_menu":
        bot.answer_callback_query(call.id)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📝 تعديل الترحيب", callback_data="edit_welcome"))
        markup.add(InlineKeyboardButton("🤖 تعديل أندرويد (1)", callback_data="edit_android"))
        markup.add(InlineKeyboardButton("💎 تعديل ميجيل (2)", callback_data="edit_miguel"))
        markup.add(InlineKeyboardButton("🍏 تعديل فيلزا (3)", callback_data="edit_filza"))
        bot.edit_message_text("اختر القسم للتعديل:", call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data.startswith("edit_"):
        bot.answer_callback_query(call.id)
        section = call.data.split("_")[1]
        user_edit_state[ADMIN_ID] = section
        bot.send_message(call.message.chat.id, f"أرسل النص الجديد لقسم ({section}):")

if __name__ == "__main__":
    bot.infinity_polling()
