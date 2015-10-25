from flask import Flask,json,make_response

app = Flask(__name__)

@app.route("/")
def hello():
	message = {'message': "Authenticate."}
	return make_response(json.dumps(message),200)

if __name__ == "__main__":
	app.run()