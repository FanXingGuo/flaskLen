from flask import Flask,render_template,request
from forms import captchaForm


app=Flask(__name__)


@app.route("/")
def index():
    return "hello world"
@app.route("/register/",methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template("login.html")
    else:
        form=captchaForm(request.form)
        if form.validate():
            return "验证成功"
        else:

            return "验证失败:%s"%form.errors

if __name__=='__main__':
    app.run(debug=True)
