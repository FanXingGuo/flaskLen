from flask import Flask,url_for
from flask_restful import Api,Resource,reqparse,inputs,fields,marshal_with
app=Flask(__name__)
api=Api(app)

@app.route("/")
def index():
    return "Hello World !"

class LoginView(Resource):
    def post(self,username=None):
        parser=reqparse.RequestParser()
        parser.add_argument("username",type=str,help="用户名验证错误")
        parser.add_argument("password",type=str,help="用户密码验证错误")
        parser.add_argument("home_page",type=inputs.url,help="个人中心验证错误")
        parser.add_argument("phone",type=inputs.regex(r'1[3,5,7,8]\d{9}'))
        args=parser.parse_args()
        print(args)
        if username:
            return {"msg":username}
        else:
            return {"msg":"zhiliao"}
api.add_resource(LoginView,"/login/",endpoint="login")

class Article(object):
    def __init__(self,title,content):
        self.title=title
        self.content=content
article=Article("abc",'xxx')

# restful 标准化返回参数
class ArticleView(Resource):
    resource_fields={
        "title":fields.String,
        "content":fields.String
    }
    @marshal_with(resource_fields)
    def post(self):
        return article
api.add_resource(ArticleView,"/article/",endpoint="article")



with app.test_request_context():
    print(url_for("login",username="213"))

if __name__=="__main__":
    app.run(debug=True)