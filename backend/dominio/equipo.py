from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from backend.datos import db

class Equipo(db.Model):
    __tablename__ = 'equipos'
    imei = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String(20), nullable=False)
    modelo = Column(String(120), nullable=False)
    fecha_ingreso =Column(Date(),nulable=False)
    activo = Column(Boolean(), nullable=False)
