from flask import Flask, render_template, url_for, request
import requests
import json


posts_url = "https://jsonplaceholder.typicode.com/posts"
users_url = "https://jsonplaceholder.typicode.com/users"
comments_url = "https://jsonplaceholder.typicode.com/comments"

posts = requests.get(posts_url).json()
users = requests.get(users_url).json()
comments = requests.get(comments_url).json()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/posty', methods=['POST'])
def posty():
    postsWithPhrases=[];
    searchterm = request.form['searchbox']
    for x in posts:
        if(x["title"].find(searchterm)!=-1):
            id = x["userId"] 
            for y in users:
                if y["id"] == id:
                    x["userId"] = y["name"]
                
            postsWithPhrases.append(x)
            
                

      
    return render_template('posty.html',posts=postsWithPhrases, users=users,comments = comments)
   

app.static_folder = 'static'
app.add_url_rule('/static/css/<path:filename>', endpoint='css', view_func=app.send_static_file)