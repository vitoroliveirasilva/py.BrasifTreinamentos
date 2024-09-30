from TREINAMENTO import db
from datetime import datetime

class Colaborador(db.Model):
    __tablename__ = 'tb_colaboradores'
    id_colaborador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100))
    id_empresa = db.Column(db.Integer, db.ForeignKey('tb_empresas.id_empresa'), nullable=False)
    id_responsavel = db.Column(db.Integer, db.ForeignKey('tb_responsaveis.id'), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    logins = db.relationship('Login', backref='colaborador', lazy=True)
    inscricoes = db.relationship('Inscricao', backref='colaborador', lazy=True)

    def __repr__(self):
        return f"<Colaborador(id_colaborador={self.id_colaborador}, nome='{self.nome}', email='{self.email}')>"
    