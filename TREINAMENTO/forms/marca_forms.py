from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class MarcaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    id_tipo = SelectField('Tipo', coerce=int, validators=[DataRequired()])
    status = BooleanField('Ativo', default=True)
    submit = SubmitField('Salvar')
