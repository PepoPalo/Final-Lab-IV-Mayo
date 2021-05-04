from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from datos import db

class Lineaequipoplan(db.Model):
    __tablename__ = 'li_eq_pl'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    cantidad = Column(Integer())
