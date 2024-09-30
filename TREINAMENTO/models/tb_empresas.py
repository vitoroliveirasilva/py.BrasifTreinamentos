from TREINAMENTO import db
from datetime import datetime

class Empresa(db.Model):
    __tablename__ = 'tb_empresas'
    id_empresa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_empresa = db.Column(db.String(100), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    colaboradores = db.relationship('Colaborador', backref='empresa', lazy=True)

    def __repr__(self):
        return f"<Empresa(id_empresa={self.id_empresa}, nome_empresa='{self.nome_empresa}')>"
