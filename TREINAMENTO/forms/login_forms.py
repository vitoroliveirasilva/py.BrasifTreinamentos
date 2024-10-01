from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(), Length(max=100)])
    id_colaborador = SelectField('Colaborador', coerce=int, validators=[DataRequired()])
    id_marca = SelectField('Marca', coerce=int, validators=[DataRequired()])
    status = BooleanField('Ativo', default=True)
    submit = SubmitField('Salvar')
