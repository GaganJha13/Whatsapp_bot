from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/Aman/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)

target = '"Gagan Jha"'
message = "Hello sir, This is an AI tool that is taking over the conversation"
number_of_times = 1  # No. of times to send a message

contact_path = '//span[contains(@title,' + target + ')]'
contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
contact.click()
message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))

# Send text message
for x in range(number_of_times):
    message_box.send_keys(message + Keys.ENTER)
    time.sleep(10)

# Send image
image_path = 'D:\img.png'  # Replace with the actual path of your image file
attachment_button = driver.find_element(By.XPATH, '//div[@title="Attach"]')
attachment_button.click()

image_input = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_input.send_keys(image_path)

# Wait for the image to be uploaded before sending
time.sleep(2)

# Click on the send button
send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
send_button.click()

# You may need to adjust the timing based on your system and network speed
time.sleep(10)
