from Web.launch import launch_it
from threading import Thread
from Discord import bot
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d [%(threadName)s] %(message)s')
    info = {'stop': False}
    t1 = Thread(target=launch_it, args=(info,), name="Web Bot")
    t2 = Thread(target=bot.run, args=(info,), name="Discord Bot")
    while True:
        print("Menu:")
        print("[1] Launch Web Bot")
        print("[2] Launch Discord Bot")
        print("[3] Launch Both.")
        print("Input 1/2/3.")
        answer = input()
        if answer == "1":
            logging.debug("Starting Web Bot thread.")
            t1.start()
            t1.join()

            "thread finished...exiting"
        elif answer == "2":
            t2.start()
            t2.join()
        elif answer == "3":
            threads =[]
            t1.start()
            t2.start()
            for i in threads:
                i.join()
        else:
            pass # rinse and repeat.