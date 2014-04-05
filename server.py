from flask import Flask, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def chat_room():
	return render_template('chat.html')

@app.route("/test", methods=["POST"])
def test():
	return request.form["message_box"]

if __name__ == "__main__": 	
	app.debug = True
	app.run()

