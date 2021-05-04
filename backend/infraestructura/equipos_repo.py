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

    def baja(self,id):
        e = Equipo.query.get(id)
        if e:
            e.activo = False
            db.session.commit()
            return True
        return False

    def buscar_by_activo(self, desde, hasta):
        return Equipo.query.filter(
            Equipo.fecha_ingreso >= desde,
            Equipo.fecha_ingreso <= hasta,
            Equipo.activo ==True).all()

    def modificar(self, id, data):
        e = Equipo.query.get(id)
        if e:
            e.imei = data['imei']
            e.marca = data['marca']
            e.modelo = data.get('modelo')
            e.estado= data['estado']
            e.fecha_ingreso = data.get('fecha_ingreso')
            e.activo = data['activo']            
            db.session.commit()
            return True
        return False