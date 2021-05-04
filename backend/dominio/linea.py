from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from datos import db

class Linea(db.Model):
    __tablename__ = 'lineas'
    numero = Column(Integer(), primary_key=True, autoincrement=True)
    mesa = Column(Integer(), nullable=False)
    porcentaje_venta = Column(Float())
    
    fecha = Column(Date(), nullable=False)
    cerrada = Column(Boolean(False))
