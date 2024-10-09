from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class MarcaTipoForm(FlaskForm):
    # Campo para selecionar o id da marca
    id_marca = SelectField('Marca', coerce=int, validators=[
        DataRequired(message="Por favor, selecione uma marca.")
    ])

    # Campo para selecionar o id do tipo
    id_tipo = SelectField('Tipo', coerce=int, validators=[
        DataRequired(message="Por favor, selecione um tipo.")
    ])

    submit = SubmitField('Salvar')
