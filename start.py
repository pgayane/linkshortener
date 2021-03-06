from flask import Flask
from flask import render_template
from flask import request, redirect
import random, requests, dinologic

app = Flask(__name__)



@app.route('/<key>')
def redir_Url(key):
    #redir
    # calls something in dinologic to get the full url, then goes to that website
    url = dinologic.get_url(key)
    if url is not '':
      return redirect('http://' + url, code = 302)
    else:
        return 'Error: id does not exsist'

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        url = request.form['linkbox']
        
        tiny_url = dinologic.make_tiny(url, request.host)
        return render_template('redir.html', long_url = 'http://'+url, tiny_url = tiny_url)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
    
