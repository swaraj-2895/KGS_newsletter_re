from flask import request
from flask import jsonify
from flask import Flask, render_template, url_for
import rq
from rq import Queue
from worker import conn
from utils import pred, get_links

q = Queue(connection=conn)
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('text_sum.html')

@app.route('/pred', methods=['POST'])
def pred():
    if request.method=='POST':
        links = q.enqueue(get_links)
        head_sum, text_sum=q.enqueue(pred, links) 
    return render_template('text_sum.html', head_sum=head_sum, text_sum=text_sum)

if __name__=='__main__':
    app.run() #add threaded=True