from flask import Flask,request,Response
from datetime import datetime,timedelta
from cmsviews import bp
app=Flask(__name__)
app.register_blueprint(bp)
app.config['SERVER_NAME']="xg.com:5000"

@app.route("/")
def index():
    resp=Response("设置cookie")
    resp.set_cookie("username","xingguo")
    return resp

@app.route("/del/")
def del_cookie():
    resp=Response("删除cookie")
    resp.delete_cookie("username")
    return resp

@app.route("/setct/")
def set_ct():
    resp=Response("设置cookie有效期")
    resp.set_cookie("username","xingguo",max_age=120)
    return resp
@app.route("/setct1/")
def set_ct1():
    resp=Response("设置cookie有效期")
    expires=datetime.now()+timedelta(days=30,hours=16)
    resp.set_cookie("username","xingguo",expires=expires)
    return resp

@app.route("/domain/")
def cookie_d():
    resp=Response("子域名cookie")
    resp.set_cookie("name","hao",max_age=1000,domain=".xg.com")
    return resp


if __name__=='__main__':
    app.run(debug=True)
