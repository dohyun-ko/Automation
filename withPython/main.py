import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os

if __name__ == '__main__':
    print("Auto youtube subtitle parser for internet letters to the Korean army.")

    video_url = input("Enter the youtube video url: ")
    subtitle_url = "https://downsub.com/?url=subtitle.to/" + video_url

    dir_path = os.path.dirname(os.path.realpath(__file__))

    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": dir_path}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    driver.get(url=subtitle_url)

    try:
        subtitle_button = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, "#app > div > main > div > div.container.ds-info.outlined > div > div.row.no-gutters > div.pr-1.col-sm-7.col-md-6.col-12 > div.flex.mt-5.text-center > div.layout.justify-start.align-center > button:nth-child(2)"))
        subtitle_button.click()
    except Exception as e:
        print(e)



