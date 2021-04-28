from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from backend.infraestructura.equipos_repo import EquiposRepo

repo = EquiposRepo()

nsEquipo = Namespace('equipos', description='Administrador de equipos')

modeloEquipoSinID = Model('EquipoSinCod',{
    'tipo': fields.String(),
    'descripcion': fields.String(),
    'porcentaje_ganancia': fields.Integer(),
    'costo': fields.Float()
})

modeloEquipo = modeloEquipoSinID.clone('Equipo',{
    'codigo': fields.Integer(),

})

nsEquipo.models[modeloEquipo.name] = modeloEquipo
nsEquipo.models[modeloEquipoSinID.name] = modeloEquipoSinID

nuevoEquipoParser = reqparse.RequestParser(bundle_errors=True)
nuevoEquipoParser.add_argument('tipo', type=str, required=True)
nuevoEquipoParser.add_argument('descripcion', type=str)
nuevoEquipoParser.add_argument('costo', type=float)
nuevoEquipoParser.add_argument('porcentaje_ganancia', type=int, required=True)

editarEquipoParser = nuevoEquipoParser.copy()
editarEquipoParser.add_argument('codigo',type=int, required=True)

@nsEquipo.route('/')
class EquipoResource(Resource):
    @nsEquipo.marshal_list_with(modeloEquipo)
    def get(self):
        return repo.get_all()

    @nsEquipo.expect(modeloEquipoSinID)
    @nsEquipo.marshal_with(modeloEquipo)
    def post(self):
        data = nuevoEquipoParser.parse_args()
        p = repo.agregar(data)
        if p:
            return p, 200
        abort(500)

@nsEquipo.route('/<int:id>')
class EquipoResource(Resource):
    @nsEquipo.marshal_with(modeloEquipo)
    def get(self, id):
        p = repo.get_by_id(id)
        if p:
            return p, 200
        abort(404)
    
    def delete(self, id):
        if repo.borrar(id):
            return 'Equipo Eliminado', 200
        abort(400)
    
    @nsEquipo.expect(modeloEquipo)
    def put(self, id):
        data = editarEquipoParser.parse_args()
        if repo.modificar(id,data):
            return 'Equipo actualizado', 200
        abort(404)