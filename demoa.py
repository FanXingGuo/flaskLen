from flask import Flask
import config
from exts import db
from models import User

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)



@app.route("/")
def index():
    user=User(name="zhang")
    db.session.add(user)
    db.session.commit()
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)