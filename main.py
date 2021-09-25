from flask import Flask, request, jsonify
from replit import db
import random
db.clear()
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/input', methods = ['GET', 'POST'])
def input():
  num = random.randint(0, 10000)
  name = request.args.get('name')
  heading = request.args.get('heading')
  desc = request.args.get('desc')
  reward = request.args.get('reward')
  lst = [name, heading, desc, reward]
  db[str(num)] = lst
  return "check"

@app.route('/output', methods = ['GET', 'POST'])
def output():
  output = []
  for i in db:
    name = db[i][0]
    heading = db[i][1]
    desc = db[i][2]
    reward = db[i][3]
    dict = {
      "name": name,
      "heading": heading,
      "description": desc,
      "reward": reward
    }
    output.append(dict)
  print(output)
  return jsonify(dict)

app.run(host='0.0.0.0', port=8080)