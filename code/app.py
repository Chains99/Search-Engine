from glob import escape
from pydoc import doc
from flask import Flask,render_template, request
import time
from program import *
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

app = Flask(__name__)
initialize()
print('Hola')



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
    return render_template('search_results.html',query=query,time=final-inicio)