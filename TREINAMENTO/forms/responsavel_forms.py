from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField

class ResponsavelForm(FlaskForm):
    permissao = BooleanField('Permissão', default=False)
    status = BooleanField('Ativo', default=True)
    submit = SubmitField('Salvar')