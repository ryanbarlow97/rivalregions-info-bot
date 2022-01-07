import threading

import threading
import time

import threading
import time

exitFlag = 0

class myThread(threading.Thread):
   def __init__(self, threadID, name, function_, *args):
       threading.Thread.__init__(self)
       self.threadID = threadID
       self.name = name
       self.function_ = function_
       self.args = args

   def run(self):
      print("Starting " + self.name)
      self.function_(*self.args)
      print("Exiting " + self.name)

def do_every (interval, worker_func, iterations = 0):
  if iterations != 1:
    threading.Timer (
      interval,
      do_every, [interval, worker_func, 0 if iterations == 0 else iterations-1]
    ).start ()

  worker_func ()

def setInterval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop(lock):
                with lock:# executed in another thread
                    while not stopped.wait(interval): # until stopped
                        function(*args, **kwargs)

            lock = threading.Lock()
            t = threading.Thread(target=loop, name ="Interval", args=(lock,))
            t.daemon = True # stop if the program exits
            t.start()
            return stopped
        return wrapper
    return decorator

"""
Recreation
"""

