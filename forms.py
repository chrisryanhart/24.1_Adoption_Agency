from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import InputRequired, URL, ValidationError, Optional

def age_check(form, field):
    if not field.data:
        return
    elif field.data < 0 or field.data >30:
        raise ValidationError('Age must be between 0-30 years')

def species_check(form,field):
    types = ['cat','dog','porcupine']
    if field.data not in types:
        raise ValidationError('Species must be cat, dog, or porcupine')


class AddPetForm(FlaskForm):
    """Form to add new pet"""
    name = StringField('Pet Name', validators=[InputRequired()])

    species = StringField('Species',validators=[InputRequired(),species_check])

    photo_url = StringField('Photo url', validators=[URL(require_tld=True,message='Must be valid URL'), Optional()])

    age = IntegerField('Age', validators=[age_check, Optional()])

    notes = StringField('Notes', validators=[Optional()])

    available = BooleanField('Available',validators=[Optional()],default='checked')

class EditPetForm(FlaskForm):
    """Edit existing pet"""
    photo_url = StringField('Photo url', validators=[URL(require_tld=True,message='Must be valid URL'), Optional()])

    notes = StringField('Notes', validators=[Optional()])

    available = BooleanField('Available',validators=[Optional()],default='checked')


    