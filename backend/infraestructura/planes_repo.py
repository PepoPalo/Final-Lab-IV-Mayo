from backend.dominio.plan import plan
from backend.datos import db

class PlanRepo():
    def get_all(self):
        return plan.query.all()

    def agregar(self, data):
        plan = plan(**data)
        db.session.add(plan)
        db.session.commit()
        return plan
    
    def get_by_id(self, id):
        return plan.query.get(id)

    def baja(self, id):
        plan = plan.query.get(id)
        if plan:
            plan.estaActivo =False
            db.session.commit()
            return True
        return False

    def modificar(self,id,data):
        plan = plan.query.get(id)
        if plan:
            plan.id = data['id']
            plan.nombre = data['nombre']
            plan.costo_por_mes = data['costo_por_mes']
            plan.cant_llamadas = data['cant_llamadas']
            plan.cant_mensajes = data['cant_mensajes']
            plan.cant_gigas = data['cant_gigas']
            plan.tipo = data['tipo']


            db.session.commit()
            return True
        return False