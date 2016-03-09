import requests


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
    For further Details:http://info.rightrelevance.com/docs/api-docs/
    """

    def __init__(self):
        """
        Generating the access_token whenever an API is invoked
        """
        self.access_token = '68a98c9fe9ebfc409d7d46bd9d496561045e9d52372c8896c8f25d1d6e64e1d8'

    def articles(self,query,start,rows):
        """
        This API returns relevant articles for a given topic in near real-time.

        Signature:http://api.rightrelevance.com/v2/articles/search?query=<rr_topic>&start=X&rows=Y&access_token=<access_token>

        :param query: a particular query topic user searches.
        :param start: start=X: Starting index for articles. Default-0
        :param rows: rows=Y: Number of articles to return. Default-10
        :return: JSON String of the topic.

        """

        payload = {'query':query,'start':start,'rows':rows,'access_token': self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/articles/search",params=payload,stream=True)
        #with open('art_file.txt','w') as outfile:
        #    for chunk in r.iter_content(chunk_size=1):
        #        outfile.write(chunk)
        """ returning the JSON Response """
        for chunk in r.iter_content(chunk_size=1000000):
            return chunk

    def influencers(self,query,start,rows):

        """
        This API provides access to the influencers graph for a structured RightRelevance topic.
        It is 2-level (global and per-topic) rank page provides unparalleled relevance.

        Signature: http://api.rightrelevance.com/v2/experts/search?query=<rr_topic>&start=X&rows=Y&access_token=<access_token>


        :param query: a particular query topic user searches.
        :param start: start=X: Starting index for articles. Default-0
        :param rows: rows=Y: Number of articles to return. Default-10
        :return: JSON String of the topic.
        """

        payload = {'query':query,'start':start,'rows':rows,'access_token':self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/experts/search",params=payload,stream=True)
        #with open('influencers_file.txt','w') as outfile:
        #    for chunk in r.iter_content(chunk_size=1):
        #        outfile.write(chunk)
        """ returning the JSON Response """
        for chunk in r.iter_content(chunk_size=1000000):
            return chunk

    def conversations(self,query,page,rows,order):

        """
        This API aggregates and provide topical influencer conversations in a tree topology.

        Signature: http://api.rightrelevance.com/v2/conversations/search?query=<rr_topic>&page=X&rows=Y&order_by=_order_by_&access_token=<access_token>

        :param query: a particular query topic user searches.
        :param page: page=X: Starting index for articles. Default-0
        :param rows: rows=Y: Number of articles to return. Default-10
        :param order: orderby=[time|relevance]: Order in which the conversations are received. Default-relevance
        :return: JSON String of the topic.

        """
        payload = {'query':query,'page':page,'rows':rows,'order_by':order,'access_token':self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/conversations/search",params=payload,stream=True)
        #with open('conversations_file.txt','w') as outfile:
        #    for chunk in r.iter_content(chunk_size=1):
        #        outfile.write(chunk)
        """ returning the JSON Response """
        for chunk in r.iter_content(chunk_size=1000000):
            return chunk

    def autocomplete(self, q):
        """
        This API supports auto-complete functionality for a search box experience in your application.

        Signature: http://api.rightrelevance.com/v2/topics/autocomplete?q=<string>&access_token=<access_token>

        :param q: q=string: Any string for which suggested topics are needed.
        :return: JSON String of the topic.

        """
        payload = {'query':q,'access_token':self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/topics/autocomplete",params=payload,stream=True)
        #with open('autocomplete_file.txt','w') as outfile:
        #    for chunk in r.iter_content(chunk_size=1):
        #        outfile.write(chunk)
        """ returning the JSON Response """
        for chunk in r.iter_content(chunk_size=1000000):
            return chunk

api_obj = Api()	 # object of class Api.
api_obj.articles('data', 0, 1)  # Data Extraction from articles API which is stored in a file called 'art_file.txt'
