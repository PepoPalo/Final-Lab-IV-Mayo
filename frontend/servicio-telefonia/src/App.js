import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, Switch, Route, BrowserRouter as Router } from "react-router-dom";

import ClienteForm from './componentes/cliente/ClienteForm';
import ClienteListado from './componentes/cliente/ClienteListado';

import EquipoForm from './componentes/equipo/EquipoForm';
import EquipoListado from './componentes/equipo/EquipoListado';

import LineaForm from './componentes/linea/LineaForm';
import LineaListado from './componentes/linea/LineaListado';

import PlanForm from './componentes/plan/PlanForm';
import PlanListado from './componentes/plan/PlanListado';


export default function App() {
  return (
    <div className="container">
      <Router>
        <div className="App">
          <ul className="nav nav-tabs">
            <li className="nav-item">
              <Link className="nav-link active" to="/clientes">Clientes</Link>
            </li>
            <li className="nav-item dropdown">
              <Link className="nav-link active" to="/equipos">Equipos</Link>

            </li>
           
            <li className="nav-item dropdown">
              <Link className="nav-link active" to="/lineas">Linea</Link>

            </li>
          </ul>
        </div>
        <Switch>

          {/* Clientes */}
          <Route path="/clientes/nuevo" component={ClienteForm}></Route>
          <Route path="/clientes/:id" component={ClienteForm}></Route>
          <Route path="/clientes" component={ClienteListado}></Route>

          {/* Equipos */}
          <Route path="/equipos/nuevo" component={EquipoForm}></Route>
          <Route path="/equipos/:id" component={EquipoForm} ></Route>
          <Route path="/equipos" component={EquipoListado}></Route>

          {/* Linea */}
          <Route path="/lineas/nueva" component={LineaForm}></Route>
          <Route path="/lineas/:numero" component={LineaForm}></Route>
          <Route path="/lineas/buscar/:desde/:hasta" component={LineaListado}></Route>
          <Route path="/lineas/buscar/:desde/:hasta/:mozo" component={LineaListado}></Route>
          <Route path="/lineas" component={LineaListado}></Route>

        </Switch>
      </Router >
    </div>
  );
}

