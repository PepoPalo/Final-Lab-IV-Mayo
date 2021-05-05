from dominio.lineaequipoplan import Lineaequipoplan
from datos import db
from datetime import date


class LineaEquipoPlanRepo():
    def get_all(self):
        return Lineaequipoplan.query.all()

    def agregar(self, data):
        lineaequipoplan = lineaequipoplan(**data)
        db.session.add(lineaequipoplan)
        db.session.commit()
        return lineaequipoplan
    
    def get_by_id(self, id):
        return Lineaequipoplan.query.get(id)

    def baja(self, id):
        lineaequipoplan = Lineaequipoplan.query.get(id)
        if lineaequipoplan:
            lineaequipoplan.fecha_fin = date.now()
            db.session.commit()
            return True
        return False

    def modificar(self,id,data):
        lineaequipoplan = Lineaequipoplan.query.get(id)
        if lineaequipoplan:
            lineaequipoplan.id = data['id']
            lineaequipoplan.plan_id = data['plan_id']
            lineaequipoplan.equipo_id = data['equipo_id']
            lineaequipoplan.fecha_ini = data['fecha_ini']
            lineaequipoplan.fecha_fin = data['fecha_fin']
            lineaequipoplan.plan_costo = data['plan_costo']

            db.session.commit()
            return True
        return False