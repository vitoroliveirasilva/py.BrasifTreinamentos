from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class EmpresaForm(FlaskForm):
    nome_empresa = StringField('Nome', validators=[DataRequired(), Length(max=50)])
    filial = SelectField('Filial', choices=[("Selecione uma filial")], validators=[DataRequired()])
    status = BooleanField('Ativo', default=True)
    submit = SubmitField('Salvar')
