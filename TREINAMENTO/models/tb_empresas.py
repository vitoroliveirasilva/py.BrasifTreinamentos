from TREINAMENTO import db
from datetime import datetime
from .enum_filiais import Filiais

class Empresa(db.Model):
    __tablename__ = 'tb_empresas'
    id_empresa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_empresa = db.Column(db.String(100), nullable=False)
    filial = db.Column(db.Enum(Filiais), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    colaboradores = db.relationship('Colaborador', backref='empresa', lazy=True)

    def __repr__(self):
        return f"<Empresa(id_empresa={self.id_empresa}, nome_empresa='{self.nome_empresa}', filial='{self.filial}')>"
    
    # Método para criar uma empresa a partir do formulário
    @classmethod
    def cadastro_empresa(cls, form):
        return cls(
            nome_empresa=form.nome_empresa.data,
            filial=form.filial.data,
            status=form.status.data
        )