from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app=Flask(__name__)
app.config.from_object(config)
db=SQLAlchemy(app)

class User(db.Model):
    __tablename__="user_demo2"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))

# db.create_all()
# user=User(name="liu")
# db.session.add(user)
# db.session.commit()

# user=User.query.filter_by(name="liu").first()

# user=User.query.first()
# db.session.delete(user)
# db.session.commit()

# user=User.query.first()
# user.name="fan"
# db.session.commit()


@app.route("/")
def index():

    return "hello "

if __name__=="__main__":
    app.run(debug=True)