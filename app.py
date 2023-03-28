from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posty', methods=['POST'])
def posty():
      return render_template('posty.html')

app.static_folder = 'static'
app.add_url_rule('/static/css/<path:filename>', endpoint='css', view_func=app.send_static_file)