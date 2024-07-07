from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_World():
	return '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Flask 001</title>
</head>
<body>
	<h1>Flask 001</h1>	
	<p>This is a Python/Flask showcase site.</p>
</body>
</html>'''

if __name__ == "__main__":
    app.run(port=3727)

