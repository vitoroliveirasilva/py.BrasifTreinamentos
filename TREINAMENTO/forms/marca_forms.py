from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class MarcaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=50)])
    status = BooleanField('Ativo', default=True)
    submit = SubmitField('Salvar')
