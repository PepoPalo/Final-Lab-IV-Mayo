from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from backend.datos import db

class Linea(db.Model):
    __tablename__ = 'lineas'
    numero = Column(Integer(), primary_key=True, autoincrement=True)
    mesa = Column(Integer(), nullable=False)
    porcentaje_venta = Column(Float())
    nro_mozo = Column(Integer(), ForeignKey('mozo.numero'), nullable=False)
    fecha = Column(Date(), nullable=False)
    cerrada = Column(Boolean(False))
    detalles = relationship('Detalle')
