import requests
import httpretty

@httpretty.activate

class TestApi:

	def __init__(self):
		self.access_token = '68a98c9fe9ebfc409d7d46bd9d496561045e9d52372c8896c8f25d1d6e64e1d8'

	def test_demo(self,query,start,rows):
		payload = {'query':query,'start':start,'rows':rows,'access_token':self.access_token}
		r = requests.get("http://api.rightrelevance.com/v2/articles/search",params=payload)
		httpretty.register_uri(httpretty.GET,r.url,body="json response successful",content_type='application/json')
		response = r

		print "The Status Code:"+str(response.status_code)
		print response.content
		assert response.status_code == 200
		

	def test_articles_api(self,query,start,rows):
		payload = {'query':query,'start':start,'rows':rows,'access_token':self.access_token}
		r = requests.get("http://api.rightrelevance.com/v2/articles/search",params=payload)
		httpretty.register_uri(httpretty.GET,r.url,body="json response successful",content_type='application/json')
		response = r

		print "The Status Code:"+str(response.status_code)
		# print response.content	
		assert response.status_code == 200
		

	def test_influencers_api(self,query,start,rows):
		payload = {'query':query,'start':start,'rows':rows,'access_token':self.access_token}
		r = requests.get("http://api.rightrelevance.com/v2/experts/search",params=payload)
		httpretty.register_uri(httpretty.GET,r.url,body="json response successful",content_type='application/json')
		response = r

		print "The Status Code:"+str(response.status_code)
		# print response.content	
		assert response.status_code == 200
		

	def test_conversations_api(self,query,page,rows,order):
		payload = {'query':query,'page':page,'rows':rows,'order_by':order,'access_token':self.access_token}
		r = requests.get("http://api.rightrelevance.com/v2/conversations/search",params=payload)
		httpretty.register_uri(httpretty.GET,r.url,body="json response successful",content_type='application/json')
		response = r

		print "The Status Code:"+str(response.status_code)
		# print response.content	
		assert response.status_code == 200
		

	def test_autocomplete_api(self,q):
		payload = {'query':q,'access_token':self.access_token}
		r = requests.get("http://api.rightrelevance.com/v2/topics/autocomplete",params=payload)
		httpretty.register_uri(httpretty.GET,r.url,body="json response successful",content_type='application/json')
		response = r

		print "The Status Code:"+str(response.status_code)
		# print response.content	
		assert response.status_code == 200
		

test_obj = TestApi()
test_obj.test_demo('django',0,1)
# test_obj.test_articles_api('data',0,1)
# test_obj.test_influencers_api('data',0,1)
# test_obj.test_conversations_api('data',0,1)
