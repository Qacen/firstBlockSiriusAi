from selenium import webdriver
from selenium_stealth import stealth

def driver_create(url):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    options.add_argument("--headless")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    stealth(
        driver,
        languages=["ru-RU", "ru"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    driver.get(url)
    return driver
