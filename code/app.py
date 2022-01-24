from glob import escape
from pydoc import doc
from flask import Flask,render_template, request
import time
from program import *
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

initialize()
print('Hola')
app = Flask(__name__)


@app.route("/")
def search():
    return render_template('index.html')

@app.route("/search_results")
def search_results():
    query=request.args.get('query')
    inicio=time.time()
    final=time.time()
    print(query)
    docs=run_program(query)
    return render_template('search_results.html',query=query,time=final-inicio,docs=docs[:min(len(docs),20)])