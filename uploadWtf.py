from flask import Flask,request,render_template,send_from_directory
import os
from forms import fileForm
from werkzeug.datastructures import CombinedMultiDict

app=Flask(__name__)

PATH=os.path.dirname(__file__)
FILEPATH=os.path.join(PATH,"static")
@app.route("/upload/",methods=['GET','POST'])
def upload():
    if request.method=='GET':
        return render_template('upload.html')
    else:
        # desc=request.form.get('desc')
        # avatar=request.files.get('avatar')
        form=fileForm(CombinedMultiDict([request.form,request.files]))
        if form.validate():
            avatar=form.avatar.data
            desc=form.desc.data
            avatar.save(PATH+"/static/"+avatar.filename)
            print(desc)
            return "上传成功"
        else:
            return "文件验证失败"
@app.route("/static/<filename>")
def getfile(filename):
    return send_from_directory(FILEPATH,filename)

if __name__=='__main__':
    app.run(debug=True)


