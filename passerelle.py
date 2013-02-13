import os
from urlparse import urlparse
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods=["POST"])
def git2git():
	from_url = request.args.get('from')
	to_url = request.args.get('to')

	if not from_url and not to_url:
		return Response(status="400 Git URLs Not Sent With Request")
	if not from_url:
		return Response(status="400 Git 'from' URL Not Sent")
	if not to_url:
		return Response(status="400 Git 'to' URL Not Sent")
	if not check_git_url(from_url):
		return Response(status="400 Git 'from' URL Not Acceptable")
	if not check_git_url(to_url):
		return Response(status="400 Git 'to' URL Not Acceptable")

	
	
	return Response(response="yay", status=200)

def check_git_url(url):
	''' This is a gross sanity check on git URLs
		It doesn't cover all cases but it should filter out
		obviously wrong URLs
		'''
	accepted_schemes = ['ssh', 'git', 'http', 'https', 'ftp', 'ftps',
			'rsync', 'file']
	if not url.endswith(('.git', '.git/')):
		return False
	elif url.startswith('file:///'):
		return True
	elif '://' in url:
		parsed = urlparse(url)
		return parsed.scheme in accepted_schemes and parsed.netloc != ''
	else:
		return True

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	if port == 5000:
		app.debug = True
	app.run(host='0.0.0.0', port=port)
