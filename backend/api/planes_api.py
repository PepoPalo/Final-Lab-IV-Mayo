from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from backend.infraestructura.planes_repo import planesRepo

repo = planesRepo()

nsPlan = Namespace('planes', description='Administrador de planes')

modeloPlanSinID = Model('PlanSinCod',{
    'tipo': fields.String(),
    'descripcion': fields.String(),
    'porcentaje_ganancia': fields.Integer(),
    'costo': fields.Float()
})

modeloPlan = modeloPlanSinID.clone('Plan',{
    'codigo': fields.Integer(),

})

nsPlan.models[modeloPlan.name] = modeloPlan
nsPlan.models[modeloPlanSinID.name] = modeloPlanSinID

nuevoPlanParser = reqparse.RequestParser(bundle_errors=True)
nuevoPlanParser.add_argument('tipo', type=str, required=True)
nuevoPlanParser.add_argument('descripcion', type=str)
nuevoPlanParser.add_argument('costo', type=float)
nuevoPlanParser.add_argument('porcentaje_ganancia', type=int, required=True)

editarPlanParser = nuevoPlanParser.copy()
editarPlanParser.add_argument('codigo',type=int, required=True)

@nsPlan.route('/')
class PlanResource(Resource):
    @nsPlan.marshal_list_with(modeloPlan)
    def get(self):
        return repo.get_all()

    @nsPlan.expect(modeloPlanSinID)
    @nsPlan.marshal_with(modeloPlan)
    def post(self):
        data = nuevoPlanParser.parse_args()
        p = repo.agregar(data)
        if p:
            return p, 200
        abort(500)

@nsPlan.route('/<int:id>')
class PlanResource(Resource):
    @nsPlan.marshal_with(modeloPlan)
    def get(self, id):
        p = repo.get_by_id(id)
        if p:
            return p, 200
        abort(404)
    
    def delete(self, id):
        if repo.borrar(id):
            return 'Plan Eliminado', 200
        abort(400)
    
    @nsPlan.expect(modeloPlan)
    def put(self, id):
        data = editarPlanParser.parse_args()
        if repo.modificar(id,data):
            return 'Plan actualizado', 200
        abort(404)