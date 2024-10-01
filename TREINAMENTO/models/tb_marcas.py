from TREINAMENTO import db
from datetime import datetime

class Marca(db.Model):
    __tablename__ = 'tb_marcas'
    id_marca = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tb_tipos.id_tipo'), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    treinamentos = db.relationship('Treinamento', backref='marca', lazy=True)
    logins = db.relationship('Login', backref='marca', lazy=True)

    def __repr__(self):
        return f"<Marca(id_marca={self.id_marca}, nome='{self.nome}', id_tipo={self.id_tipo}, status={self.status})>"
    
    # Método para criar uma marca a partir do formulário
    @classmethod
    def cadastro_marca(cls, form):
        return cls(
            nome=form.nome.data,
            id_tipo=form.id_tipo.data,
            status=form.status.data
        )