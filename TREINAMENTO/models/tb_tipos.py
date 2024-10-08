from TREINAMENTO import db
from datetime import datetime


class Tipo(db.Model):
    __tablename__ = 'tb_tipos'

    id_tipo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    marcas_tipos = db.relationship('MarcaTipo', back_populates='tipo', lazy=True)

    def __repr__(self):
        return f"<Tipo(id_tipo={self.id_tipo}, nome='{self.nome}', " \
               f"status={self.status}, data_criacao='{self.data_criacao}', " \
               f"data_alteracao='{self.data_alteracao}')>"


    @classmethod
    def cadastro_tipo(cls, form):
        # Verifica se o nome existe
        if cls.query.filter_by(nome=form.nome.data).first():
            raise ValueError(f"O tipo '{form.nome.data}' já existe. Por favor, escolha outro nome.")

        # Cria e retorna uma nova instância de Tipo
        return cls(
            nome=form.nome.data,
            status=form.status.data
        )

    def atualizar_tipo(self, form):
        # Verifica se o nome existe e é diferente do atual
        tipo_existente = Tipo.query.filter_by(nome=form.nome.data).first()
        if tipo_existente and tipo_existente.id_tipo != self.id_tipo:
            raise ValueError(f"O nome '{form.nome.data}' já está em uso por outro registro.")

        # Atualiza os atributos da instância com os dados do formulário
        self.nome = form.nome.data
        self.status = form.status.data
        return self
