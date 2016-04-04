import pytest

@pytest.mark.django_db

class TestResponse:
	def test_demo(self,client):
		response = client.get('/data/',follow=True)
		print response.content 
		assert response.status_code == 200
	
	def test_articles(self,client):
		response = client.get('/data/articles',follow=True)
		print response.content
		assert response.status_code == 200

	def test_influencers(self,client):
		response = client.get('/data/influencers',follow=True)
		print response.content
		assert response.status_code == 200

	def test_conversations(self,client):
		response = client.get('/data/conversations',follow=True)
		print response.content
		assert response.status_code == 200

	def test_autocomplete(self,client):
		response = client.get('/data/autocomplete',follow=True)
		print response.content
		assert response.status_code == 200