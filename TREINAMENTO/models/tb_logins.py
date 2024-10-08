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
    def cadastro_login(cls, form):
        
        # Verifica se o login já existe para a combinação de usuário e marca_tipo
        login_existente = cls.query.filter_by(usuario=form.usuario.data, id_marca_tipo=form.id_marca_tipo.data).first()

        if login_existente:
            raise ValueError(f"O usuário '{form.usuario.data}' já está cadastrado para a marca/tipo correspondente.")
        
        return cls(
            usuario=form.usuario.data,
            id_colaborador=form.id_colaborador.data,
            id_marca_tipo=form.id_marca_tipo.data,
            status=form.status.data
        )

    def atualizar_login(self, form):
        
        # Verifica se o login já existe para a combinação de usuário e marca_tipo, exceto para o login atual
        login_existente = Login.query.filter_by(usuario=form.usuario.data, id_marca_tipo=form.id_marca_tipo.data).first()

        if login_existente and login_existente.id_login != self.id_login:
            raise ValueError(f"O usuário '{form.usuario.data}' já está em uso por outro login na mesma marca/tipo.")

        # Atualiza os atributos da instância com os dados do formulário
        self.usuario = form.usuario.data
        self.id_colaborador = form.id_colaborador.data
        self.id_marca_tipo = form.id_marca_tipo.data
        self.status = form.status.data
        return self
