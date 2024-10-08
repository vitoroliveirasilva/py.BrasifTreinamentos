from TREINAMENTO import db
from datetime import datetime


class Marca(db.Model):
    __tablename__ = 'tb_marcas'

    id_marca = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    marcas_tipos = db.relationship('MarcaTipo', back_populates='marca', lazy=True)
    treinamentos = db.relationship('Treinamento', back_populates='marca', lazy=True)

    def __repr__(self):
        return f"<Marca(id_marca={self.id_marca}, nome='{self.nome}', " \
               f"status={self.status}, data_criacao='{self.data_criacao}', " \
               f"data_alteracao='{self.data_alteracao}')>"


    @classmethod
    def cadastro_marca(cls, form):
        # Verifica se o nome da marca já existe
        if cls.query.filter_by(nome=form.nome.data).first():
            raise ValueError(f"A marca '{form.nome.data}' já existe. Por favor, escolha outro nome.")
        
        # Cria e retorna uma nova instância de Marca
        return cls(
            nome=form.nome.data,
            id_tipo=form.id_tipo.data,
            status=form.status.data
        )
    
    def atualizar_marca(self, form):
        # Verifica se o nome já existe e é diferente do atual
        marca_existente = Marca.query.filter_by(nome=form.nome.data).first()

        if marca_existente and marca_existente.id_marca != self.id_marca:
            raise ValueError(f"O nome da marca '{form.nome.data}' já está em uso por outro registro.")

        # Atualiza os atributos da instância com os dados do formulário
        self.nome = form.nome.data
        self.id_tipo = form.id_tipo.data
        self.status = form.status.data

        return self
