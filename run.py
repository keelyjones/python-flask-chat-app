import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

@app.route('/<username>')# angle brackets mean this gets treated as a variable
def user(username):
    return "Hi " + username

@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)# returns a string of username: message with .format method

app.run(host='0.0.0.0', port=5000, debug=True) # slightly amended for github
'''
This line makes your python app (all of the code written in the file before it) run on the server. You pass it three parameters:
Host: This parameter tells gitpod which online server to run the app on. In this case it will be 0.0.0.0, which tells it to run on the current server (i.e. Gitpod).
Port: So you can think of a port like a... port. Instead of ships coming in and loading/unloading, it's data.
Each server could have hundreds of applications running, and the port number is a way of making each unique.
So the service running on www.google.com:8000 can be completely different than the one running on www.google.com:8001.
The port that we generally use for flask is 5000. The data for each unique app comes in and out of its unique port.
Debug: This is just a flag to print out detailed error messages if you get an error. You don't want this when your site is deployed for final use because these detailed messages can give away secrets/info that you want to keep private.
'''
