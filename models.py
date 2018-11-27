from exts import db

class User(db.Model):
    __tablename__="user_demo1"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))
