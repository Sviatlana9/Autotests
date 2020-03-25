import unittest
import requests
import random

random_pet_id = random.randint(5,1000)
SUCCESS_CODE = 200
url = "https://petstore.swagger.io/v2"





class TestPets3(unittest.TestCase):
	def test_update_an_existing_pet_random_id(self):
		pet_id = random_pet_id
		name = "dog"
		body = '{"id": '+str(pet_id)+',"category": {"id": '+str(pet_id)+ ',"name" : "category"},"name": "pet_name","photoUrls": [    "string"  ],  "tags": [    {      "id": 1,      "name": "tag_name"    }  ],  "status": "available"}'
		headers = {
				'accept': 'application/json',
				'Content-Type': 'application/json'
			}
		r = requests.put(url + "/pet", headers = headers, data = body)
		self.assertEqual(r.status_code, SUCCESS_CODE)
		r1 = requests.put(url + "/pet/" + str(pet_id))
		print(r1.url)
		

	def test_update_an_existing_pet(self):
		id = 9
		name = "cat"
		body = '{"id": '+str(id)+',"category": {"id": '+str(id)+ ',"name" : "category"},"name": "pet_name","photoUrls": [    "string"  ],  "tags": [    {      "id": 1,      "name": "tag_name"    }  ],  "status": "available"}'
		headers = {
				'accept': 'application/json',
				'Content-Type': 'application/json'
			}
	
		r = requests.put(url + "/pet", headers = headers, data = body)
		self.assertEqual(r.status_code, SUCCESS_CODE)
		r1 = requests.put(url + "/pet/" + str(id))
		print(r1.url)


	

if __name__ == "__main__":
	unittest.main()