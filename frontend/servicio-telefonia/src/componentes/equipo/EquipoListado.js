import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";
import axios from 'axios';

var equipos = [
    {
        imei: 1,
        marca: 'IPhone',
        modelo: '10S Plus',
        estado: 'vendido',
        fecha_ingreso: '10/02/2020',
        activo: 'True'
    },
    {
        imei: 2,
        marca: 'Samsung',
        modelo: 'Galaxy S10',
        estado: 'preventa',
        fecha_ingreso: '10/05/2019',
        activo: 'False'
    },
    {
        imei: 3,
        marca: 'Motorola',
        modelo: 'G3',
        estado: 'vendido',
        fecha_ingreso: '01/01/2020',
        activo: 'True'
    },
    {
        imei: 4,
        marca: 'Motorola',
        modelo: 'G3',
        estado: 'descompuesto',
        fecha_ingreso: '01/01/2020',
        activo: 'False'
    }
]

export default function EquipoListado() {
    const [lista, setLista] = useState([])
    useEffect(() => {
      getEquipos()
    }, [])
  
    function getEquipos() {
    //   axios.get("http://localhost:5000/equipos/")
    //     .then((response) => setLista(response.data)))
    //     .catch((error) => alert(error))
        setLista(equipos)
    }
  
  
    // function borrar(imei) {
    //   axios.delete(`http://localhost:5000/equipos/${imei}`)
    //     .then((response) => {
    //       alert("Registro borrado correctamente")
    //       getEquipos()
    //     })
    //     .catch(error => alert(error))
    // }


    return (
        <>
            <div className="bg-white rounded-bottom rounded-right">
                <div>
                    <Link to="/equipos/nuevo" className="btn btn-primary my-3">Nuevo</Link>
                    <form >
                    {/* <div className="row"> */}
                        <label htmlFor="start">Desde:</label>
                        <input 
                            type="date"
                            min="2018-01-01" 
                            max="2023-12-31" 
                            // onChange={(event) => handleOnChange(event, 'desde')}
                        >
                        </input>

                        <label htmlFor="start">Hasta:</label>
                        <input 
                            type="date"
                            min="2018-01-01" 
                            max="2023-12-31" 
                            // onChange={(event) => handleOnChange(event, 'hasta')}
                            >
                        </input>
                        
                        {/* <button onClick={(event) => getFiltradas(event)}> BUSCAR</button> */}
                    {/* </div> */}
                </form>
                </div>
                <table className="table table-hover">
                    <thead className="bg-info">
                        <tr>
                        <th scope="col">IMEI</th>
                        <th className="text-center" scope="col">Marca</th>
                        <th className="text-center" scope="col">Modelo</th>
                        <th className="text-center" scope="col">Estado</th>
                        <th className="text-center" scope="col">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {lista.length > 0 && (
                            lista.map(equipo => (
                                <>
                                <tr key={equipo.imei}>
                                    <th scope="row">{equipo.imei}</th>
                                    <td className="text-center">{equipo.marca}</td>
                                    <td className="text-center">{equipo.modelo}</td>
                                    <td className="text-center">{equipo.estado}</td>
                                    <td className="text-center">
                                        <Link className="btn btn-outline-primary" to={"/equipos/" + equipo.numero}>Editar</Link> &nbsp;
                                        <Link className="btn btn-outline-danger"   to={"/equipos/"/* + equipo.numero*/}>Dar Baja</Link> &nbsp;
                                    </td>
                                </tr>
                            {/*!equipo.cerrada &&(
                                <td>
                                <button className="btn btn-primary" to={"/equipos/" + equipo.numero} disabled>Ver</button> &nbsp;
                                <Link className="btn btn-warning" to={"/equipos/" + equipo.numero}>Editar</Link> &nbsp;
                                </td>

                            )*/}
                                {/*equipo.cerrada &&(
                                <td >
                                <Link className="btn btn-primary" to={"/equipos/" + equipo.numero}>Ver</Link> &nbsp;
                                <button className="btn btn-warning"   to={"/equipos/" + equipo.numero} disabled>Editar</button> &nbsp;
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