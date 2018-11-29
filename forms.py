from wtforms import StringField,Form,validators,FileField
from wtforms.validators import Regexp,Length,EqualTo,ValidationError,InputRequired
from flask_wtf.file import FileRequired,FileAllowed

class fileForm(Form):
    avatar=FileField(validators=[FileRequired(),FileAllowed(['jpg','png','gif'])])
    desc=StringField(validators=[InputRequired()])

class registerForm(Form):
    username = StringField(validators=[Length(min=3, max=6, message="长度为3-6个字符")])
    password = StringField(validators=[Length(min=6, max=10, message="密码长度6-10个字符")])
    repeat_password = StringField(validators=[Length(min=6, max=10, message="密码长度6-10个字符")
        , EqualTo("password", message="两次密码输入必须一致")])

class phoneForm(Form):
    phone=StringField(validators=[Regexp(r'1[3578]\d{9}')])

class captchaForm(Form):
    captcha=StringField(validators=[Length(min=4,max=4)])
    def validate_captcha(self,field):
        if field.data !='1234':
            print()
            raise ValidationError("验证码错误!")



