from flask import Flask
import os
import socket

app = Flask(__name__)
counter = 0

print('Server stats:', counter, __name__)

@app.route('/')
def show_counter():
    print('Hello!')
    html = "<h3>Счётчик:{counter}</h3>"
    return html.format(counter=counter)

@app.route('/stat')
def increment():
    global counter
    old_counter = counter
    counter += 1
    html = "<h3>Счётчик:{counter}</h3>"
    return html.format(counter=old_counter)

@app.route("/about")
def hello():
    html = "<h3>Hello, Marina Agafonova!</h3><b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

from flask import Flask
app = Flask(__name__)