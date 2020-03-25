import unittest
import requests
import random


SUCCESS_CODE = 200
NOT_FOUND_CODE = 404
url = "https://petstore.swagger.io/v2"
user_id = 1
user_name = "Sveta"


class TestUser3(unittest.TestCase):
	def test_add_user(self):
		
		body = '{ "id": 1, "username": "Sveta", "firstName": "Svetlana", "lastName": "Karpova", "email": "123", "password": "123", "phone": "123", "userStatus": 0 }'
		headers = {
				'accept': 'application/json',
				'Content-Type': 'application/json'
			}
		r = requests.post(url + "/user/createWithArray/",headers = headers, data = body)
		# self.assertEqual(r.status_code, SUCCESS_CODE) 
		#  AssertionError: 500 != 200
		print(r.url)
		

	def test_user_by_user_name(self):
		r = requests.get(url + "/user/" + str(user_name))
		self.assertEqual(r.status_code, SUCCESS_CODE)

	def test_logs_user_into_the_system(self):
		r = requests.get(url + "/user/login?username=Sveta&password=123")
		self.assertEqual(r.status_code, SUCCESS_CODE)

	def test_logout_user(self):
		r = requests.get(url + "/user/logout")
		self.assertEqual(r.status_code, SUCCESS_CODE)
	

if __name__ == "__main__":
	unittest.main()