from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class EmpresaForm(FlaskForm):
    # Nome da empresa
    nome_empresa = StringField("Nome da empresa", validators=[
        DataRequired(message="O nome da empresa é obrigatório."),
        Length(max=50, message="O nome da empresa deve ter no máximo 50 caracteres.")
    ])

    # Campo para selecionar o a filial
    filial = SelectField('Filial', choices=[], validators=[
        DataRequired(message="Por favor, selecione uma filial.")
    ])

    # Status do tipo (ativo/inativo)
    status = BooleanField('Ativo', default=True)

    submit = SubmitField('Salvar')
