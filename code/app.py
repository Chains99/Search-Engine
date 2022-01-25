from glob import escape
from pydoc import doc
from flask import Flask,render_template, request
import time
from program import *

initialize()

app = Flask(__name__)


@app.route("/")
def search():
    return render_template('index.html')

@app.route("/search_results")
def search_results():
    global docs
    query=request.args.get('query')
    inicio=time.time()
    docs_len=run_program(query)
    final=time.time()
    len_=docs_len[0]
    docs=docs_len[1]
    min_len=min(len(docs),20)
    return render_template('search_results.html',query=query,time=str(final-inicio)[:4],docs=docs[:min_len],len=len_)

@app.route("/doc/<int:index>")
def doc(index):
    return render_template('doc.html',doc=docs[index][1])