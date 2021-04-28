from backend.dominio.cliente import Cliente
from backend.datos import db

class ClientesRepo():
    def get_all(self):
        return Cliente.query.all()

    def agregar(self, data):
        cliente = Cliente(**data)
        db.session.add(cliente)
        db.session.commit()
        return cliente

    def get_by_id(self,id):
        return Cliente.query.get(id)

    def borrar(self,id):
        m = Cliente.query.get(id)
        if m:
            db.session.delete(m)
            db.session.commit()
            return True
        return False

    def modificar(self, id, data):
        m = Cliente.query.get(id)
        if m:
            m.numero = data['numero']
            m.nombre = data['nombre']
            db.session.commit()
            return True
        return False
