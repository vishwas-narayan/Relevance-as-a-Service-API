import requests
import json

class Api:
    def __init__(self):
        self.access_token = '68a98c9fe9ebfc409d7d46bd9d496561045e9d52372c8896c8f25d1d6e64e1d8'
    def articles(self,query,page,rows):
        payload = {'query':query,'page':page,'rows':rows,
         'access_token': self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/articles/search",params=payload,stream=True)
        data = r.json()
        extract = data['articles']
        with open('art_file.txt','w') as outfile:
            json.dump(extract,outfile)
    def influencers(self,query,page,rows):
        payload = {'query':query,'page':page,'rows':rows,
        'access_token':self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/experts/search",params=payload,stream=True)
        data = r.json()
        extract = data['results']
        with open('inf_file.txt','w') as outfile:
            json.dump(extract,outfile)

    def conversations(self,query,page,rows,order):
        payload = {'query':query,'page':page,'rows':rows,'order_by':order,
            'access_token':self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/conversations/search",params=payload,stream=True)
        data = r.json()
        extract = data['conversations']
        with open('conv_file.txt','w') as outfile:
            json.dump(extract,outfile)
    def autoComplete(self,q):
        payload = {'query':q,
                'access_token':self.access_token}
        r = requests.get("http://api.rightrelevance.com/v2/topics/autocomplete",params=payload,stream=True)
        data = r.json()
        extract = data['suggestions']
        with open('autocomp_file.txt','w') as outfile:
            json.dump(extract,outfile)

if __name__ == "__main__":
    api_obj = Api()
    api_obj.articles('data',0,1)
