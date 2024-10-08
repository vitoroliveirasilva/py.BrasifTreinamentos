from TREINAMENTO import db
from sqlalchemy import UniqueConstraint


class MarcaTipo(db.Model):
    __tablename__ = 'tb_marca_tipo'

    id_marca_tipo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_marca = db.Column(db.Integer, db.ForeignKey('tb_marcas.id_marca'), nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tb_tipos.id_tipo'), nullable=False)

    marca = db.relationship('Marca', back_populates='marcas_tipos')
    tipo = db.relationship('Tipo', back_populates='marcas_tipos')

    UniqueConstraint('id_marca', 'id_tipo', name='unique_marca_tipo')

    def __repr__(self):
        return f"<MarcaTipo(id_marca_tipo={self.id_marca_tipo}, id_marca={self.id_marca}, " \
               f"id_tipo={self.id_tipo})>"

