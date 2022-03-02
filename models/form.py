from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    todo = StringField('Todo', validators=[DataRequired('Please enter a todo item!')])
    done = BooleanField('Done')
    
    
    
    
    
    
    
    