from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from TREINAMENTO.models.enum_filiais import Filiais

class ColaboradorForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    email = EmailField('E-mail', validators=[DataRequired(), Email(), Length(max=100)])
    cargo = StringField('Cargo', validators=[Length(max=100)])
    filial = SelectField('Filial', choices=[(f.name, f.value) for f in Filiais], validators=[DataRequired()])
    status = BooleanField('Ativo', default=True)
    submit = SubmitField('Cadastrar')
    id_empresa = SelectField('Empresa', coerce=int, validators=[DataRequired()])
