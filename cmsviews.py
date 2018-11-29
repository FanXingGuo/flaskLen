from flask import Blueprint,request

bp=Blueprint("cms",__name__,subdomain="cms")

@bp.route("/")
def index():
    data=request.cookies.get("name")
    print(data)
    return  data or "无cookie信息"