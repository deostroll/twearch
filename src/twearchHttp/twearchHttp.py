# -*- coding: utf-8 -*-
from twearchTypes import twResultTypes

import urllib2
import json

class twHttp():
  def __init__(self, SearchRequest):
    self.searchUrl = SearchRequest.buildUrl()
    self.updateCallback = None		
    self.errorCallback = None
    
  def makeRequest(self):
    try:
      #print url for debugging only
      #print self.searchUrl
      httpRequest = urllib2.urlopen(self.searchUrl)
      searchDataResponse = httpRequest.read()
    except Exception, err:
	if self.errorCallback:
	  self.errorCallback(err)
	return
    self.parseResponse(searchDataResponse)
	  
  def parseResponse(self, jsonResponse):
    data = json.loads(jsonResponse)
    response = twResultTypes.twSearchResult()
    response.max_id = data['max_id']
    response.since_id = data['since_id']
    response.refresh_url = data['refresh_url']
    if 'next_page' in data:
      response.next_page = data['next_page']
    response.results_per_page = data['results_per_page']
    response.page = data['page']
    response.completed_in = data['completed_in']
    response.since_id_str = data['since_id_str']
    response.max_id_str = data['max_id_str']
    response.query = data['query']

    for tweet in data['results']:
      post = twResultTypes.twPost()
      post.from_user_id_str = tweet['from_user_id_str']
      post.profile_image_url = tweet['profile_image_url']
      post.create_at = tweet['created_at']
      post.from_user = tweet['from_user']
      post.id_str = tweet['id_str']
      post.to_user_id = tweet['to_user_id']
      post.text = tweet['text']
      post.id = tweet['id']
      post.from_user_id = tweet['from_user_id']
      post.geo = tweet['geo']
      post.iso_language_code = tweet['iso_language_code']
      post.to_user_id_str = tweet['to_user_id_str']
      post.source = tweet['source']
      response.results.append(post)
      
    self.updateCallback(response)	

  
    
