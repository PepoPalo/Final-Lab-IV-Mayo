import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";
import axios from 'axios';

var planes = [
    {
        id: 1,
        nombre: 'Plan 5G',
        costo_por_mes: 1690.00,
        cant_llamadas: 1000,
        cant_mensajes: 5000,
        cant_gigas: 5,
        tipo: 'tarjeta',
        estaActivo: 'False'
    },
    {
        id: 2,
        nombre: 'Plan 3G',
        costo_por_mes: 1300.00,
        cant_llamadas: 1000,
        cant_mensajes: 5000,
        cant_gigas: 3,
        tipo: 'tarjeta',
        estaActivo: 'False'
    },
    {
        id: 3,
        nombre: 'Familiar',
        costo_por_mes: 2190.00,
        cant_llamadas: 10000,
        cant_mensajes: 10000,
        cant_gigas: 10,
        tipo: 'tarjeta',
        estaActivo: 'False'
    },
    {
        id: 4,
        nombre: 'Básico',
        costo_por_mes: 500.00,
        cant_llamadas: 500,
        cant_mensajes: 1000,
        cant_gigas: 1,
        tipo: 'prepaga',
        estaActivo: 'False'
    }
]

export default function PlanListado() {
    const [lista, setLista] = useState([])
    useEffect(() => {
      getPlanes()
    }, [])
  
    function getPlanes() {
    //   axios.get("http://localhost:5000/planes/")
    //     .then((response) => setLista(response.data.filter(mozo => mozo.nombre != null)))
    //     .catch((error) => alert(error))
        setLista(planes)
    }
  
  
    // function borrar(id) {
    //   axios.delete(`http://localhost:5000/planes/${id}`)
    //     .then((response) => {
    //       alert("Registro borrado correctamente")
    //       getPlanes()
    //     })
    //     .catch(error => alert(error))
    // }


    return (
        <>
            <div className="bg-white rounded-bottom rounded-right">
                <div>
                    <Link to="/planes/nuevo" className="btn btn-primary my-3">Nuevo</Link>
                </div>
                <table className="table table-hover">
                    <thead className="bg-info">
                        <tr>
                        <th className="text-center" scope="col">Nombre</th>
                        <th className="text-center" scope="col">Costo por mes</th>
                        <th className="text-center" scope="col">Cantidad de llamadas</th>
                        <th className="text-center" scope="col">Cantidad de mensajes</th>
                        <th className="text-center" scope="col">Cantidad de gigas</th>
                        <th className="text-center" scope="col">Tipo</th>
                        <th className="text-center" scope="col">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {lista.length > 0 && (
                            lista.map(plan => (
                                <>
                                <tr key={plan.id}>
                                    <th className="text-center">{plan.nombre}</th>
                                    <td className="text-center">$ {plan.costo_por_mes}</td>
                                    <td className="text-center">{plan.cant_llamadas}</td>
                                    <td className="text-center">{plan.cant_mensajes}</td>
                                    <td className="text-center">{plan.cant_gigas} gb</td>
                                    <td className="text-center">{plan.tipo}</td>
                                    <td className="text-center">
                                        <Link className="btn btn-outline-primary" to={"/planes/" + plan.id}>Editar</Link> &nbsp;
                                        <button className="btn btn-outline-danger"   to={"/planes/"}>Eliminar</button> &nbsp;
                                    </td>
                                </tr>
                            {/*!plan.cerrada &&(
                                <td>
                                <button className="btn btn-primary" to={"/planes/" + plan.nombre} disabled>Ver</button> &nbsp;
                                <Link className="btn btn-warning" to={"/planes/" + plan.nombre}>Editar</Link> &nbsp;
                                </td>

                            )*/}
                                {/*plan.cerrada &&(
                                <td >
                                <Link className="btn btn-primary" to={"/planes/" + plan.nombre}>Ver</Link> &nbsp;
                                <button className="btn btn-warning"   to={"/planes/" + plan.nombre} disabled>Editar</button> &nbsp;
                                </td>

                                )*/}
                                
                            </>))
                        )}
                        {lista.length === 0 && (
                            <tr>
                            <td colSpan="3">
                                <h2>No hay datos</h2>
                            </td>
                            </tr>
                        )}
                    </tbody>
                </table>

            </div>
        </>
    )
}