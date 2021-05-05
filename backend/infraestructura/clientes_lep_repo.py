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

    def baja(self, numero):
        a = ClienteLep.buscar_by_cliente(numero)
        if a:
            a.activo=False
            db.session.commit()
            return True
        return False

    def modificar(self,numero,data):
        a = ClienteLep.query.get(numero)
        if a:
            a.id = data['id']
            a.cliente_id = data['lep_id']
            a.lep_id = data['lep_id']  
            a.activo = data['activo']          
            db.session.commit()
            return True
        return False

    def buscar(self, desde, hasta):
        return ClienteLep.query.filter(
            ClienteLep.fecha >= desde,
            ClienteLep.fecha <= hasta).all()

    def buscar_by_cliente(self, cliente):
        return ClienteLep.query.filter(            
            ClienteLep.cliente_id == cliente,
            ClienteLep.activo ==True).all()
    def buscar_by_lep(self, lep):
        return ClienteLep.query.filter(            
            ClienteLep.lep_id == lep,
            ClienteLep.activo ==True).all()           