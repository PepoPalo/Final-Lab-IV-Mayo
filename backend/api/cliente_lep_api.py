from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from backend.infraestructura.clientes_lep_repo import ClientesLepRepo

repo = ClientesLepRepo()

nsclienteLEP = Namespace('clienteLEPs', description='Administrador de clienteLEPs')
modeloclienteLEPSinN = Model('clienteLEPSinNumero',{
    'mesa': fields.Integer(),
    'porcentaje_venta': fields.Float(),
    'fecha': fields.Date(),
    'nro_clienteLEP': fields.Integer(),
    'cerrada': fields.Boolean()
})

modeloclienteLEP = modeloclienteLEPSinN.clone('clienteLEP', {
    'numero': fields.Integer()
})

modeloBusqueda = Model('BusquedaFechas', {
    'desde': fields.Date(),
    'hasta': fields.Date()
})

nsclienteLEP.models[modeloclienteLEP.name] = modeloclienteLEP
nsclienteLEP.models[modeloclienteLEPSinN.name] = modeloclienteLEPSinN
nsclienteLEP.models[modeloBusqueda.name] = modeloBusqueda

nuevaclienteLEPParser = reqparse.RequestParser(bundle_errors=True)
nuevaclienteLEPParser.add_argument('mesa', type=int, required=True)
nuevaclienteLEPParser.add_argument('porcentaje_venta', type=float, required=True)
nuevaclienteLEPParser.add_argument('fecha', type=str, required=True)
nuevaclienteLEPParser.add_argument('nro_clienteLEP', type=int, required=True)
nuevaclienteLEPParser.add_argument('cerrada', type=bool, required=False)

editarclienteLEPParser = nuevaclienteLEPParser.copy()
editarclienteLEPParser.add_argument('numero', type=int, required=True)

buscarclienteLEPsParser = reqparse.RequestParser(bundle_errors=True)
buscarclienteLEPsParser.add_argument('desde', type=str, required=True)
buscarclienteLEPsParser.add_argument('hasta', type=str, required=True)


@nsclienteLEP.route('/')
class clienteLEPResource(Resource):
    @nsclienteLEP.marshal_list_with(modeloclienteLEP)
    def get(self):
        return repo.get_all()

    @nsclienteLEP.expect(modeloclienteLEPSinN)
    @nsclienteLEP.marshal_with(modeloclienteLEP)
    def post(self):
        data = nuevaclienteLEPParser.parse_args()
        f = repo.agregar(data)
        if f:
            return f, 201
        abort(500)

@nsclienteLEP.route('/<int:numero>')
class clienteLEPsResource(Resource):
    @nsclienteLEP.marshal_with(modeloclienteLEP)
    def get(self, numero):
        f = repo.get_by_numero(numero)
        if f:
            return f, 200
        abort(404)

    def delete(self, numero):
        if repo.borrar(numero):
            return 'clienteLEP borrada', 200
        abort(400)
    
    @nsclienteLEP.expect(modeloclienteLEP)
    def put(self, numero):
        data = editarclienteLEPParser.parse_args()
        if repo.modificar(numero, data):
            return 'clienteLEP modificada', 200
        abort(404)

@nsclienteLEP.route('/buscar/<string:desde>/<string:hasta>/')
class clienteLEPsResource(Resource):
    @nsclienteLEP.marshal_list_with(modeloclienteLEP)
    def get(self, desde, hasta):
        l = repo.buscar(desde, hasta)
        if l:
            return l, 200
        abort(404)

@nsclienteLEP.route('/buscar/<string:desde>/<string:hasta>/<int:clienteLEP>')
class clienteLEPsResource(Resource):
    # """
    # Busca clienteLEPs con las fechas, el formato es: YYYY-MM-DD
    # """
    @nsclienteLEP.marshal_list_with(modeloclienteLEP)
    def get(self, desde, hasta, cliente):
        l = repo.buscar_by_cliente(desde, hasta, cliente)
        if l:
            return l, 200
        abort(404)
