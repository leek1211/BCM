from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required, EqualTo

class RegisterForm(Form):
  name = TextField('TeamName', [Required()])
  
