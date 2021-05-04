from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from datos import db

class Linea(db.Model):
    __tablename__ = 'lineas'    
    id= Column(Integer(), primary_key=True, autoincrement=True)
    numero = Column(Integer(), nullable=False)
    estado = Column(Integer(), nullable=False)
    activa =  Column(Boolean(True), nullable=False)
