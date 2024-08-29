from selenium import webdriver

class Chrome:
    def driver(self):
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.add_argument("--incognito")
        return webdriver.Chrome(ChromeOptions)