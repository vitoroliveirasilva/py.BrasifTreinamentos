from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
from TREINAMENTO.models.enum_filiais import Filiais

class EmpresaForm(FlaskForm):
    nome_empresa = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    filial = SelectField('Filial', choices=[(f.name, f.value) for f in Filiais], validators=[DataRequired()])
    status = BooleanField('Ativo', default=True)
    submit = SubmitField('Salvar Alterações')