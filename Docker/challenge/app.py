from flask import Flask
import redis
import os

app = Flask(__name__)

# configure redis connection
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))

# initialize redis client
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

# create homepage route
@app.route("/")
def home():
    return "Welcome to the CoderCo Containers!"

# create count route  to track visits
@app.route("/count")
def count():
    visits = r.incr("visit_count")
    return f"This /count page has been visited {visits} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)