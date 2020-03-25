import unittest
import requests
import random


url = "https://petstore.swagger.io/v2"
status_sold = 200
status_available = 200
status_pending = 200
random_pet_id = random.randint(5,1000)


class TestPets3(unittest.TestCase):

		
	def test_find_pet_by_status_sold(self):
		r = requests.get(url + "/pet/findByStatus?status=sold" )
		self.assertEqual(r.status_code, status_sold)

	def test_find_pet_by_status_available(self):
		r = requests.get(url + "/pet/findByStatus?status=available" )
		self.assertEqual(r.status_code, status_available)

	def test_find_pet_by_status_pending(self):
		r = requests.get(url + "/pet/findByStatus?status=pending" )
		self.assertEqual(r.status_code, status_pending)

	def test_find_pet_by_status_sold_id(self):
		r = requests.get(url + "/pet/findByStatus?status=sold" + str(random_pet_id) )
		self.assertEqual(r.status_code, status_sold)


	def test_find_pet_by_status_available_id(self):
		r = requests.get(url + "/pet/findByStatus?status=available" + str(random_pet_id) )
		self.assertEqual(r.status_code, status_available)

	def test_find_pet_by_status_pending_id(self):
		r = requests.get(url + "/pet/findByStatus?status=pending" + str(random_pet_id) )
		self.assertEqual(r.status_code, status_pending)


if __name__ == "__main__":
	unittest.main()