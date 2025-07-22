import uiautomator2 as u2
import time

app_name = "com.feds.official"

def launch_app(name):
    try:
        d.app_start(name)  # 遠東百貨的manifest name
        if d.app_wait (name, timeout=5):
            print(f"{name} 順利啟動")
        else:
            print(f"{name} 沒有如期啟動")
    except Exception as e:
        print(f"App啟動失敗: {e}")
        
def click_button(name):
    # 嘗試點擊「我的」按鈕（可用 text 或 resourceId）
    if d(text=name).exists:
        d(text=name).click()
        print(f"完成點擊\"{name}\"按鈕")
    elif d(description=name).exists:
        d(description=name).click()
        print(f"完成點擊\"{name}\"按鈕")
    else:
        print(f"找不到\"{name}\"按鈕")

    time.sleep(2)

    # print(d(text="簽到任務").info)

def click_coordinates (name):
    # 無法透過text 或 resourceId 來點擊 "簽到任務" 按鈕，改成點擊座標
    btn = d(text=name)

    if btn.exists:
        print(f"\"{name}\"button存在")
        bounds = btn.info['bounds']
        x = (bounds['left'] + bounds['right']) // 2
        y = (bounds['top'] + bounds['bottom']) // 2 - 50
        print(f"x: {x}, y: {y}")
        d.click(x, y)
    else:
        print(f"找不到\"{name}\"按鈕")

    time.sleep(2)

if __name__ == "__main__":
    # 連接設備
    d = u2.connect()  # 預設會連接唯一設備
    launch_app (app_name)
    click_button ("我的")
    click_coordinates ("簽到任務")
    click_button ("賺點任務")
    click_button ("限時遊戲")
    click_button ("每日簽到")
    click_button ("立即簽到")
    d.app_stop(app_name)
    
