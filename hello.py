from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World Index page"

@app.route("/<message>")
def show_message(message):
	return "Hello World ! %s"%message

"""@app.route("/<path:p>")
def zzz():
	return redirect('/')"""

@app.errorhandler(404) 
def page_not_found(e): 
	# your processing here return result
	return redirect('/')

if __name__ == "__main__":
    app.run()
