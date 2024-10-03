from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class InscricaoForm(FlaskForm):
    id_tipo = SelectField('Tipo', choices=[(-1, "Selecione um tipo")], coerce=int, validators=[DataRequired()])
    id_marca = SelectField('Marca', choices=[(-1, "Selecione uma marca")], coerce=int, validators=[DataRequired()])
    id_treinamento = SelectField('Treinamento', choices=[(-1, "Selecione um treinamento")], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Cadastrar Inscrição')
