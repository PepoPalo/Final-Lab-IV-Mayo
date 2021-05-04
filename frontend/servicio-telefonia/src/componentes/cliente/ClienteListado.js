import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";
import axios from 'axios';

var clientes = [
    {
        id: 1,
        nombre: 'Pedro Palomino',
        direccion: 'Av. Crespo 1072',
        sexo: 'Masculino',
        edad: 26
    },
    {
        id: 2,
        nombre: 'Milagros Pavón',
        direccion: 'Buenos Aires 726',
        sexo: 'Femenino',
        edad: 25
    },
    {
        id: 3,
        nombre: 'Josué Main',
        direccion: 'Av. Zanni 1970',
        sexo: 'Masculino',
        edad: 29
    }
]

export default function ClienteForm() {
    const [lista, setLista] = useState([])
    useEffect(() => {
      getClientes()
    }, [])
  
    function getClientes() {
    //   axios.get("http://localhost:5000/clientes/")
    //     .then((response) => setLista(response.data.filter(mozo => mozo.numero != null)))
    //     .catch((error) => alert(error))
        setLista(clientes)
    }
  
  
    // function borrar(id) {
    //   axios.delete(`http://localhost:5000/clientes/${id}`)
    //     .then((response) => {
    //       alert("Registro borrado correctamente")
    //       getClientes()
    //     })
    //     .catch(error => alert(error))
    // }


    return (
        <>
            <div className="bg-white rounded-bottom rounded-right">
                <div>
                    <button className="btn btn-primary my-3">Nuevo</button>
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
                        <th scope="col">#</th>
                        <th className="text-center" scope="col">Nombre</th>
                        <th  className="text-center" scope="col">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {lista.length > 0 && (
                            lista.map(cliente => (
                                <>
                                <tr key={cliente.id}>
                                    <th scope="row">{cliente.id}</th>
                                    <td className="text-center">{cliente.nombre}</td>
                                    <td className="text-center">
                                        <Link className="btn btn-primary" to={"/clientes/"/* + cliente.numero*/}>Ver</Link> &nbsp;
                                        <button className="btn btn-warning"   to={"/clientes/"/* + cliente.numero*/}>Editar</button> &nbsp;
                                    </td>
                                </tr>
                            {/*!cliente.cerrada &&(
                                <td>
                                <button className="btn btn-primary" to={"/adiciones/" + cliente.numero} disabled>Ver</button> &nbsp;
                                <Link className="btn btn-warning" to={"/adiciones/" + cliente.numero}>Editar</Link> &nbsp;
                                </td>

                            )*/}
                                {/*cliente.cerrada &&(
                                <td >
                                <Link className="btn btn-primary" to={"/adiciones/" + cliente.numero}>Ver</Link> &nbsp;
                                <button className="btn btn-warning"   to={"/adiciones/" + cliente.numero} disabled>Editar</button> &nbsp;
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