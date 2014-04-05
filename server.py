from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route("/")
def chat_room():
	return render_template('chat.html')

if __name__ == "__main__": 	
	app.run()

