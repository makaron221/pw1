from flask_wtf import FlaskForm
from wtforms import StringField,\
PasswordField, SubmitField, BooleanField
from wtforms.validators import\
DataRequired, EqualTo

class Create_ChangeForm(FlaskForm):
    content = StringField("content", validators=[DataRequired()])

class DeleteForm(FlaskForm):
    num = StringField("num", validators=[DataRequired()])
    submit = SubmitField("submit")