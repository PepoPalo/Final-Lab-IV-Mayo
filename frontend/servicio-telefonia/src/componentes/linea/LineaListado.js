import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";
import axios from 'axios';

var lineas = [
    {
        id: 1,
        numero: '+543435182886',
        estado: 'activada',
        activa: 'True'
    },
    {
        id: 2,
        numero: '+543435182887',
        estado: 'pendiente',
        activa: 'False'
    },
    {
        id: 3,
        numero: '+543435182826',
        estado: 'bloqueada',
        activa: 'False'
    },
    {
        id: 4,
        numero: '+543435123456',
        estado: 'bloqueada',
        activa: 'False'
    }
]

export default function LineaListado() {
    const [lista, setLista] = useState([])
    useEffect(() => {
      getLineas()
    }, [])
  
    function getLineas() {
    //   axios.get("http://localhost:5000/lineas/")
    //     .then((response) => setLista(response.data)))
    //     .catch((error) => alert(error))
        setLista(lineas)
    }
  
  
    // function borrar(id) {
    //   axios.delete(`http://localhost:5000/lineas/${id}`)
    //     .then((response) => {
    //       alert("Registro borrado correctamente")
    //       getLineas()
    //     })
    //     .catch(error => alert(error))
    // }


    return (
        <>
            <div className="bg-white rounded-bottom rounded-right">
                <div>
                    <Link to='/lineas/nueva' className="btn btn-primary my-3">Nuevo</Link>
                </div>
                <table className="table table-hover">
                    <thead className="bg-info">
                        <tr>
                        <th className="text-center" scope="col">Número</th>
                        <th className="text-center" scope="col">Estado</th>
                        <th className="text-center" scope="col">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {lista.length > 0 && (
                            lista.map(linea => (
                                <>
                                <tr key={linea.id}>
                                    <th className="text-center">{linea.numero}</th>
                                    <td className="text-center">{linea.estado}</td>
                                    <td className="text-center">
                                        <Link className="btn btn-primary" to={"/lineas/" + linea.numero}>Editar</Link> &nbsp;
                                        <button className="btn btn-danger"   to={"/lineas/"/* + linea.numero*/}>Baja</button> &nbsp;
                                    </td>
                                </tr>
                            {/*!linea.cerrada &&(
                                <td>
                                <button className="btn btn-primary" to={"/lineas/" + linea.numero} disabled>Ver</button> &nbsp;
                                <Link className="btn btn-warning" to={"/lineas/" + linea.numero}>Editar</Link> &nbsp;
                                </td>

                            )*/}
                                {/*linea.cerrada &&(
                                <td >
                                <Link className="btn btn-primary" to={"/lineas/" + linea.numero}>Ver</Link> &nbsp;
                                <button className="btn btn-warning"   to={"/lineas/" + linea.numero} disabled>Editar</button> &nbsp;
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