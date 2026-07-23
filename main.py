import subprocess
import sys
import time

def run_script(script_name):
    """دالة لتشغيل ملف بايثون كعملية مستقلة"""
    return subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    print("🚀 جاري بدء تشغيل البوتات معاً في الخلفية...")
    
    # 1. تشغيل بوت الرد التلقائي القديم (تأكد أن اسم ملفه القديم هو auto_bot.py)
    p1 = run_script("auto_bot.py")
    
    # 2. تشغيل بوت التحكم والأقسام الجديد (تأكد أن اسم ملفه الجديد هو admin_bot.py)
    p2 = run_script("admin_bot.py")
    
    try:
        # إبقاء السيرفر حياً يتابع العمليات
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()
        print("تم إيقاف البوتات.")
