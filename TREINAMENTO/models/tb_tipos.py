from TREINAMENTO import db
from datetime import datetime

class Tipo(db.Model):
    __tablename__ = 'tb_tipos'
    id_tipo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    marcas = db.relationship('Marca', backref='tipo', lazy=True)

    def __repr__(self):
        return f"<Tipo(id_tipo={self.id_tipo}, nome='{self.nome}', status={self.status})>"
    
    # Método para criar um tipo a partir do formulário
    @classmethod
    def cadastro_tipo(cls, form):
        return cls(
            nome=form.nome.data,
            status=form.status.data
        )
    
    # Método para atualizar o tipo existente a partir do formulário
    def atualizar_tipo(self, form):
        self.nome = form.nome.data
        self.status = form.status.data
        return self