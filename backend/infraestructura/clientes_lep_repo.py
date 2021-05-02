import datetime
from backend.dominio.cliente_lep import ClienteLEP
from backend.datos import db

class ClientesLepRepo():
    def get_all(self):
        return ClienteLEP.query.all()

    def agregar(self, data):
        a = ClienteLEP(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_numero(self, numero):
        return ClienteLEP.query.get(numero)

    def borrar(self, numero):
        a = ClienteLEP.query.get(numero)
        if a:
            db.session.delete(a)
            db.session.commit()
            return True
        return False

    def modificar(self,numero,data):
        a = ClienteLEP.query.get(numero)
        if a:
            a.id = data['id']
            a.cliente_id = data['lep_id']
            a.lep_id = data['lep_id']            
            db.session.commit()
            return True
        return False

    def buscar(self, desde, hasta):
        return ClienteLEP.query.filter(
            ClienteLEP.fecha >= desde,
            ClienteLEP.fecha <= hasta).all()

    def buscar_by_cliente(self, desde, hasta, cliente):
        return ClienteLEP.query.filter(
            ClienteLEP.fecha >= desde,
            ClienteLEP.fecha <= hasta,
            ClienteLEP.id_cliente == cliente).all()