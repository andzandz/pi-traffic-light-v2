# Import the Flask module so we can run a Python web server
from flask import Flask

# Import the file "traffic_light.py" so we can use the functions defined within it
# The GPIO setup at the top of traffic_light.py is executed at this point
import traffic_light

app = Flask(__name__)

# A function that returns some HTML/CSS with a customisable message (text)
def add_styling(text):
  return """<style>body{font-size:5em; text-align:center}</style><body>
    <br>
    <a href='/r'>red</a><br><br>
    <a href='/ry'>red-yellow</a><br><br>
    <a href='/y'>yellow</a><br><br>
    <a href='/g'>green</a><br><br>""" + text + "</body>"

# The method decorator (line beginning with @) tells Flask to call this method when a user browses to the defined URL 
# (just "/" is the home page at 192.168.1.1)
@app.route("/")
def hello():
  return add_styling("Hello! Click a link above, or navigate to /r, /ry, /y or /g")

# This one is called when a user browses to the URL: http://192.168.1.1/r
@app.route("/r")
def red():
  # Call the "red()" function from traffic_light.py
  traffic_light.red()
  # Output the HTML that add_styling(...) returns, to the user's browser
  return add_styling("Now it's red")

@app.route("/ry")
def red_yellow():
  traffic_light.red_yellow()
  return add_styling("Now it's red-yellow")
 
@app.route("/y")
def yellow():
  traffic_light.yellow()
  return add_styling("Now it's yellow")

@app.route("/g")
def green():
  traffic_light.green()
  return add_styling("Now it's green")
