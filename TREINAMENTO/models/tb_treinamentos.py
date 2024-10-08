from TREINAMENTO import db
from datetime import datetime

class Treinamento(db.Model):
    __tablename__ = 'tb_treinamentos'
    id_treinamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_marca = db.Column(db.Integer, db.ForeignKey('tb_marcas.id_marca'), nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tb_tipos.id_tipo'), nullable=False)
    treinamento = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    inscricoes = db.relationship('Inscricao', backref='treinamento_inscricao', lazy=True)
    tipo = db.relationship('Tipo', back_populates='treinamentos', lazy=True)
    marca = db.relationship('Marca', back_populates='treinamentos', lazy=True)

    def __repr__(self):
        return f"<Treinamento(id_treinamento={self.id_treinamento}, treinamento='{self.treinamento}', id_marca={self.id_marca}, id_tipo={self.id_tipo})>"


    @classmethod
    def cadastro_treinamento(cls, form):
        # Verifica se o nome do treinamento já existe para a mesma marca e tipo
        treinamento_existente = cls.query.filter_by(
            treinamento=form.treinamento.data,
            id_marca=form.id_marca.data,
            id_tipo=form.id_tipo.data
        ).first()

        if treinamento_existente:
            raise ValueError(f"O treinamento '{form.treinamento.data}' já existe para essa marca e tipo.")
        
        return cls(
            id_marca=form.id_marca.data,
            id_tipo=form.id_tipo.data,
            treinamento=form.treinamento.data,
            descricao=form.descricao.data,
            status=form.status.data
        )

    def atualizar_treinamento(self, form):
        # Verifica se o nome do treinamento já existe e se pertence a outro registro
        treinamento_existente = Treinamento.query.filter_by(
            treinamento=form.treinamento.data,
            id_marca=form.id_marca.data,
            id_tipo=form.id_tipo.data
        ).first()

        if treinamento_existente and treinamento_existente.id_treinamento != self.id_treinamento:
            raise ValueError(f"O treinamento '{form.treinamento.data}' já existe para essa marca e tipo.")

        self.id_marca = form.id_marca.data
        self.id_tipo = form.id_tipo.data
        self.treinamento = form.treinamento.data
        self.descricao = form.descricao.data
        self.status = form.status.data
        return self
