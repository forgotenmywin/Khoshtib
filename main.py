# main.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

TARGET_URL = "https://hashora.net/register?ref=KINGKINGPLM0073637"

# ===== مختصات کلیک =====
CLICK_X = 828
CLICK_Y = 936

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
# ===== توابع =====
# =============================================

def click_at(driver, x, y, label=""):
    """کلیک در مختصات مشخص"""
    try:
        actions = ActionChains(driver)
        actions.move_by_offset(x, y).click().perform()
        print(f"✅ Clicked at ({x}, {y}) {label}")
        return True
    except:
        try:
            result = driver.execute_script(f"""
                var element = document.elementFromPoint({x}, {y});
                if (element) {{
                    element.click();
                    element.focus();
                    return true;
                }}
                return false;
            """)
            if result:
                print(f"✅ Clicked at ({x}, {y}) with JavaScript {label}")
                return True
        except Exception as e:
            print(f"❌ Click failed: {e}")
            return False

def take_screenshot(driver, name, timestamp):
    """گرفتن اسکرین‌شات"""
    filename = f"{name}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f"📸 Screenshot saved: {filename}")
    return filename

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
    
    # ===== انتظار ۲۰ ثانیه =====
    print("\n⏳ Waiting 20 seconds...")
    for i in range(20, 0, -1):
        print(f"   {i}s remaining...", end="\r")
        time.sleep(1)
    print("\n✅ 20 seconds passed!")
    
    # ===== کلیک در مختصات =====
    print(f"\n🖱️ Clicking at ({CLICK_X}, {CLICK_Y})...")
    click_at(driver, CLICK_X, CLICK_Y, "(Click)")
    time.sleep(1)
    
    # ===== ۵ اسکرین‌شات با فاصله ۱ ثانیه =====
    print("\n📸 Taking 5 screenshots (every 1 second)...")
    for i in range(1, 6):
        screenshot_name = f"screenshot_{i}"
        take_screenshot(driver, screenshot_name, timestamp)
        if i < 5:
            time.sleep(1)
    
    print("\n✅ ALL DONE!")
    print(f"📸 5 screenshots saved: screenshot_1 to screenshot_5")
    
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
