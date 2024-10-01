from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class InscricaoForm(FlaskForm):
    id_colaborador = SelectField('Colaborador', coerce=int, validators=[DataRequired()])
    id_treinamento = SelectField('Treinamento', coerce=int, validators=[DataRequired()])
    data_inscricao = DateField('Data de Inscrição', format='%Y-%m-%d', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Pendente', 'Pendente'), ('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')], validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
