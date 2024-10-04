from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class InscricaoColaboradorForm(FlaskForm):
    filial = SelectField('Filial', choices=[(-1, "Selecione uma filial")], validators=[DataRequired()])
    id_colaborador = SelectField('Colaborador', choices=[(-1, "Selecione um colaborador")], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Registrar inscrição')
