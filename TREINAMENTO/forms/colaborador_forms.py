from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ColaboradorForm(FlaskForm):
    # Nome do colaborador
    nome = StringField("Nome", validators=[
        DataRequired(message="O nome é obrigatório."),
        Length(max=50, message="O nome deve ter no máximo 50 caracteres.")
    ])

    # E-mail do colaborador
    email = EmailField('E-mail', validators=[
        DataRequired(message="O e-mail é obrigatório."),
        Email(message="Insira um e-mail válido."),
        Length(max=50, message="O e-mail deve ter no máximo 50 caracteres.")
    ])

    # Cargo do colaborador
    cargo = StringField('Cargo', validators=[
        DataRequired(message="O cargo é obrigatório."),
        Length(max=50, message="O cargo deve ter no máximo 50 caracteres.")
    ])

    # Campo para selecionar o a filial
    filial = SelectField('Filial', choices=[], validators=[
        DataRequired(message="Por favor, selecione uma filial.")
    ])
    
    id_empresa = SelectField('Empresa', choices=[], coerce=int, validators=[
        DataRequired(message="Por favor, selecione uma empresa.")
    ])

    # Status do tipo (ativo/inativo)
    status = BooleanField('Ativo', default=True)

    submit = SubmitField('Salvar')
