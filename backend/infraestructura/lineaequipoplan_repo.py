from backend.dominio.lineaequipoplan import lineaequipoplan
from backend.datos import db

class LineaEquipoPlanRepo():
    def get_all(self):
        return lineaequipoplan.query.all()

    def agregar(self, data):
        lineaequipoplan = lineaequipoplan(**data)
        db.session.add(lineaequipoplan)
        db.session.commit()
        return lineaequipoplan
    
    def get_by_id(self, id):
        return lineaequipoplan.query.get(id)

    def borrar(self, id):
        lineaequipoplan = lineaequipoplan.query.get(id)
        if lineaequipoplan:
            db.session.delete(lineaequipoplan)
            db.session.commit()
            return True
        return False

    def modificar(self,id,data):
        lineaequipoplan = lineaequipoplan.query.get(id)
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