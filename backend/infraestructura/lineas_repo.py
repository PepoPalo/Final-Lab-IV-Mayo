import datetime
from backend.dominio.linea import Linea
from backend.datos import db

class AdicionesRepo():
    def get_all(self):
        return Linea.query.all()

    def agregar(self, data):
        a = Linea(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_numero(self, numero):
        return Linea.query.get(numero)

    def borrar(self, numero):
        a = Linea.query.get(numero)
        if a:
            db.session.delete(a)
            db.session.commit()
            return True
        return False

    def modificar(self,numero,data):
        a = Linea.query.get(numero)
        if a:
            a.numero = data['numero']
            a.mesa = data['mesa']
            a.porcentaje_venta = data['porcentaje_venta']
            a.nro_mozo = data['nro_mozo']
            a.fecha = data['fecha']
            a.cerrada = data['cerrada']
            db.session.commit()
            return True
        return False

    def buscar(self, desde, hasta):
        return Linea.query.filter(
            Linea.fecha >= desde,
            Linea.fecha <= hasta).all()

    def buscar_by_mozo(self, desde, hasta, mozo):
        return Linea.query.filter(
            Linea.fecha >= desde,
            Linea.fecha <= hasta,
            Linea.nro_mozo == mozo).all()
