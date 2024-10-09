from TREINAMENTO import db
from datetime import datetime
from sqlalchemy import UniqueConstraint


class MarcaTipo(db.Model):
    __tablename__ = 'tb_marca_tipo'

    id_marca_tipo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_marca = db.Column(db.Integer, db.ForeignKey('tb_marcas.id_marca'), nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tb_tipos.id_tipo'), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    logins = db.relationship('Login', back_populates='marca_tipo')
    marca = db.relationship('Marca', back_populates='marca_tipo')
    tipo = db.relationship('Tipo', back_populates='marca_tipo')
    treinamentos = db.relationship('Treinamento', back_populates='marca_tipo')

    UniqueConstraint('id_marca', 'id_tipo', name='unique_marca_tipo')

    def __repr__(self):
        return f"<MarcaTipo(id_marca_tipo={self.id_marca_tipo}, id_marca={self.id_marca}, " \
               f"id_tipo={self.id_tipo})>"


    @classmethod
    def cadastro_marca_tipo(cls, form):
        # Verifica se a combinação de id_marca e id_tipo já existe
        if cls.query.filter_by(id_marca=form.id_marca.data, id_tipo=form.id_tipo.data).first():
            raise ValueError(f"A combinação de marca e tipo já existe. Por favor, escolha outra.")

        # Cria e retorna uma nova instância de MarcaTipo
        return cls(
            id_marca=form.id_marca.data,
            id_tipo=form.id_tipo.data
        )

    def atualizar_marca_tipo(self, form):
        # Verifica se a nova combinação de id_marca e id_tipo já existe e é diferente da atual
        marca_tipo_existente = MarcaTipo.query.filter_by(id_marca=form.id_marca.data, id_tipo=form.id_tipo.data).first()

        if marca_tipo_existente and marca_tipo_existente.id_marca_tipo != self.id_marca_tipo:
            raise ValueError(f"A combinação de marca e tipo já está em uso por outro registro.")

        # Atualiza os atributos da instância com os dados do formulário
        self.id_marca = form.id_marca.data
        self.id_tipo = form.id_tipo.data

        return self
