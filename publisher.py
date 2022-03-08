import subprocess, re, json

from flask import Flask, render_template, request
from datetime import date


def fetch_index():
    print("Downloading index data from remote server...")
    try:
        subprocess.run(["scp", "andy@192.168.50.2:/opt/gemini/backend/index.json", "index.json"])
        print("Index pulled from remote server...")
    except:
        print("An error occurred pulling index data.")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template('publisher.html')

@app.route('/', methods=['POST'])
def application():
    filename = request.form['filename']
    title = request.form['title']
    description = request.form['description']
    body = request.form['textbody']

    filename = filename.replace(" ", "_")
    filename = re.sub(r'[^\w]', '', filename)
    filename = filename + ".gmi"
    print(filename)
    
    with open(filename, 'w') as new_file:
        title = "#" + title + "\n"
        body = body
        total = title+body
        total = total.replace('\r', '')

        new_file.write(total)

    with open('index.json') as f:
            json_data = json.load(f)
            print("Json data loaded from pulled file")
    
    with open('index.json', 'w') as json_file:
        json_data['entries'].append({'date' : str(date.today()), 'description' : description, 'filename' : filename})
        json.dump(json_data, json_file)

    
    scp_path = "andy@192.168.50.2:/opt/gemini/www/" + filename
    subprocess.run(["scp", filename, scp_path])

    scp_path2 = "andy@192.168.50.2:/opt/gemini/backend/index.json"
    subprocess.run(["scp", "index.json", scp_path2])

    return 'OK'


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=9999, type=int, help='port to listen on')

    args = parser.parse_args()
    port = args.port
    
    fetch_index()
    print("Serving web application...")
    app.run(host='127.0.0.1', port=port)
