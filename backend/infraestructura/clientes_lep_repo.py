import datetime
from dominio.cliente_lep import ClienteLep
from datos import db

class ClientesLepRepo():
    def get_all(self):
        return ClienteLep.query.all()

    def agregar(self, data):
        a = ClienteLep(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_numero(self, numero):
        return ClienteLep.query.get(numero)

    def borrar(self, numero):
        a = ClienteLep.query.get(numero)
        if a:
            db.session.delete(a)
            db.session.commit()
            return True
        return False

    def modificar(self,numero,data):
        a = ClienteLep.query.get(numero)
        if a:
            a.id = data['id']
            a.cliente_id = data['lep_id']
            a.lep_id = data['lep_id']            
            db.session.commit()
            return True
        return False

    def buscar(self, desde, hasta):
        return ClienteLep.query.filter(
            ClienteLep.fecha >= desde,
            ClienteLep.fecha <= hasta).all()

    def buscar_by_cliente(self, desde, hasta, cliente):
        return ClienteLep.query.filter(
            ClienteLep.fecha >= desde,
            ClienteLep.fecha <= hasta,
            ClienteLep.id_cliente == cliente).all()