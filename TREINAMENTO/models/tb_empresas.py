from TREINAMENTO import db
from datetime import datetime
from .enum_filiais import Filiais
from sqlalchemy import UniqueConstraint


class Empresa(db.Model):
    __tablename__ = 'tb_empresas'

    id_empresa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_empresa = db.Column(db.String(100), nullable=False)
    filial = db.Column(db.Enum(Filiais), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    colaboradores = db.relationship('Colaborador', back_populates='empresa', lazy=True)

    UniqueConstraint('nome_empresa', 'filial', name='unique_empresa_filial')

    def __repr__(self):
        return f"<Empresa(id_empresa={self.id_empresa}, nome_empresa='{self.nome_empresa}', " \
               f"filial='{self.filial}', status={self.status}, " \
               f"data_criacao='{self.data_criacao}', data_alteracao='{self.data_alteracao}')>"


    @classmethod
    # Método para criar uma empresa a partir do formulário
    def cadastro_empresa(cls, form):
        # Verifica se o nome da empresa já existe
        empresa_existente = cls.query.filter_by(nome_empresa=form.nome_empresa.data).first()

        if empresa_existente:
            raise ValueError(f"A empresa '{form.nome_empresa.data}' já existe. Por favor, escolha outro nome.")
        
        return cls(
            nome_empresa=form.nome_empresa.data,
            filial=form.filial.data,
            status=form.status.data
        )
    
    # Método para atualizar a empresa existente a partir do formulário
    def atualizar_empresa(self, form):
        # Verifica se o nome da empresa já existe e se pertence a outro registro
        empresa_existente = Empresa.query.filter_by(nome_empresa=form.nome_empresa.data).first()

        if empresa_existente and empresa_existente.id_empresa != self.id_empresa:
            raise ValueError(f"O nome da empresa '{form.nome_empresa.data}' já está em uso por outro registro.")

        self.nome_empresa = form.nome_empresa.data
        self.filial = form.filial.data
        self.status = form.status.data
        return self
