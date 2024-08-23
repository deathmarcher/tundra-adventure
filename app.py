#!/usr/bin/env python3

import argparse
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/tiles.json')
def tiles():
    return send_from_directory('.', 'tiles.json')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Tile Game Flask server.")
    parser.add_argument('-p', '--port', type=int, default=5000, help='Port to run the server on')
    args = parser.parse_args()

    app.run(debug=True, port=args.port)

