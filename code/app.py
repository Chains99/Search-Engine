from glob import escape
from pydoc import doc
from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def search():
    return render_template('index.html')

@app.route("/search_results")
def search_results():
    docs={

    }
    
    query=request.args.get('query')
    amor='asd'
    return render_template('search_results.html',query=query,amor=amor)