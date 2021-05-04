import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import axios from 'axios';

export default function LineaForm(){
    const history = useHistory()
    const { id } = useParams()
    const [linea, setLinea] = useState({
        id: '',
        numero: '',
        estado: '',
        activo: '',
    })

    useEffect(() => {
        // if (id) {
        //     axios.get(`http://localhost:5000/lineas/${id}`)
        //         .then(response => setLinea(response.data))
        //         .catch(error => alert(error))
        // }
    }, [])

    function handleOnChange(event, campo) {
        setLinea({
            ...linea,
            [campo]: event.target.value
        })
    }

    function guardar(event) {

        event.preventDefault()
        event.stopPropagation()
        if (id) {
            axios.put(`http://localhost:5000/lineas/${id}`, linea)
                .then(response => {
                    alert("se ha modificado el registro")
                    history.push("/lineas/")
                })
                .catch(error => alert(error))
        }
        else {
            axios.post("http://localhost:5000/lineas/", linea)
                .then(response => {
                    alert("se ha agregado el registro")
                    history.push("/lineas/")
                }).catch(error => alert(error))
        }
    }

    return(
        <>
            <div className="container bg-white">

                {id && <h1>Editando linea</h1>}
                {!id && <h1>Nuevo linea</h1>}
                <form onSubmit={(event) => guardar(event)}>
                    <div className="form-group">
                        <label>Número</label>
                        <input type="text" className="form-control" value={linea.numero} onChange={(event) => handleOnChange(event, 'numero')} />
                    </div>
                    <div className="form-group">
                        <label>Estado</label>
                        <input type="text" className="form-control" value={linea.estado} onChange={(event) => handleOnChange(event, 'estado')} />
                    </div>

                    <div className="float-right">
                        <button type="submit" className="btn btn-primary mr-2">Aceptar</button>
                        <button onClick={() => history.push("/lineas/")} className="btn btn-primary">Cancelar</button>
                    </div>
                </form>
            </div>
        </>
    )
}