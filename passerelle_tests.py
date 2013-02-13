import unittest
import passerelle


class PasserelleTestCase(unittest.TestCase):
	def setUp(self):
		passerelle.app.testing = True
		self.client = passerelle.app.test_client()
		self.correct_urls = ['ssh://user@host.com:8080/path/to/repo.git/',
				'ssh://user@host.com:8080/~user/path/to/repo.git/',
				'git://host.com:8080/path/to/repo.git',
				'git://host.com:8080/~user/path/to/repo.git',
				'https://host.com:8080/path/to/repo.git',
				'ftp://host.com:8080/path/to/repo.git',
				'rsync://host.com:8080/path/to/repo.git',
				'git@host.com:username/repo.git',
				'host.com/~/path/to/repo.git',
				'/path/to/repo.git/',
				'file:///path/to/repo.git']
		self.wrong_urls = ['host.com/repo',
				'rtmp://whatisthis.com/really.git']
	
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
	
	def test_proper_git_urls(self):
		for url in self.correct_urls:
			assert passerelle.check_git_url(url) is True
		for url in self.wrong_urls:
			assert passerelle.check_git_url(url) is False

	def test_status_with_bad_git_urls(self):
		response = self.client.post(query_string={'from':
			self.wrong_urls[0], 'to': self.correct_urls[0]})
		assert response.status_code == 400
		assert response.status == "400 Git 'from' URL Not Acceptable"
		response = self.client.post(query_string={'from':
			self.correct_urls[0], 'to': self.wrong_urls[0]})
		assert response.status_code == 400
		assert response.status == "400 Git 'to' URL Not Acceptable"

if __name__ == '__main__':
    unittest.main()
