from flask import Flask,request,g,abort,render_template
from signals import login_signal

app=Flask(__name__)

with app.app_context():
    print(123)


@app.route("/")
def index():
    user=request.args.get("username")
    if user:
        g.username=user
        login_signal.send()
        if user=='123':
            abort(500)
        return "欢迎回来%s"%user
    else:
        return "请您登录"
@app.route("/i/")
def iindex():
    return render_template("index.html")

@app.errorhandler(500)
def server_error(errors):
    return "服务器正在打盹",500

@app.context_processor
def content_processor():
    return {"username":"123"}

if __name__=="__main__":
    app.run(debug=True)