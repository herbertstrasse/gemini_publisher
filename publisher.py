import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template('publisher.html')

@app.route('/', methods=['POST'])
def application():
    title = request.form['title']
    heading1 = request.form['heading1']
    heading2 = request.form['heading2']
    body = request.form['body']




if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=9999, type=int, help='port to listen on')

    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port)
