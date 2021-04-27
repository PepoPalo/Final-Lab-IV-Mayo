from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from infraestructura.clientes_repo import clientes_repo

repo = clientes_repo()

nsCliente = Namespace('clientes', description='Administrador de cliente')

modeloClienteSinID = Model('ClienteSinID',{
    'nombre': fields.String()
})

modeloCliente = modeloClienteSinID.clone('Cliente',{
    'numero': fields.Integer()
})


nsCliente.models[modeloCliente.name] = modeloCliente
nsCliente.models[modeloClienteSinID.name] = modeloClienteSinID

nuevoClienteParser = reqparse.RequestParser(bundle_errors=True)
nuevoClienteParser.add_argument('nombre', type=str, required=True)

editarClienteParser = nuevoClienteParser.copy()
editarClienteParser.add_argument('numero', type=int, required=True)

@nsCliente.route('/')
class ClientesResource(Resource):
    @nsCliente.marshal_list_with(modeloCliente)
    def get(self):
        return repo.get_all()
    
    
    @nsCliente.expect(modeloClienteSinID)
    @nsCliente.marshal_with(modeloCliente)
    def post(self):
        data = nuevoClienteParser.parse_args()
        cliente = repo.agregar(data)
        if cliente:
            return cliente, 201
        abort(500)

@nsCliente.route('/<int:id>')
class ClientesResource(Resource):
    @nsCliente.marshal_with(modeloCliente)
    def get(self, id):
        cliente = repo.get_by_id(id)
        if cliente:
            return cliente, 200
        abort(404)

    def delete(self, id):
        if repo.borrar(id):
            return 'Cliente eliminado', 200
        abort(400)

    @nsCliente.expect(modeloCliente)
    def put(self, id):
        data = editarClienteParser.parse_args()
        if repo.modificar(id, data):
            return 'Cliente actualizado', 200
        abort(404)