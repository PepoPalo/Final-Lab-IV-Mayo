from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from datos import db

class Equipo(db.Model):
    __tablename__ = 'equipos'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(10), nullable=False)
    descripcion = Column(String(120), nullable=False)
    costo = Column(Numeric())
    porcentaje_ganancia = Column(Numeric())
