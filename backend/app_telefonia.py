from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from datos import db

from api.clientes_api import nsMozo
from api.equipos_api import nsProducto
from api.lineas_api import nsAdicion
from api.lineaequipoplan_api import nsDetalle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Yegua2020@localhost/Telefonia"
CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()


api = Api(app, version='1.0.beta', title='Telefonía', description='Administracion de servicio de telefonía')

api.add_namespace(nsMozo)
api.add_namespace(nsProducto)
api.add_namespace(nsAdicion) 
api.add_namespace(nsDetalle)

if __name__ == '__main__':
    app.run()