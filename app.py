from flask import Flask, render_template, url_for, request
import json

with open("posts.json", "r") as f:
    posts = json.load(f)

with open("comments.json", "r") as f:
    comments = json.load(f)

with open("users.json", "r") as f:
    users = json.load(f)

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