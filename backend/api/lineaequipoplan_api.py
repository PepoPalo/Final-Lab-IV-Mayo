from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from backend.infraestructura.lineaequipoplan_repo import LineaEquipoPlanRepo

repo = LineaEquipoPlanRepo()

nsLEP = Namespace('lineaequipoplan', description= 'Administrador de linea-equipo-plan')
modeloLEPSinNum = Model('DetalleSinNumero',{
    'adicion_numero': fields.Integer(),
    'producto_codigo': fields.Integer(),
    'cantidad': fields.Integer()
})

modeloLEP = modeloLEPSinNum.clone('Lineaequipoplan', {
    'id': fields.Integer()
})

nsLEP.models[modeloLEPSinNum.name] = modeloLEPSinNum
nsLEP.models[modeloLEP.name] = modeloLEP

nuevoLEPParser = reqparse.RequestParser(bundle_errors=True)
nuevoLEPParser.add_argument('adicion_numero', type=int, required=True)
nuevoLEPParser.add_argument('producto_codigo', type=int, required=True)
nuevoLEPParser.add_argument('cantidad', type=int, required=True)

editarLEPParser = nuevoLEPParser.copy()
editarLEPParser.add_argument('id', type=int, required=True)

@nsLEP.route('/')
class DetalleResource(Resource):
    @nsLEP.marshal_list_with(modeloLEP)
    def get(self):
        return repo.get_all()

    @nsLEP.expect(modeloLEPSinNum)
    @nsLEP.marshal_with(modeloLEP)
    def post(self):
        data = nuevoLEPParser.parse_args()
        df = repo.agregar(data)
        if df:
            return df, 201
        abort(500)

@nsLEP.route('/<int:id>')
class DetalleResource(Resource):
    @nsLEP.marshal_with(modeloLEP)
    def get(self, id):
        df = repo.get_by_id(id)
        if df:
            return df, 200
        abort(400)

    def delete(self, id):
        if repo.borrar(id):
            return 'Relacion linea-equipo-plan eliminada', 200
        abort(400)

    @nsLEP.expect(modeloLEP)
    def put(self, id):
        data = editarLEPParser.parse_args()
        if repo.modificar(id,data):
            return 'Relacion linea-equipo-plan modificada', 200
        abort(404)