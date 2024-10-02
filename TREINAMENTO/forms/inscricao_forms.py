from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class InscricaoForm(FlaskForm):
    id_colaborador = SelectField('Colaborador', coerce=int, validators=[DataRequired()])
    id_treinamento = SelectField('Treinamento', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
