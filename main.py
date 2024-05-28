from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

ACCOUNT_TO_FOLLOW = "shiba.inu.fans_"
USERNAME = "Your Instagram username"
PASSWORD = "Your Instagram password"

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(4)

        #cookie
        accept_button = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        accept_button.click()
        time.sleep(4)

        #Log in
        login_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        login_button.send_keys(USERNAME)
        time.sleep(2)
        password_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        password_button.send_keys(PASSWORD, Keys.RETURN)
        time.sleep(5)
        #popups
        save_info_not_now = self.driver.find_element(By.XPATH, '//div[contains(text(), "Not now")]')
        save_info_not_now.click()
        time.sleep(4)

        notifications_button = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_button:
            notifications_button.click()
            time.sleep(4)

    def find_followers(self):
        #Search account
        self.driver.get('https://www.instagram.com/shiba.inu.fans_/')
        time.sleep(4)
        click_followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        click_followers.click()
        time.sleep(4)
        scroll = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
        for i in range(4):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(10)

    def follow(self):
        #Follow Button
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        
        #Click follow
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

