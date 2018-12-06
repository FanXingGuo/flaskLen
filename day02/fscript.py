from flask import Flask

from day02.exts import db
from icbc import config

app=Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route("/")
def index():
    return "Hello World !"

if __name__=="__main__":
    app.run(debug=True)