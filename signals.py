from blinker import Namespace
from flask import request,g
from datetime import datetime

test=Namespace()
login_signal=test.signal("login")

def login_log(sender):
    now=datetime.now()
    ip=request.remote_addr
    log_line="{username}-{time}-{ip}\n".format(time=now,ip=ip,username=g.username)
    with open("login_log.txt","a",encoding="utf-8") as file:
        file.write(log_line)

login_signal.connect(login_log)
