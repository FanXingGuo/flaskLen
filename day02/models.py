from day02.exts import db

class User(db.Model):
    __tablename__="user_icbc"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50),nullable=False)
    age=db.Column(db.Integer)