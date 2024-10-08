from TREINAMENTO import db
from datetime import datetime
from .enum_filiais import Filiais


class Colaborador(db.Model):
    __tablename__ = 'tb_colaboradores'

    id_colaborador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100))
    id_empresa = db.Column(db.Integer, db.ForeignKey('tb_empresas.id_empresa'), nullable=False)
    id_responsavel = db.Column(db.Integer, db.ForeignKey('tb_responsaveis.id'), nullable=False)
    filial = db.Column(db.Enum(Filiais), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    empresa = db.relationship('Empresa', back_populates='colaboradores')
    responsavel = db.relationship('Responsavel', back_populates='colaboradores')
    logins = db.relationship('Login', back_populates='colaborador', lazy=True)
    inscricoes = db.relationship('Inscricao', back_populates='colaborador', lazy=True)

    def __repr__(self):
        return f"<Colaborador(id_colaborador={self.id_colaborador}, nome='{self.nome}', " \
               f"email='{self.email}', cargo='{self.cargo}', " \
               f"id_empresa={self.id_empresa}, id_responsavel={self.id_responsavel}, " \
               f"filial='{self.filial}', status={self.status}, " \
               f"data_criacao='{self.data_criacao}', data_alteracao='{self.data_alteracao}')>"


    @classmethod
    def cadastro_colaborador(cls, form, id_responsavel):
                
        if not id_responsavel:
            raise ValueError("Não foi possível obter o ID do responsável logado no sistema.")
        
        # Verifica se o email do colaborador já está cadastrado
        colaborador_existente = cls.query.filter_by(email=form.email.data).first()

        if colaborador_existente:
            raise ValueError(f"O email '{form.email.data}' já está cadastrado para outro colaborador.")

        # Cria e retorna uma nova instância de Colaborador
        return cls(
            nome=form.nome.data,
            email=form.email.data,
            cargo=form.cargo.data,
            id_empresa=form.id_empresa.data,
            id_responsavel=id_responsavel,
            filial=form.filial.data,
            status=form.status.data
        )

    def atualizar_colaborador(self, form):
        
        # Verifica se o email já está sendo utilizado por outro colaborador
        colaborador_existente = Colaborador.query.filter_by(email=form.email.data).first()

        if colaborador_existente and colaborador_existente.id_colaborador != self.id_colaborador:
            raise ValueError(f"O email '{form.email.data}' já está em uso por outro colaborador.")

        # Atualiza os atributos da instância com os dados do formulário
        self.nome = form.nome.data
        self.email = form.email.data
        self.cargo = form.cargo.data
        self.id_empresa = form.id_empresa.data
        self.id_responsavel = form.id_responsavel.data
        self.filial = form.filial.data
        self.status = form.status.data
        return self
