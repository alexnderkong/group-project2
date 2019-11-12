from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class NameForm(FlaskForm):
    first_name = StringField('first name: ', validators=[DataRequired(), Length(min=2, max=100)])
    last_name = StringField('last name: ', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('submit')