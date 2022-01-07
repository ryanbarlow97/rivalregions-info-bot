import json
import sys
import time

from Web.Toolbox import instance
from Web.Toolbox.threader import do_every


def collect_stats(interval, iterations):
    def handle_prices(price_list):
        item_price_dict = json.load(open("price_stats.txt"))
        index = 0

        for i in item_price_dict:
            item_price_dict[i].append(price_list[index])
            index = index + 1

        json.dump(item_price_dict, open("price_stats.txt", 'w'))

    def collect_prices():
        try:
            driver = instance.login()
            driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[6]").click()
            time.sleep(1)
            price_list = []
            for item in range(0, 16):
                if item == 7: continue
                driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[{}]".format(str(3+item))).click()
                time.sleep(0.5)
                price = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[3]/span/span").text
                price_list.append(price)

            handle_prices(price_list)
        except:
            try:
                instance.destroy(driver)
            except:
                exit()


    item_price_dict = {}
    item_list = ["oil", "ore", "uranium", "diamonds",
                 "liquid oxygen", "helium-3", "antirad",
                 "spacerockets", "tanks", "aircrafts",
                 "missiles", "bombers", "battleships",
                 "moon tanks", "space stations"]


    for i in item_list:
        item_price_dict[i] = []

    json.dump(item_price_dict, open("price_stats.txt", 'w'))

    do_every(interval, collect_prices, iterations)

