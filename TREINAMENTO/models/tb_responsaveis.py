from TREINAMENTO import db
from datetime import datetime

class Responsavel(db.Model):
    __tablename__ = 'tb_responsaveis'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    id_azure_ad = db.Column(db.String(100), unique=True, nullable=False)
    permissao = db.Column(db.Boolean, default=False, nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    colaboradores = db.relationship('Colaborador', backref='responsavel_colaborador', lazy=True)

    def __repr__(self):
        return f"<Responsavel(id={self.id}, nome='{self.nome}', email='{self.email}')>"


    # Métodos exigidos pelo Flask-Login
    @property
    def is_active(self):
        # Verifica se o usuário está ativo
        return self.status

    @property
    def is_authenticated(self):
        # Verifica se o usuário está autenticado
        return True

    @property
    def is_anonymous(self):
        # Verifica se o usuário é anônimo
        return False

    def get_id(self):
        # Retorna o ID do usuário
        return str(self.id)
    

    # Método para atualizar o responsável existente a partir do formulário
    def atualizar_responsavel(self, form):
        self.permissao = form.permissao.data
        self.status = form.status.data
        return self