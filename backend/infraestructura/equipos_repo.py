from dominio.equipo import Equipo
from datos import db


class EquiposRepo():
    def get_all(self):
        return Equipo.query.all()

    def agregar(self, data):
        e = Equipo(**data)
        db.session.add(e)
        db.session.commit()
        return e
    
    def get_by_id(self, id):
        return Equipo.query.get(id)

    def borrar(self,id):
        e = Equipo.query.get(id)
        if e:
            db.session.delete(e)
            db.session.commit()
            return True
        return False

    def modificar(self, id, data):
        e = Equipo.query.get(id)
        if e:
            e.codigo = data['codigo']
            e.tipo = data['tipo']
            e.descripcion = data.get('descripcion', None)
            e.costo = data['costo']
            e.porcentaje_ganancia = data['porcentaje_ganancia']
            db.session.commit()
            return True
        return False