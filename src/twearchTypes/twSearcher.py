# -*- coding: utf-8 -*-
# the actual searcher
from twearchHttp import twearchHttp, httpQueue
from twearchTypes import twSearchParameters as sp, twSearchRequest as sr
from threading import Timer
class twSpider():
  def __init__(self, spider_name, search_query, results_per_page = 15):
    self.spiderName = spider_name
    self.query = search_query
    self.results_per_page = results_per_page
    req = sr.twSearchRequest()
    tsp = sp.twSearchParameters()
    req.params[tsp.SearchQuery] = self.query
    req.params[tsp.ResultsPerPage] = self.results_per_page
    self.http = twearchHttp.twHttp(req)
    self.http.updateCallback = self.onSearchReceived
    self.http.errorCallback = self.onError
  
  def onSearchReceived(self, data):
    print self.spiderName, '[data received]'
    if len(data.results):
      for post in data.results:
	print post.from_user, ':',  post.text
    else:
      print self.spiderName, '[no new tweets]'
    self.http.searchUrl = httpQueue.twitterUrl + data.refresh_url
    print ' url =', self.http.searchUrl
    Timer(10,httpQueue.add, [self]).start()
    return
  
  def onError(self, err):
    print self.spiderName, '[error]', err
    Timer(10,httpQueue.add, [self]).start()
    return
  
  
        
        
