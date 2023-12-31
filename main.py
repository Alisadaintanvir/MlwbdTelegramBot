import time
import os
from telebot import TeleBot
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

bot = TeleBot(token=os.environ.get("BOT_TOKEN"))
current_users = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Please enter the movie link from MLWBD:")


@bot.message_handler(func=lambda message: True)
def download_movie(message):
    chat_id = message.chat.id

    if chat_id in current_users:
        bot.send_message(chat_id, "You are already in the process of downloading a movie.")
        return

    current_users[chat_id] = True
    url = message.text.strip()

    title = url.split("/")[-2]

    wait_message = bot.send_message(chat_id, "Please wait while we process your request...")

    print("It may take 60 seconds or more based on your internet speed.")

    # Hide chrome and work in background
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    wait = WebDriverWait(driver, 60)
    window_before = driver.window_handles[0]

    form_id = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/div/div/"
                                            "table/tbody/tr[1]/td[1]/form").get_attribute("id")

    script = f"javascript:document.getElementById({form_id}).submit();"
    driver.execute_script(script)

    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    download_btn1 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/center/form/button"))
    )
    download_btn1.click()

    download_btn2 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/form/div/input"))
    )
    download_btn2.click()

    download_btn3 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/a"))
    )
    download_btn3.click()

    download_btn4 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/article/div[2]/div[2]/div/p/a"))
    )
    download_btn4.click()

    download_btn5 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/article/div[2]/div[3]/form/input[2]"))
    )
    download_btn5.click()

    download_btn6 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div/a"))
    )
    download_btn6.click()

    download_btn7 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[2]/div[2]/form/input[2]"))
    )
    download_btn7.click()

    download_btn8 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/a[2]"))
    )
    download_btn8.click()

    time.sleep(3)

    # Notify the user with the download link
    bot.send_message(message.chat.id, f"Here is your download page link of '{title}':\n{driver.current_url}")

    driver.quit()

    del current_users[chat_id]
    bot.delete_message(chat_id, wait_message.message_id)


bot.polling()
