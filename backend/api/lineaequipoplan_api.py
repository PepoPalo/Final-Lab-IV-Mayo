from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from infraestructura.lineaequipoplan_repo import LineaEquipoPlanRepo
from infraestructura.clientes_lep_repo import ClientesLepRepo
from flask_restx.inputs import date

repo = LineaEquipoPlanRepo()
repoLep = ClientesLepRepo()

nsLEP = Namespace('lineaequipoplan', description= 'Administrador de linea-equipo-plan')
modeloLEPSinNum = Model('DetalleSinNumero',{
    'plan_id': fields.Integer(),
    'linea_id': fields.Integer(),
    'equipo_id': fields.Integer(),
    'fecha_ini': fields.Date(),
    'fecha_fin': fields.Date(),
    'plan_costo': fields.Float()


})

modeloLEP = modeloLEPSinNum.clone('Lineaequipoplan', {
    'id': fields.Integer()
})

nsLEP.models[modeloLEPSinNum.name] = modeloLEPSinNum
nsLEP.models[modeloLEP.name] = modeloLEP

nuevoLEPParser = reqparse.RequestParser(bundle_errors=True)
nuevoLEPParser.add_argument('plan_id', type=int, required=True)
nuevoLEPParser.add_argument('linea_id', type=int, required=True)
nuevoLEPParser.add_argument('equipo_id', type=int, required=True)
nuevoLEPParser.add_argument('fecha_ini', type=date, required=True)
nuevoLEPParser.add_argument('fecha_fin', type=date, required=False)
nuevoLEPParser.add_argument('plan_costo', type=float, required=True)

editarLEPParser = nuevoLEPParser.copy()
editarLEPParser.add_argument('id', type=int, required=True)

@nsLEP.route('/')
class LepResource(Resource):
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
class LepResource(Resource):
    @nsLEP.marshal_with(modeloLEP)
    def get(self, id):
        df = repo.get_by_id(id)
        if df:
            return df, 200
        abort(400)
   
    @nsLEP.expect(modeloLEP)
    def put(self, id):
        data = editarLEPParser.parse_args()
        if repo.modificar(id,data):
            return 'Relacion linea-equipo-plan modificada', 200
        abort(404)
@nsLEP.route('/baja/<int:id>')
class LepResource(Resource):
    @nsEquipo.expect(modeloLEP)

    def put(self, id):
        if repo.baja(id):
            #baja en cliente_lep           
            repoLep.bajalep(id)
            return 'Relacion linea-equipo-plan dada de Baja', 200            
        abort(400)