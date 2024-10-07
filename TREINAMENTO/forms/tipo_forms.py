from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class TipoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=50)])
    status = BooleanField('Ativo', default=True)
    submit = SubmitField('Salvar')
