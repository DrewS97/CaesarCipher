from flask import Flask, render_template, request
from caesar import rotate_string
app = Flask('app')

@app.route('/')
def caesar_cipher():
  return render_template("index.html")

@app.route('/', methods=["POST"])
def encrypt():
  rot = int(request.form.get('rot'))
  text = str(request.form.get('text'))
  
  newS = rotate_string(text, rot)

  return render_template("index.html", newS = newS)


app.run(host='0.0.0.0', port=8080)