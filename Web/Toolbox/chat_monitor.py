"""import time
from Toolbox import interact

def count_message(driver, time_, silent=False):
    if type(time_) != int: time_ = 60

    message_window = driver.find_element_by_xpath('//*[@id="header_chat"]')
    message_window.click()
    while len(driver.find_elements_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div')) == 0:
        time.sleep(1)

    if silent == False:
        interact.send_message(driver, "Recording number of messages in {} seconds.".format(time_))

    refresh_rate = None
    for i in range(f)
    initial_length = len(driver.find_elements_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div')) - 1
    time.sleep(time_)
    end_length = len(driver.find_elements_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div')) - 1
    messages_sent = end_length-initial_length
    driver.find_element_by_xpath('//*[@id="slide_close"]').click()

    if silent == False:
        interact.send_message(driver, "Messages sent in {} seconds: {}".format(time_, messages_sent))

    return messages_sent"""