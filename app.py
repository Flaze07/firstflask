from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def enter_name():
		return render_template('index.html')

@app.route('/hello', methods=['POST', 'GET'])
def hello_user():
	if request.method == 'POST':
		return render_template('other.html', user=request.form['name'])
	else:
		return render_template('other.html', user='fuckng hacker')

if __name__=='__main__':
	app.run(host='127.0.0.1', port=8000)