from TREINAMENTO import db
from datetime import datetime

class Treinamento(db.Model):
    __tablename__ = 'tb_treinamentos'
    id_treinamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_marca = db.Column(db.Integer, db.ForeignKey('tb_marcas.id_marca'), nullable=False)
    treinamento = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    inscricoes = db.relationship('Inscricao', backref='treinamento', lazy=True)

    def __repr__(self):
        return f"<Treinamento(id_treinamento={self.id_treinamento}, treinamento='{self.treinamento}', id_marca={self.id_marca})>"
    
    # Método para cadastrar um treinamento a partir do formulário
    @classmethod
    def cadastro_treinamento(cls, form):
        return cls(
            id_marca=form.id_marca.data,
            treinamento=form.treinamento.data,
            descricao=form.descricao.data,
            status=form.status.data
        )

    # Método para atualizar o treinamento existente a partir do formulário
    def atualizar_treinamento(self, form):
        self.id_marca = form.id_marca.data
        self.treinamento = form.treinamento.data
        self.descricao = form.descricao.data
        self.status = form.status.data
        return self