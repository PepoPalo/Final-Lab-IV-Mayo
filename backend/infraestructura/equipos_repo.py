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
            e.imei = data['imei']
            e.marca = data['marca']
            e.modelo = data.get('modelo')
            # e.activo = data['costo']
            e.estado= data['activo']
            db.session.commit()
            return True
        return False