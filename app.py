from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost',27017)
db = client.memodb

@app.route('/')
def home():
		return render_template('index.html')

@app.route('/post', methods=['POST'])
def memo_create():
		post_Title = request.form['post_Title']
		post_Body = request.form['post_Body']
		print(post_Title, post_Body)
		post = {'post_Title': post_Title, 'post_Body': post_Body}

		db.post.insert_one(post)

		return jsonify({'result': 'success'})

@app.route('/post', methods=['GET'])
def memo_read():
		result = list(db.post.find({}, {'_id': 0}))
		return jsonify({"result": "success", "post": result})

@app.route('/post/update', methods=['POST'])
def memo_update():
		post_Title = request.form['post_Title']
		post_Body = request.form['post_Body']
		post_U_Title = request.form['post_U_Title']
		print(post_Title,post_Body,post_U_Title)
		post_U_Body = request.form['post_U_Body']
		print(post_U_Title,post_U_Body)
		# uPost = db.post.find_one({'post_Title': post_Title, 'post_Body': post_Body})
		db.post.update_one({'post_Title': post_Title, 'post_Body': post_Body}, {'$set':{'post_Title':post_U_Title,'post_Body':post_U_Body}})

		return jsonify({"result":"success"})

@app.route('/post/delete', methods=['POST'])
def memo_delete():
		post_Title = request.form['post_Title']
		db.post.delete_one({"post_Title": post_Title})
		return jsonify({'result': "success"})



if __name__ == '__main__':
		app.run('127.0.0.3',port=5000,debug=True)