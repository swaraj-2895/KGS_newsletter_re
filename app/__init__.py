from flask import Flask
import redis
from rq import Queue

app = Flask(__name__)

r = redis.Redis()

q = Queue(connection=r)

from app import app.views
from app import app.tasks
