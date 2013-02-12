import unittest
import passerelle


class PasserelleTestCase(unittest.TestCase):
	def setUp(self):
		passerelle.app.testing = True
		self.client = passerelle.app.test_client()
	
	def tearDown(self):
		pass
	
	def test_no_params_sent(self):
		response = self.client.post('/')
		assert response.status_code == 400
		assert response.status == "400 Git URLs Not Sent With Request"

	def test_one_param_sent(self):
		response = self.client.post('/?from=foo')
		assert response.status_code == 400
		assert response.status == "400 Git 'to' URL Not Sent"
		response = self.client.post('/?to=bar')
		assert response.status_code == 400
		assert response.status == "400 Git 'from' URL Not Sent"
	

if __name__ == '__main__':
    unittest.main()
