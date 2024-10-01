from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class TreinamentoForm(FlaskForm):
    id_marca = SelectField('Marca', coerce=int, validators=[DataRequired()])
    treinamento = StringField('Treinamento', validators=[DataRequired()])
    descricao = TextAreaField('Descrição')
    status = BooleanField('Ativo', default=True)
    submit = SubmitField('Salvar Alterações')
