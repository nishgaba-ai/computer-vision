import requests



class getRequest:
    '''
        Class to send GET request
    '''

    def __init__(self, GET_URL = None, GET_PARAMS = None):
        if GET_PARAMS is not None:
            setParams(GET_PARAMS)
        else:
            self.GET_PARAMS = GET_PARAMS

        if GET_URL is not None:
            setUrl(GET_URL)
        else:
            self.GET_URL = None

    def setUrl(self, GET_URL):
        self.GET_URL = GET_URL

    def setParams(self, GET_PARAMS):
        self.GET_PARAMS = dict(GET_PARAMS)

    def makeRequest(self):
        self.request = requests.get(url = self.GET_URL, params = self.GET_PARAMS)
        try:
            self.response = self.request.json()
        except:
            self.response = "Error while extracting JSON response for the GET request, please check 'request' attribute for further details"





class postRequest:
    '''
        Class to send POST request
    '''

    def __init__(self, POST_URL = None, POST_PARAMS = None):
        if POST_PARAMS is not None:
            setParams(POST_PARAMS)
        else:
            self.POST_PARAMS = POST_PARAMS

        if POST_URL is not None:
            setUrl(POST_URL)
        else:
            self.POST_URL = None

    def setUrl(self, POST_URL):
        self.POST_URL = POST_URL

    def setParams(self, POST_PARAMS):
        self.POST_PARAMS = dict(POST_PARAMS)

    def makeRequest(self):
        self.request = requests.post(url = self.POST_URL, data = self.POST_PARAMS)
        try:
            self.response = self.request.json()
        except:
            self.response = "Error while extracting JSON response for the POST request, please check 'request' attribute for further details"






















