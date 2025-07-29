import uiautomator2 as u2
import logging
import time

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

app_name = "com.feds.official"

def launch_app(d, name):
    try:
        # Start the app by its manifest name
        d.app_start(name)
        if d.app_wait (name, timeout=5):
            logger.info(f"{name} 順利啟動")
        else:
            logger.info(f"{name} 沒有如期啟動")

        # Explicit wait for the app to be ready by checking its main screen
        if d(text="Main screen identifier").wait(timeout=5):  # Adjust the identifier accordingly
            logger.info(f"{name} 主畫面準備就緒")
        else:
            logger.warning(f"{name} 主畫面未能及時顯示")

    except Exception as e:
        logger.info(f"App啟動失敗: {e}")
        
def click_button(d, name):
    # 嘗試點擊按鈕（可用 text 或 resourceId）
    try:
        button = d(text=name) or d(description=name)

        if button.exists:
            button.click()
            logger.info(f"完成點擊\"{name}\"按鈕")
        else:
            logger.info(f"找不到\"{name}\"按鈕")

        # Wait until the next screen is ready after the click
        if button.wait(timeout=2):  # Replace with actual identifier after click
            logger.info(f"等待\"{name}\"按鈕後的畫面顯示成功")
        else:
            logger.warning(f"等待\"{name}\"按鈕後的畫面超時")

    except Exception as e:
        logger.error(f"點擊按鈕 {name} 失敗: {e}")

def click_coordinates (d, name):
    # 無法透過text 或 resourceId 來點擊 "簽到任務" 按鈕，改成點擊座標
    try:
        btn = d(text=name)

        if btn.exists:
            logger.info(f"\"{name}\"button存在")
            bounds = btn.info['bounds']
            x = (bounds['left'] + bounds['right']) // 2
            y = (bounds['top'] + bounds['bottom']) // 2 - 50
            logger.info(f"x: {x}, y: {y}")
            d.click(x, y)
        else:
            logger.warning(f"找不到\"{name}\"按鈕")

        # Wait after clicking coordinates
        if btn.wait(timeout=2):  # Adjust the identifier accordingly
            logger.info(f"等待\"{name}\"按鈕後的畫面顯示成功")
        else:
            logger.warning(f"等待\"{name}\"按鈕後的畫面超時")

    except Exception as e:
        logger.error(f"點擊座標 {name} 失敗: {e}")

def main():
    try:
        # 連接設備，預設會連接唯一設備
        d = u2.connect() 
        logger.info ("設備連接成功")
    except Exception as e:
        logger.error ("設備連接失敗: {e}")

    launch_app (d, app_name)
    click_button (d, "我的")
    click_coordinates (d, "簽到任務")
    click_button (d, "每日簽到")
    click_button (d, "立即簽到")

    try:
        d.app_stop(app_name)
        logger.info (f"{app_name} 停止成功")
    except Exception as e:
        logger.error (f"{app_name} 停止失敗: {e}")

if __name__ == "__main__":
    main()
    
