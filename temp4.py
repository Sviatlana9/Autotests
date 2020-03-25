import unittest
import requests
import random


SUCCESS_CODE = 200
url = "https://petstore.swagger.io/v2"
pet_id = 6
NOT_FOUND_CODE = 404

class TestPets3(unittest.TestCase):
	def test_delete_pet(self):
		
		body = '{"id": '+str(pet_id)+',"category": {"id": '+str(pet_id)+ ',"name" : "category"},"name": "pet_name","photoUrls": [    "string"  ],  "tags": [    {      "id": '+str(pet_id)+',      "name": "tag_name"    }  ],  "status": "available"}'
		headers = {
				'accept': 'application/json',
				'Content-Type': 'application/json'
			}
	
		
		r = requests.delete(url + "/pet/" + str(pet_id))
		self.assertEqual(r.status_code, NOT_FOUND_CODE)

		print(r.url, NOT_FOUND_CODE )


if __name__ == "__main__":
	unittest.main()