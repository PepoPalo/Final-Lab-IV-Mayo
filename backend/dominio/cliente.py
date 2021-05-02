from sqlalchemy import Column, Integer, String, Date, Array, Boolean
from backend.datos import db

class Cliente(db.Model):
    __tablename__: 'clientes'
    numero = Column(Integer(), primary_key=True, autoincrement=True)
    id = Column(Integer(), primary_key=True)
    dni = Column(Integer(), primary_key=True)
    nombre = Column(String(80), nullable=False)
    adiciones = db.relationship('Adicion')
    direccion = Column(String(100), nullable=False)
    sexo =Column(String(1), nullable=False)
    fecha_ingreso = Column(Date(), nullable=False)
    rel_lep  = Column(Array(), nullable=False)
    activo = Column(Boolean(True), nullable=False)