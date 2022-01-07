import time
import threading
from Web.Toolbox.instance import login
from Web.Toolbox.stats_collector import collect_stats
from Web.Toolbox.threader import myThread
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)

def launch_it(info):
    logging.debug('Hi from myfunc')
    #driver = login()
    #print("Logged in.")
    #time.sleep(3)
    # interact.send_message(driver, "This is an automated bot process logging in. Date-time: {}".format(str(time.ctime())))
    #time.sleep(0.5)
    # interact.send_message(driver, "Current cash levels: {}".format(driver.find_element_by_xpath('//*[@id="m"]').text))

    """ Message Counter - Unfinished """
    # print("Counting starts now.")
    # messages_sent = chat_monitor.count_message(driver, 1800, True)
    # print("Messages send: {}".format(str(messages_sent)))

    """ Price Collector - Unfinished """
    stats_thread = myThread(1, "Stats Collector - Startup", collect_stats, 5, 1)
    stats_thread2 = myThread(2, "Stats Collector - Startup2", collect_stats, 5, 1)
    stats_thread.run()
    stats_thread2.run()

    print(str(threading.enumerate()))