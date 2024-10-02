from TREINAMENTO import db
from datetime import datetime

class Inscricao(db.Model):
    __tablename__ = 'tb_inscricoes'
    
    id_inscricao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_colaborador = db.Column(db.Integer, db.ForeignKey('tb_colaboradores.id_colaborador'), nullable=False)
    id_treinamento = db.Column(db.Integer, db.ForeignKey('tb_treinamentos.id_treinamento'), nullable=False)
    id_responsavel = db.Column(db.Integer, db.ForeignKey('tb_responsaveis.id'), nullable=False)
    data_inscricao = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('Pendente', 'Concluída', 'Cancelada', name='enum_status'), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Inscricao(id_inscricao={self.id_inscricao}, status='{self.status}', id_colaborador={self.id_colaborador}, id_treinamento={self.id_treinamento}, id_responsavel={self.id_responsavel})>"

    @staticmethod
    def cadastro_inscricao(form, id_responsavel):
        return Inscricao(
            id_colaborador=form.id_colaborador.data,
            id_treinamento=form.id_treinamento.data,
            id_responsavel=id_responsavel,
            data_inscricao=datetime.utcnow(),
            status='Pendente'
        )