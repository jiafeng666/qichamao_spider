from selenium import webdriver


def get_driver():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
    chromeOptions.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')
    chromeOptions.add_experimental_option('useAutomationExtension', False)
    chromeOptions.add_argument('--disable-infobars')
    chromeOptions.add_argument("--start-maximized")
    # 修改
    # chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--no-sandbox")
    # 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
    path = r'.\chromedriver.exe'
    driver = webdriver.Chrome(options=chromeOptions, executable_path=path)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    })
    driver.set_page_load_timeout(60)
    return driver
