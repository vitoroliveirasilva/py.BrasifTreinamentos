from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ColaboradorForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    email = EmailField('E-mail', validators=[DataRequired(), Email(), Length(max=100)])
    cargo = StringField('Cargo', validators=[DataRequired(), Length(max=100)])
    filial = SelectField('Filial', choices=[(-1, "Selecione uma filial")], validators=[DataRequired()])
    status = BooleanField('Ativo', default=True)
    id_empresa = SelectField('Empresa', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Salvar')
