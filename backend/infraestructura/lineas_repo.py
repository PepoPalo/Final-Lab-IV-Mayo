import datetime
from dominio.linea import Linea
from datos import db

class LineasRepo():
    def get_all(self):
        return Linea.query.all()

    def agregar(self, data):
        a = Linea(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_numero(self, numero):
        return Linea.query.get(numero)

    def baja(self, numero):
        a = Linea.query.get(numero)
        if a:
            a.activa = False
            db.session.commit()
            return True
        return False

    def modificar(self,numero,data):
        a = Linea.query.get(numero)
        if a:
            a.id = data['id']
            a.numero = data['numero']
            a.estado = data['estado']
            a.activa = data['activa']
            db.session.commit()
            return True
        return False

    def buscar(self):
        return Linea.query.filter(
            Linea.activa ==True
           ).all()

   
