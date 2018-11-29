from flask import Flask
import config
from exts import db
from models import User

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)



@app.route("/")
def index():
    user=User.query.get(1)
    return "hello %s"%user.name

if __name__ == '__main__':
    app.run(debug=True)

