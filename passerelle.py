import os
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods=["POST"])
def git2git():
	return Response(response="yay", status=200)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	if port == 5000:
		app.debug = True
	app.run(host='0.0.0.0', port=port)
