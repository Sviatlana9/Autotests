import unittest
import requests
import random

random_pet_id = random.randint(5,1000)
NOT_FOUND_CODE = 404
url = "https://petstore.swagger.io/v2"
order_id = 5
success_code = 200

 class TestOrder(unittest.TestCase):
 	def test_place_an_order_for_a_pet(self):
 		pet_id = random_pet_id
		
 		body = '{ "id":'+str(order_id)+ ', "petId":'+str(pet_id)+ ', "quantity": 0, "shipDate": "2020-03-25T14:43:33.225Z", "status": "placed", "complete": true}'
 		headers = {
				'accept': 'application/json',
 				'Content-Type': 'application/json'# 			}
 		r = requests.post(url + "/store/order", headers = headers, data = body)
 		self.assertEqual(r.status_code, success_code)
		r1 = requests.get(url + "/store/order/" + str(order_id))
 		print(r1.url)
 		self.assertEqual(r1.status_code, success_code)
		
 	def test_find_order_by_id(self):
 		r = requests.get(url + "/store/order/" + str(order_id))
		self.assertEqual(r.status_code, success_code)
 		print(r.url)

 	def test_find_order_by_id_negative(self):
 		negative_list = [6695558, "asd", " "]
		for i in negative_list:
 			r = requests.get(url + "/store/order/" + str(i))
 			self.assertEqual(r.status_code, NOT_FOUND_CODE)
 			print(r.url)

 	def test_returns_pet_inventories_by_status(self):
 		r = requests.get(url + "/store/inventory/" + str(order_id))
		
 		print(r.url)


	

if __name__ == "__main__":
	unittest.main()
