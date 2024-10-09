from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class MarcaTipoForm(FlaskForm):
    id_marca = SelectField('Marca', coerce=int, validators=[DataRequired()])
    id_tipo = SelectField('Tipo', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Salvar')
