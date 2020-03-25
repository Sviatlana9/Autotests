import unittest
import requests
import random

random_pet_id = random.randint(5,1000)
SUCCESS_CODE = 200
NOT_FOUND_CODE = 404
url = "https://petstore.swagger.io/v2"
exist_pet_id = 1




class TestPets3(unittest.TestCase):
	def test_add_pet_to_store(self):
		pet_id = random_pet_id
		body = '{"id": '+str(pet_id)+',"category": {"id": '+str(pet_id)+ ',"name" : "category"},"name": "pet_name","photoUrls": [    "string"  ],  "tags": [    {      "id": 1,      "name": "tag_name"    }  ],  "status": "available"}'
		headers = {
				'accept': 'application/json',
				'Content-Type': 'application/json'
			}
		r = requests.post(url + "/pet", headers = headers, data = body)
		self.assertEqual(r.status_code, SUCCESS_CODE)
		r1 = requests.get(url + "/pet/" + str(pet_id))
		print(r1.url)
		self.assertEqual(r1.status_code, SUCCESS_CODE)
		
	def test_find_pet_by_id(self):
		r = requests.get(url + "/pet/" + str(exist_pet_id))
		self.assertEqual(r.status_code, SUCCESS_CODE)

	def test_find_pet_by_id_negative(self):
		negative_list = [99999999, "asd", " "]
		for i in negative_list:
			r = requests.get(url + "/pet/" + str(i))
			self.assertEqual(r.status_code, NOT_FOUND_CODE)


	

if __name__ == "__main__":
	unittest.main()