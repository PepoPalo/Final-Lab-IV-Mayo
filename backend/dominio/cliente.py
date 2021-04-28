from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.datos import db

class Cliente(db.Model):
    __tablename__: 'clientes'
    numero = Column(Integer(), primary_key=True, autoincrement=True)
    nombre = Column(String(80), nullable=False)
    adiciones = db.relationship('Adicion')
