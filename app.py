from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import os
from os import listdir
import json

@app.route('/')
def index():

  ls_file = os.listdir("./static/data_img")
  ls_file_json = os.listdir("./static/data")
  ls_return  = []

  for _file in ls_file:
    dic_data = dict()
    # preprocess string 
    _file_json = _file[:-3]+"json"
    with open("./static/data/"+ _file_json) as f:
      data_infor = json.load(f)

    dic_data["image"] = "../static/data_img/"+ _file
    dic_data["title"] = data_infor["Name"]
    dic_data["description"] = data_infor["Price"]
    ls_return.append(dic_data)

  return render_template('index_2.html', data=ls_return)

@app.route('/detail')
def detail():

  _id = request.args.get("id")
  file_name = _id[:-3]+"json"
  with open('./static/data/'+ file_name) as f: 
    data_infor = json.load(f)

  data_infor['image'] = "../static/data_img/"+_id
  return render_template('detail.html', data=data_infor)

@app.route('/home')
def home():

  ls_file = os.listdir("./static/data_img")
  ls_file_json = os.listdir("./static/data")
  ls_return  = []

  for _file in ls_file:
    dic_data = dict()
    # preprocess string 
    _file_json = _file[:-3]+"json"
    with open("./static/data/"+ _file_json) as f:
      data_infor = json.load(f)

    dic_data["image"] = "../static/data_img/"+ _file
    dic_data["title"] = data_infor["Name"]
    dic_data["description"] = data_infor["Price"]
    ls_return.append(dic_data)

  return render_template('index_2.html', data=ls_return)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
