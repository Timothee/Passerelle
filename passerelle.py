import os
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

	return Response(response="yay", status=200)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	if port == 5000:
		app.debug = True
	app.run(host='0.0.0.0', port=port)
