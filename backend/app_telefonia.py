from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from backend.datos import db

from backend.api.clientes_api import nsCliente
from backend.api.equipos_api import nsEquipo
from backend.api.lineas_api import nsLinea
from backend.api.lineaequipoplan_api import nsLEP
from backend.api.planes_api import nsPlan
from backend.api.cliente_lep_api import nsclienteLEP

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Yegua2020@localhost/Telefonia"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:100letters@localhost/Telefonia"

CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()


api = Api(app, version='1.0.beta', title='Telefonía', description='Administracion de servicio de telefonía')

api.add_namespace(nsCliente)
api.add_namespace(nsEquipo)
api.add_namespace(nsLinea) 
api.add_namespace(nsLEP)
api.add_namespace(nsPlan)
api.add_namespace(nsclienteLEP)

if __name__ == '__main__':
    app.run()