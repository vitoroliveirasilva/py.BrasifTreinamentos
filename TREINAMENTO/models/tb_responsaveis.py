from TREINAMENTO import db
from datetime import datetime

class Responsavel(db.Model):
    __tablename__ = 'tb_responsaveis'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    id_azure_ad = db.Column(db.String(100), unique=True, nullable=False)
    permissao = db.Column(db.Boolean, default=False, nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    colaboradores = db.relationship('Colaborador', backref='responsavel', lazy=True)

    def __repr__(self):
        return f"<Responsavel(id={self.id}, nome='{self.nome}', email='{self.email}')>"
    