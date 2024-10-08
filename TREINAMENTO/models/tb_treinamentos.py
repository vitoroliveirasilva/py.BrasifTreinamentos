from TREINAMENTO import db
from datetime import datetime
from sqlalchemy import UniqueConstraint


class Treinamento(db.Model):
    __tablename__ = 'tb_treinamentos'

    id_treinamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_marca_tipo = db.Column(db.Integer, db.ForeignKey('tb_marca_tipo.id_marca_tipo'), nullable=False)
    treinamento = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    marca_tipo = db.relationship('MarcaTipo', back_populates='treinamentos', lazy='joined')

    UniqueConstraint('id_marca_tipo', 'treinamento', name='unique_treinamento_marca_tipo')

    def __repr__(self):
        return f"<Treinamento(id_treinamento={self.id_treinamento}, " \
               f"id_marca_tipo={self.id_marca_tipo}, treinamento='{self.treinamento}', " \
               f"status={self.status}, data_criacao='{self.data_criacao}', " \
               f"data_alteracao='{self.data_alteracao}')>"


    @classmethod
    def cadastro_treinamento(cls, form):
        # Verifica se o nome do treinamento já existe para a mesma marca e tipo
        treinamento_existente = cls.query.filter_by(
            id_marca_tipo=form.id_marca_tipo.data,
            treinamento=form.treinamento.data
        ).first()

        if treinamento_existente:
            raise ValueError(f"O treinamento '{form.treinamento.data}' já existe para essa marca e tipo.")
        
        # Cria e retorna uma nova instância de Treinamento
        return cls(
            id_marca_tipo=form.id_marca_tipo.data,
            treinamento=form.treinamento.data,
            descricao=form.descricao.data,
            status=form.status.data
        )

    def atualizar_treinamento(self, form):
        # Verifica se o nome do treinamento já existe e se pertence a outro registro
        treinamento_existente = Treinamento.query.filter_by(
            id_marca_tipo=form.id_marca_tipo.data,
            treinamento=form.treinamento.data
        ).first()

        if treinamento_existente and treinamento_existente.id_treinamento != self.id_treinamento:
            raise ValueError(f"O treinamento '{form.treinamento.data}' já existe para essa marca e tipo.")

        # Atualiza os atributos da instância com os dados do formulário
        self.id_marca_tipo = form.id_marca_tipo.data
        self.treinamento = form.treinamento.data
        self.descricao = form.descricao.data
        self.status = form.status.data

        return self
