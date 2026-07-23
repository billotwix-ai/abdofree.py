")
import subprocess
import sys
import time

def run_script(script_name):
    return subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    print("🚀 جاري تشغيل البوتين معاً...")
    
    # تشغيل ملف بوت الرد التلقائي (تأكد من اسم ملفك القديم، مثلاً auto_bot.py أو bot.py)
    p1 = run_script("bot.py")
    
    # تشغيل ملف بوت التحكم والأقسام الجديد
    p2 = run_script("admin_bot.py")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()
