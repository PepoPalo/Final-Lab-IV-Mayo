import datetime
from dominio.adicion import Adicion
from datos import db

class AdicionesRepo():
    def get_all(self):
        return Adicion.query.all()

    def agregar(self, data):
        a = Adicion(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_numero(self, numero):
        return Adicion.query.get(numero)

    def borrar(self, numero):
        a = Adicion.query.get(numero)
        if a:
            db.session.delete(a)
            db.session.commit()
            return True
        return False

    def modificar(self,numero,data):
        a = Adicion.query.get(numero)
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
        return Adicion.query.filter(
            Adicion.fecha >= desde,
            Adicion.fecha <= hasta).all()

    def buscar_by_mozo(self, desde, hasta, mozo):
        return Adicion.query.filter(
            Adicion.fecha >= desde,
            Adicion.fecha <= hasta,
            Adicion.nro_mozo == mozo).all()
