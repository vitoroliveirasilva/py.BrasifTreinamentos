from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class TreinamentoForm(FlaskForm):
    # Campo para selecionar a combinação de Marca e Tipo
    id_marca_tipo = SelectField("Marca e Tipo", coerce=int, validators=[
        DataRequired(message="Por favor, selecione uma marca e tipo.")
    ])

    # Nome do treinamento
    treinamento = StringField("Nome do Treinamento", validators=[
        DataRequired(message="O nome do treinamento é obrigatório."),
        Length(max=50, message="O nome do treinamento deve ter no máximo 50 caracteres.")
    ])

    # Descrição do treinamento
    descricao = TextAreaField("Descrição", validators=[
        Length(max=500, message="A descrição pode ter no máximo 500 caracteres.")
    ])

    # Status do treinamento (ativo/inativo)
    status = BooleanField("Ativo", default=True)

    submit = SubmitField("Salvar")
