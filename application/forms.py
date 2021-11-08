from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField



class add_player(FlaskForm):
    submit = SubmitField('Add Player')
    pass

    
    
class update_player(FlaskForm):
    submit = SubmitField('Update Player')
    pass



