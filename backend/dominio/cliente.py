from sqlalchemy import Column, Integer, String, Date, Boolean
from datos import db

class Cliente(db.Model):
    __tablename__: 'clientes'
    id = Column(Integer(), primary_key=True)
    # dni = Column(Integer(), primary_key=True)
    nombre = Column(String(80), nullable=False)
    direccion = Column(String(100), nullable=False)
    sexo =Column(String(1), nullable=False)
    fecha_ingreso = Column(Date(), nullable=False)
    # rel_lep  = Column(ARRAY(), nullable=False)
    activo = Column(Boolean(True), nullable=False)