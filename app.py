#!/usr/bin/env python3
import argparse

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
	return send_from_directory('.', 'index.html')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Run the Tile Game Flask server.")
	parser.add_argument('-p', '--port', type=int, default=5000, help='Port to run the server on')
	args = parser.parse_args()

	app.run(debug=True, port=args.port)




##!/usr/bin/env python3
#
#from flask import Flask, render_template, jsonify, request
#
#app = Flask(__name__)
#
## Initialize the position of the person/tracker
#tracker_position = {'x': 0, 'y': 0}
#
#@app.route('/')
#def index():
#	return render_template('index.html')
#
#@app.route('/move', methods=['POST'])
#def move():
#	global tracker_position
#	direction = request.json.get('direction')
#	if direction == 'up' and tracker_position['y'] > 0:
#		tracker_position['y'] -= 1
#	elif direction == 'down' and tracker_position['y'] < 4:
#		tracker_position['y'] += 1
#	elif direction == 'left' and tracker_position['x'] > 0:
#		tracker_position['x'] -= 1
#	elif direction == 'right' and tracker_position['x'] < 4:
#		tracker_position['x'] += 1
#
#	return jsonify(tracker_position)
#
