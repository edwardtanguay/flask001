from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
	return '''
	<h1>Flask 001</h1>	
	<p>[<a href="/french">French</a>] | [<a href="/">English</a>]
	<p>This is a Python/Flask showcase site.</p>
'''

@app.route("/french")
def hello_world_french():
	return '''
	<h1>Flask 001</h1>	
	<p>[<a href="/french">French</a>] | [<a href="/">English</a>]
	<p>C'est un site Python/Flask.</p>
'''

if __name__ == "__main__":
    app.run(port=3727)

