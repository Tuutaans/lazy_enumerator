#!/usr/bin/python3

import sys
import threading
import time

exitFlag = 0

main = threading.main_thread()

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.daemon = True
print(thread1.daemon)
thread1.start()
thread2.start()
print(main.daemon)
sys.exit(); print ("Exiting Main Thread") 
print(main.is_alive())
thread1.join()
thread2.join()