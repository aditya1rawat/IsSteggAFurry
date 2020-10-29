from flask import Flask, redirect, render_template
import json

#Init App
app = Flask(__name__)

#Load config
with open('config.json') as config_file:
	config = json.loads(config_file.read())

#Load counter
with open(config['PATH'], 'r+') as count_file:
	_json = json.loads(count_file.read())
	count = _json['count']
	daily = _json['daily']
print(count)

#Increment Counter
def increment():
	global count, daily
	count = count + 1
	daily = daily + 1
	with open(config['PATH'], 'r+') as count_file:
		json.dump({'count': count, 'daily': daily}, count_file)
	return (count, daily)

#Routes

@app.errorhandler(404)
def page_not_found(e):
	return redirect('/furry'), 404, {'Refresh': '0; url=/furry'}

@app.route('/about')
def about():
	global count, daily
	return render_template('about.html', count=(count, daily), titles=config['TITLES'])

@app.route('/furry')
def furry():
	return render_template('index.html', count=increment(), titles=config['TITLES'])


#Init App
if __name__ == '__main__':
	app.run(port=8080, debug=True)