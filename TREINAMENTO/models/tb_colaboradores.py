from TREINAMENTO import db
from datetime import datetime
from .enum_filiais import Filiais

class Colaborador(db.Model):
    __tablename__ = 'tb_colaboradores'
    id_colaborador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100))
    id_empresa = db.Column(db.Integer, db.ForeignKey('tb_empresas.id_empresa'), nullable=False)
    id_responsavel = db.Column(db.Integer, db.ForeignKey('tb_responsaveis.id'), nullable=False)
    filial = db.Column(db.Enum(Filiais), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    logins = db.relationship('Login', backref='colaborador', lazy=True)
    inscricoes = db.relationship('Inscricao', backref='colaborador', lazy=True)

    def __repr__(self):
        return f"<Colaborador(id_colaborador={self.id_colaborador}, nome='{self.nome}', email='{self.email}', filial='{self.filial}')>"
    
    # Método para criar um colaborador a partir do formulário
    @classmethod
    def cadastro_colaborador(cls, form):
        return cls(
            nome=form.nome.data,
            email=form.email.data,
            cargo=form.cargo.data,
            id_empresa=form.id_empresa.data,
            filial=form.filial.data,
            status=form.status.data
        )
    
    # Método para atualizar o colaborador existente a partir do formulário
    def atualizar_colaborador(self, form):
        self.nome = form.nome.data
        self.email = form.email.data
        self.cargo = form.cargo.data
        self.id_empresa = form.id_empresa.data
        self.filial = form.filial.data
        self.status = form.status.data
        return self