from glob import escape
from pydoc import doc
from flask import Flask,render_template, request
import time
from program import run_program

app = Flask(__name__)

@app.route("/")
def search():
    return render_template('index.html')

@app.route("/search_results")
def search_results():
    query=request.args.get('query')

    inicio=time.time()
    final=time.time()
    docs=run_program(query)


    return render_template('search_results.html',query=query,time=final-inicio,docs=docs[:10])