import flask
from flask import request
from flask import jsonify
from flask import Flask, render_template, url_for
from tasks import get_links
from tasks import pred
import redis
from rq import Queue

app=Flask(__name__)
r = redis.Redis()

q = Queue(connection=r)

@app.route('/')
def index():
    return render_template('text_sum.html')

@app.route('/pred', methods=['POST'])
def pred():
    if request.method=='POST':
        links = q.enqueue(get_links)
        head_sum, text_sum=q.enqueue(pred, links) 
    return render_template('text_sum.html', head_sum=head_sum, text_sum=text_sum)


if __name__ == "__main__":
    app.run()