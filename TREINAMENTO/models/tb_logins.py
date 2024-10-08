from TREINAMENTO import db
from datetime import datetime
from sqlalchemy import UniqueConstraint


class Login(db.Model):
    __tablename__ = 'tb_logins'

    id_login = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_colaborador = db.Column(db.Integer, db.ForeignKey('tb_colaboradores.id_colaborador'), nullable=False)
    id_marca_tipo = db.Column(db.Integer, db.ForeignKey('tb_marca_tipo.id_marca_tipo'), nullable=False)
    usuario = db.Column(db.String(100), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    colaborador = db.relationship('Colaborador', back_populates='logins')
    marca_tipo = db.relationship('MarcaTipo', backref=db.backref('logins', lazy=True))

    UniqueConstraint('id_marca_tipo', 'usuario', name='unique_usuario_marca_tipo')

    def __repr__(self):
        return f"<Login(id_login={self.id_login}, id_colaborador={self.id_colaborador}, " \
               f"id_marca_tipo={self.id_marca_tipo}, usuario='{self.usuario}', " \
               f"status={self.status}, data_criacao='{self.data_criacao}', " \
               f"data_alteracao='{self.data_alteracao}')>"


    @classmethod
    # Método para criar um login a partir do formulário
    def cadastro_login(cls, form):
        return cls(
            usuario=form.usuario.data,
            id_colaborador=form.id_colaborador.data,
            id_marca=form.id_marca.data,
            id_tipo=form.id_tipo.data,
            status=form.status.data
        )

    # Método para atualizar o login existente a partir do formulário
    def atualizar_login(self, form):
        self.usuario = form.usuario.data
        self.id_colaborador = form.id_colaborador.data
        self.id_marca = form.id_marca.data
        self.id_tipo = form.id_tipo.data
        self.status = form.status.data
        return self
