from TREINAMENTO import db
from datetime import datetime

class Login(db.Model):
    __tablename__ = 'tb_logins'
    id_login = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_colaborador = db.Column(db.Integer, db.ForeignKey('tb_colaboradores.id_colaborador'), nullable=False)
    id_marca = db.Column(db.Integer, db.ForeignKey('tb_marcas.id_marca'), nullable=False)
    usuario = db.Column(db.String(100), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Login(id_login={self.id_login}, usuario='{self.usuario}', id_colaborador={self.id_colaborador}, id_marca={self.id_marca})>"
    
    # Método para criar um login a partir do formulário
    @classmethod
    def cadastro_login(cls, form):
        return cls(
            usuario=form.usuario.data,
            id_colaborador=form.id_colaborador.data,
            id_marca=form.id_marca.data,
            status=form.status.data
        )