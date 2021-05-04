from dominio.lineaequipoplan import Lineaequipoplan
from dominio.equipo import Equipo
from datos import db

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
            lineaequipoplan.adicion_numero = data['adicion_numero']
            lineaequipoplan.producto_codigo = data['producto_codigo']
            lineaequipoplan.cantidad = data['cantidad']
            db.session.commit()
            return True
        return False