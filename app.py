from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
	return '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Flask 001</title>
</head>
<body>
	<h1>Flask 001</h1>	
	<p>[<a href="/french">French</a>] | [<a href="/">English</a>]
	<p>This is a Python/Flask showcase site.</p>
</body>
</html>'''

@app.route("/french")
def hello_world_french():
	return '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Flask 001</title>
</head>
<body>
	<h1>Flask 001</h1>	
	<p>[<a href="/french">French</a>] | [<a href="/">English</a>]
	<p>C'est un site Python/Flask.</p>
</body>
</html>''' 

@app.route("/product/<id>")
def product_id(id):
	return f"You are viewing product #{id}"

@app.route("/welcome")
def temp1():
	return render_template("main.html", pageTitle = "Welcome")

if __name__ == "__main__":
    app.run(port=3727, debug=True)

