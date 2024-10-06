import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image

class HomePage:
    textBox_fullName_xpath = "//input[@id='name']"
    btn_next_xpath = "//span[contains(text(),'Next')]"
    btn_sign_xpath = "//span[contains(text(),'Sign')]/parent::div[@class='label']"
    label_signed_document_xpath = "//span[contains(text(),'Document signed!')]"

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, full_name):
        self.driver.find_element(By.XPATH, self.textBox_fullName_xpath).send_keys(full_name)

    def click_next_btn(self):
        self.driver.find_element(By.XPATH, self.btn_next_xpath).click()

    def click_sign_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_sign_xpath))).click()

    def label_document_sign(self):
        ele = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.label_signed_document_xpath)))
        return ele.text

    def screenshot(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_sign_xpath)))
        self.driver.save_screenshot("./Screenshots/" + "screenshot.png")

        location = element.location
        size = element.size

        left = location['x'] + 200
        top = location['y'] - 1200
        right = left + size['width'] + 1500
        bottom = top + size['height'] + 700

        image = Image.open("./Screenshots/" + "screenshot.png")
        image.crop((left, top, right, bottom)).save("./Screenshots/" + "cropped_screenshot.png")

        path = "./Screenshots/" + "Screenshot.png"
        if os.path.exists(path):
            os.remove(path)
