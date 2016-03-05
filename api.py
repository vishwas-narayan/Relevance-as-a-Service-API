import requests
import json


class Api:
    """
    This is a python class to extract data from different API's in JSON format and store it in files.
    The different functions are used for extracting data using Non-GMO HTTP library
    for python 	known as Requests.

    Mainly consists the following variables:
    payload - a dictionary which is used to pass the parameters to a particular URL query string.
    r - a response object which is used to GET data from the URL query string.
    data - a json decoder for the stream of data from r.
    extract - It is used to get particular lists(details of certain key attributes) from the dictionary
    returned from the response object.
    outfile - text file to store values of specific keys present in the response object dictionary.
    """

    def __init__(self):
        """
        Generating the access_token whenever an API is invoked
        """
        self.access_token = '68a98c9fe9ebfc409d7d46bd9d496561045e9d52372c8896c8f25d1d6e64e1d8'

    def articles(self,query,page,rows):
        """
        This API returns relevant articles for a given topic in near real-time.

        Signature:http://api.rightrelevance.com/v2/articles/search?query=<rr_topic>&start=X&rows=Y&access_token=<access_token>

        :param query: a particular topic user searches.
        :param page: pages
        :param rows: rows
        :return: JSON String of the topic.

        """

        payload = {'query':query,'page':page,'rows':rows,'access_token': self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/articles/search",params=payload,stream=True)
        data = r.json()
        extract = data['articles']
        with open('art_file.txt','w') as outfile:
            json.dump(extract,outfile)

    def influencers(self,query,page,rows):

        """
        This API provides access to the influencers graph for a structured RightRelevance topic.
        It is 2-level (global and per-topic) rank page provides unparalleled relevance.

        Signature: http://api.rightrelevance.com/v2/experts/search?query=<rr_topic>&start=X&rows=Y&access_token=<access_token>
        """

        payload = {'query':query,'page':page,'rows':rows,'access_token':self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/experts/search",params=payload,stream=True)
        data = r.json()
        extract = data['results']
        with open('inf_file.txt','w') as outfile:
            json.dump(extract,outfile)

    def conversations(self,query,page,rows,order):

        """
        This API aggregates and provide topical influencer conversations in a tree topology.

        Signature: http://api.rightrelevance.com/v2/conversations/search?query=<rr_topic>&page=X&rows=Y&order_by=_order_by_&access_token=<access_token>
        """
        payload = {'query':query,'page':page,'rows':rows,'order_by':order,'access_token':self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/conversations/search",params=payload,stream=True)
        data = r.json()
        extract = data['conversations']
        with open('conv_file.txt','w') as outfile:
            json.dump(extract,outfile)

    def autocomplete(self, q):
        """
        This API supports auto-complete functionality for a search box experience in your application.

        Signature: http://api.rightrelevance.com/v2/topics/autocomplete?q=<string>&access_token=<access_token>
        """
        payload = {'query':q,'access_token':self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/topics/autocomplete",params=payload,stream=True)
        data = r.json()
        extract = data['suggestions']
        with open('autocomp_file.txt','w') as outfile:
            json.dump(extract, outfile)

api_obj = Api()	 # object of class Api.
api_obj.articles('data',0,1)  # Data Extraction from articles API which is stored in a file called 'art_file.txt'
