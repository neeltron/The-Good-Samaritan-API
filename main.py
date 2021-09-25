from flask import Flask, request, jsonify
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/input', methods = ['GET', 'POST'])
def input():
  name = request.args.get('name')
  heading = request.args.get('heading')
  desc = request.args.get('desc')
  reward = request.args.get('reward')
  dict = {
    "name": name,
    "heading": heading,
    "description": desc,
    "reward": reward
  }
  return jsonify(dict)

app.run(host='0.0.0.0', port=8080)