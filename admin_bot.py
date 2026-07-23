import os
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# بيانات بوت التحكم
BOT_TOKEN = "8834475874:AAGEFNQlgYQxa1BbGojcwX1Xvo1vfYmT3DU"
ADMIN_ID = 8198739841  # الأيدي الخاص بك

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# قاموس مؤخم لحفظ رسائل الترحيب (يمكنك ربطه بملف لاحقاً لتثبيتها نهائياً)
bot_messages = {
    "welcome": "مرحباً بك في خدماتنا لبيع سكريبتات وبانل فري فاير 🎮🔥\n\nاختر ما يناسب جهازك بالرد برقم الطلب:\n\n1️⃣ - شراء بانل دريب كلين (أندرويد)\n2️⃣ - شراء بانل الحساب الأساسي / ميجيل برو\n3️⃣ - شراء ملفات فيلزا (أجهزة آيفون)\n4️⃣ - الاستفسار والتواصل المباشر",
    
    "android": "🤖 [ أسعار بانل دريب كلين - أندرويد بدون روت ]:\n• يوم: 50 ألف\n• أسبوع: 100 ألف\n• 15 يوم: 200 ألف\n• 30 يوم: 300 ألف\n(ايم بوت + ايم دراغ + قتل تلقائي + كشف اماكن + سرعة)\n\nللتواصل: @LAZERXx1",
    
    "miguel": "💎 [ أسعار بانل ميجيل برو / الحساب الأساسي ]:\n• يوم: 130 ألف\n• أسبوع: 410 ألف\n• شهر + يومين: 700 ألف + شهادة Gbox لمدة عام لحمايتك من البلاك ليست.\n\nللتواصل: @LAZERXx1",
    
    "filza": "🍏 [ أسعار ملفات فيلزا FILZA - آيفون ios 14.0 إلى 16.6.1 ]:\n• ايم دراغ: 250 ألف\n• هيد شوت بطن OBB: 350 ألف (مضمون في الرومات)\n• سرعة Speed: 400 ألف\n\nللتواصل: @LAZERXx1"
}

class AdminStates(StatesGroup):
    waiting_for_broadcast = State()
    waiting_for_section_choice = State()
    waiting_for_new_text = State()

current_editing_section = None

# أمر البدء للوحة التحكم
@dp.message(Command("start"), F.from_user.id == ADMIN_ID)
async def cmd_start(message: types.Message):
    kb = [
        [types.InlineKeyboardButton(text="📢 إرسال إذاعة للمستخدمين", callback_data="broadcast")],
        [types.InlineKeyboardButton(text="⚙️ تعديل رسائل الأقسام", callback_data="edit_msg")],
        [types.InlineKeyboardButton(text="📊 إحصائيات البوت", callback_data="stats")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    
    await message.answer(
        "مرحباً بك يا قائد 🛡️\nأهلاً بك في لوحة التحكم الخاصة ببوتك.",
        reply_markup=keyboard
    )

# حظر غير المشرفين
@dp.message(F.from_user.id != ADMIN_ID)
async def not_authorized(message: types.Message):
    # الرد التفاعلي للعملاء بناءً على الأرقام (1, 2, 3, 4)
    text = message.text.strip()
    if text == "1":
        await message.answer(bot_messages["android"])
    elif text == "2":
        await message.answer(bot_messages["miguel"])
    elif text == "3":
        await message.answer(bot_messages["filza"])
    elif text == "4" or text.lower() == "تواصل":
        await message.answer("للتواصل المباشر مع الدعم الفني والشراء:\n- تيليجرام: @LAZERXx1")
    else:
        # الرسالة الافتتاحية الترحيبية عند أول رسالة أو أي نص عشوائي
        await message.answer(bot_messages["welcome"])

# أزرار لوحة التحكم
@dp.callback_query(F.data == "stats", F.from_user.id == ADMIN_ID)
async def show_stats(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "📊 **إحصائيات البوت:**\n\n- حالة السيرفر: يعمل بنجاح على Railway 🟢\n- الأقسام المتاحة: أندرويد، ميجيل، فيلزا",
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "broadcast", F.from_user.id == ADMIN_ID)
async def start_broadcast(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("أرسل الآن الرسالة أو الإعلان الذي تريد إذاعته لجميع المستخدمين:")
    await state.set_state(AdminStates.waiting_for_broadcast)

@dp.message(AdminStates.waiting_for_broadcast, F.from_user.id == ADMIN_ID)
async def send_broadcast(message: types.Message, state: FSMContext):
    await message.answer(f"✅ تم استلام الإذاعة بنجاح وسيتم إرسالها:\n\n{message.text}")
    await state.clear()

# اختيار القسم المراد تعديله
@dp.callback_query(F.data == "edit_msg", F.from_user.id == ADMIN_ID)
async def choose_section_to_edit(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    kb = [
        [types.InlineKeyboardButton(text="📝 تعديل رسالة الترحيب الرئيسية", callback_data="edit_welcome")],
        [types.InlineKeyboardButton(text="🤖 تعديل قسم أندرويد (1)", callback_data="edit_android")],
        [types.InlineKeyboardButton(text="💎 تعديل قسم ميجيل برو (2)", callback_data="edit_miguel")],
        [types.InlineKeyboardButton(text="🍏 تعديل قسم فيلزا (3)", callback_data="edit_filza")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("اختر القسم الذي تريد تعديل نصه:", reply_markup=keyboard)

@dp.callback_query(F.data.startswith("edit_"), F.from_user.id == ADMIN_ID)
async def set_section_to_edit(callback: types.CallbackQuery, state: FSMContext):
    global current_editing_section
    await callback.answer()
    action = callback.data.split("_")[1]
    
    if action == "welcome":
        current_editing_section = "welcome"
    elif action == "android":
        current_editing_section = "android"
    elif action == "miguel":
        current_editing_section = "miguel"
    elif action == "filza":
        current_editing_section = "filza"
        
    await callback.message.answer(f"أرسل النص الجديد الآن لقسم ({current_editing_section}):")
    await state.set_state(AdminStates.waiting_for_new_text)

@dp.message(AdminStates.waiting_for_new_text, F.from_user.id == ADMIN_ID)
async def save_new_text(message: types.Message, state: FSMContext):
    global current_editing_section
    if current_editing_section:
        bot_messages[current_editing_section] = message.text
        await message.answer(f"✅ تم تحديث نص قسم ({current_editing_section}) بنجاح!")
    await state.clear()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
