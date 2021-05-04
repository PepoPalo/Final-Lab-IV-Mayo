import datetime
from dominio.plan import Plan
from datos import db

class PlanesRepo():
    def get_all(self):
        return Plan.query.all()

    def agregar(self, data):
        a = Plan(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_id(self, id):
        return Plan.query.get(id)

    def borrar(self, id):
        a = Plan.query.get(id)
        if a:
            db.session.delete(a)
            db.session.commit()
            return True
        return False

    def modificar(self,id,data):
        a = Plan.query.get(id)
        if a:
            a.id = data['id']
            a.nombre = data['nombre']
            a.costo_por_mes = data['costo_por_mes']
            a.cant_llamadas = data['cant_llamadas']
            a.cant_mensajes = data['cant_mensajes']
            a.cant_gigas = data['cant_gigas']
            a.tipo = data['tipo']
            a.estaActivo = data['estaActivo']
            db.session.commit()
            return True
        return False
