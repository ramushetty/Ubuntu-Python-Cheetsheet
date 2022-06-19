# Flask Initialization

```
from flask import Flask
app = Flask(__name__)
```
> Flask uses **__name__** build in variable to determine the location of the application 
The web server passes all
requests it receives from clients to this object for handling, using a protocol called
Web Server Gateway Interface (WSGI, pronounced “wiz-ghee”).

# Route
>The association between URLs and function that handles it is called a Route
>Flask instance keep track of this mappings of URLs to Python functions

 ```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Hello World!</h1>"
```
# Development Web Server
## Linux
```
(venv) $ export FLASK_APP=hello.py
(venv) $ flask run
```
## Windows
```
(venv) $ set FLASK_APP=hello.py
(venv) $ flask run
```

old version of running flask
```
if __name__ == '__main__':
app.run()
```
# Dynamic Routes

 ```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Hello World!</h1>"
@app.route("/user/<name>")
def user(name):
  return "<h1>Hello, {}!</h1>".format(name)
```

# Debug Mode
> Reloader and debugger
> Relaoder for automatically reload application with new changes in source code
> Debugger - gives the interactive stack trace of unhandled exceptions
by default debug mode is disabled
```
(venv) $ export FLASK_APP=hello.py
(venv) $ export FLASK_DEBUG=1
(venv) $ flask run
```
or 
```
app.run(debug=True)
```
> never enable debug mode in production server
# Command-Line Options
```
(venv) $ flask --help
```
```
$ flask shell
```
flask shell is used to start the Python shell session in the context of the application 
```
(venv) $ flask run --help
```
Public accessible web server from any computer in network
```
(venv) $ flask run --host 0.0.0.0
```

# Request-Response Cylce 
Request object encapsulates the HTTP request sent by the client 
## Application and Request Contexts
Flask uses contexts to temporarily make certain objects globally accessible --> this also avoid cluttering view functions with lot of arguments 
```
from flask import request
@app.route('/')
def index():
 user_agent = request.headers.get('User-Agent')
 return '<p>Your browser is {}</p>'.format(user_agent)
```
> Contexts enable Flask to make certain varaibles globally accessible to a thread with out interfering with the other threads

# Thread
Thread is the smallest sequence of instructions that can be managed independently.
Prcoess -consists of multiple active threads sharing resources 
Multithreaded web servers start a pool of threads and select  a thread from the pool to handle each incoming request 
 
