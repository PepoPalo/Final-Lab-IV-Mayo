from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from infraestructura.lineas_repo import LineasRepo

repo = LineasRepo()

nsLinea = Namespace('lineas', description='Administrador de lineas')
modeloLineaSinN = Model('LineaSinNumero',{
    'numero': fields.Integer(),
    'estado': fields.String(),
    'activa': fields.Boolean()
})

modeloLinea = modeloLineaSinN.clone('Linea', {
    'id': fields.Integer()
})

modeloBusqueda = Model('BusquedaFechas', {
    'desde': fields.Date(),
    'hasta': fields.Date()
})

nsLinea.models[modeloLinea.name] = modeloLinea
nsLinea.models[modeloLineaSinN.name] = modeloLineaSinN
nsLinea.models[modeloBusqueda.name] = modeloBusqueda

nuevaLineaParser = reqparse.RequestParser(bundle_errors=True)
nuevaLineaParser.add_argument('numero', type=int, required=True)
nuevaLineaParser.add_argument('estado', type=str, required=True)
nuevaLineaParser.add_argument('activa', type=bool, required=True)

editarLineaParser = nuevaLineaParser.copy()
editarLineaParser.add_argument('id', type=int, required=True)

buscarLineasParser = reqparse.RequestParser(bundle_errors=True)
buscarLineasParser.add_argument('desde', type=str, required=True)
buscarLineasParser.add_argument('hasta', type=str, required=True)


@nsLinea.route('/')
class LineasResource(Resource):
    @nsLinea.marshal_list_with(modeloLinea)
    def get(self):
        return repo.get_all()

    @nsLinea.expect(modeloLineaSinN)
    @nsLinea.marshal_with(modeloLinea)
    def post(self):
        data = nuevaLineaParser.parse_args()
        f = repo.agregar(data)
        if f:
            return f, 201
        abort(500)

@nsLinea.route('/<int:numero>')
class LineasResource(Resource):
    @nsLinea.marshal_with(modeloLinea)
    def get(self, numero):
        f = repo.get_by_numero(numero)
        if f:
            return f, 200
        abort(404)

    def delete(self, numero):
        if repo.borrar(numero):
            return 'Linea borrada', 200
        abort(400)
    
    @nsLinea.expect(modeloLinea)
    def put(self, numero):
        data = editarLineaParser.parse_args()
        if repo.modificar(numero, data):
            return 'Linea modificada', 200
        abort(404)

