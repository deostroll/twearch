# -*- coding: utf-8 -*-
from collections import deque
import threading
import time

SearchQueue = None
timer = None
twitterUrl = 'http://search.twitter.com/search.json'

def init():
  print 'initialized queue'
  global SearchQueue
  SearchQueue = deque()
  
def add(item):
  print 'add() started...added item', time.strftime('%H:%M:%S')
  global SearchQueue
  print 'added', item.spiderName, 'to queue'
  SearchQueue.appendleft(item)
  print 'add() ending...', time.strftime('%H:%M:%S')
  
def doWork():
  print 'doWork() started...', time.strftime('%H:%M:%S')
  global SearchQueue
  lock = threading.Lock()
  print 'acquire lock'
  if lock.acquire(False):
    while len(SearchQueue):      
      SearchQueue.pop().http.makeRequest()        
  print 'release'
  lock.release()
  setTimer()
  print 'doWork() ending...', time.strftime('%H:%M:%S')
  
def setTimer():
  global timer
  timer = threading.Timer(30, doWork)  
  timer.daemon = True
  timer.start()
  
def killTimer():
  global timer
  timer.cancel()


