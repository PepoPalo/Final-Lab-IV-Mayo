import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import axios from 'axios';

export default function ClienteForm(){
    const history = useHistory()
    const { id } = useParams()
    const [cliente, setCliente] = useState({
        id: '',
        nombre: '',
        direccion: '',
        sexo: '',
        fecha_ingreso: '',
        activo: '',
    })

    useEffect(() => {
        // if (id) {
        //     axios.get(`http://localhost:5000/clientes/${id}`)
        //         .then(response => setCliente(response.data))
        //         .catch(error => alert(error))
        // }
    }, [])

    function handleOnChange(event, campo) {
        setCliente({
            ...cliente,
            [campo]: event.target.value
        })
    }

    function guardar(event) {

        event.preventDefault()
        event.stopPropagation()
        if (id) {
            axios.put(`http://localhost:5000/clientes/${id}`, cliente)
                .then(response => {
                    alert("se ha modificado el registro")
                    history.push("/clientes/")
                })
                .catch(error => alert(error))
        }
        else {
            axios.post("http://localhost:5000/clientes/", cliente)
                .then(response => {
                    alert("se ha agregado el registro")
                    history.push("/clientes/")
                }).catch(error => alert(error))
        }
    }

    return(
        <>
            <div className="container bg-white">

                {id && <h1>Editando cliente</h1>}
                {!id && <h1>Nuevo cliente</h1>}
                <form onSubmit={(event) => guardar(event)}>
                    <div className="form-group">
                        <label>Nombre</label>
                        <input type="text" className="form-control" value={cliente.nombre} onChange={(event) => handleOnChange(event, 'nombre')} />
                    </div>
                    <div className="form-group">
                        <label>Dirección</label>
                        <input type="text" className="form-control" value={cliente.direccion} onChange={(event) => handleOnChange(event, 'direccion')} />
                    </div>
                    <div className="form-group">
                        <label>Sexo</label>
                        <input type="text" className="form-control" value={cliente.sexo} onChange={(event) => handleOnChange(event, 'sexo')} />
                    </div>
                    <div className="form-group">
                        <label>Edad</label>
                        <input type="text" className="form-control" value={cliente.edad} onChange={(event) => handleOnChange(event, 'edad')} />
                    </div>

                    <div className="float-right">
                        <button type="submit" className="btn btn-primary mr-2">Aceptar</button>
                        <button onClick={() => history.push("/clientes/")} className="btn btn-primary">Cancelar</button>
                    </div>
                </form>
            </div>
        </>
    )
}