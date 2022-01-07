import time

def send_message(driver, message):
    driver.find_element_by_xpath('//*[@id="message"]').send_keys(message)
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="chat_send"]').click()
    time.sleep(0.1)