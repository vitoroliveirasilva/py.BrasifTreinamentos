from TREINAMENTO import db
from datetime import datetime

class Inscricao(db.Model):
    __tablename__ = 'tb_inscricoes'
    id_inscricao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_colaborador = db.Column(db.Integer, db.ForeignKey('tb_colaboradores.id_colaborador'), nullable=False)
    id_treinamento = db.Column(db.Integer, db.ForeignKey('tb_treinamentos.id_treinamento'), nullable=False)
    data_inscricao = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    data_alteracao = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Inscricao(id_inscricao={self.id_inscricao}, status='{self.status}', id_colaborador={self.id_colaborador}, id_treinamento={self.id_treinamento})>"
