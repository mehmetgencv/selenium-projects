# imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
from config import Config
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--keyword', required=True)
args = vars(parser.parse_args())


configs = Config()
# specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome("drivers/chromedriver.exe")
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys(configs.INSTAGRAM_USERNAME)
password.send_keys(configs.INSTAGRAM_PASSWORD)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

not_now2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

# driver.get("https://www.instagram.com/explore/")
search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
search_box.clear()
keyword = args.get("keyword")
search_box.send_keys(keyword)
search_box.send_keys(Keys.ENTER)
search_box.send_keys(Keys.ENTER)
driver.execute_script("window.scrollTo(0, 4000);")

images = driver.find_elements(by=By.TAG_NAME, value="img")
images = [image.get_attribute("src") for image in images]

path = os.getcwd()
path = os.path.join(path, "images")
if not os.path.isdir(path):
    os.mkdir(path)
path = os.path.join(path, keyword[1:] + "s")
# path = path.replace("\\", "/")
if not os.path.isdir(path):
    os.mkdir(path)

for idx, img in enumerate(images):
    save_as = os.path.join(path, keyword[1:] + str(idx) + ".jpg")
    wget.download(img, save_as)