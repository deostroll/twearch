import twSearchParameters as sp
import urllib
import twSearchException as tse

class twSearchRequest():
    __twitterSearchUrl = 'http://search.twitter.com/search.json'
    def __init__(self):
        self.params = {}
        
    def buildUrl(self):
        sQstr = ''
	tsp = sp.twSearchParameters
        keys = self.params.keys()
        for key in keys:
            if key == tsp.SearchQuery:
                sQstr = ('?', sQstr + '&')[len(sQstr)>0 and sQstr[0] == '?'] + 'q=' + urllib.quote_plus(self.params[tsp.SearchQuery])
            elif key == tsp.ResultsPerPage:
                sQstr = ('?', sQstr + '&')[len(sQstr)>0 and sQstr[0] == '?'] + 'rpp=' + str(self.params[tsp.ResultsPerPage])
            elif key == tsp.Since_ID:
                sQstr = ('?', sQstr + '&')[len(sQstr)>0 and sQstr[0] == '?'] + 'since_id=' + self.params[tsp.Since_ID]
            elif key == tsp.Since:
                sQstr = ('?', sQstr + '&')[sQstr[0] == '?'] + 'since=' + self.params[tsp.Since]
            else:
                raise tse.twSearchException('Invalid Search Parameter')
        
        return  self.__twitterSearchUrl + sQstr
