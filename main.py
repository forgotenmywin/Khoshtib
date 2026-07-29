# main.py - فقط مرورگر باز میشه و بعد ۲۰ ثانیه یک عکس میگیره
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

TARGET_URL ="pornhub.com"

# ===== تنظیمات مرورگر =====
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# =============================================
# ===== اجرای اصلی =====
# =============================================

driver = None
timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

try:
    print("=" * 70)
    print("🚀 Starting browser...")
    print("=" * 70)
    
    driver = webdriver.Chrome(options=options)
    
    print(f"\n🌐 Opening {TARGET_URL}...")
    driver.get(TARGET_URL)
    
    print("\n⏳ Waiting 20 seconds...")
    for i in range(20, 0, -1):
        print(f"   {i}s remaining...", end="\r")
        time.sleep(1)
    print("\n✅ 20 seconds passed!")
    
    # گرفتن یک اسکرین‌شات
    screenshot_path = f"screenshot_{timestamp}.png"
    driver.save_screenshot(screenshot_path)
    print(f"📸 Screenshot saved: {screenshot_path}")
    
    print("\n✅ DONE!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    if driver:
        driver.save_screenshot(f"error_{timestamp}.png")
    import traceback
    traceback.print_exc()
    
finally:
    if driver:
        driver.quit()
        print("👋 Browser closed")
