import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import axios from 'axios';

export default function EquipoForm(){
    const history = useHistory()
    const { imei } = useParams()
    const [equipo, setEquipo] = useState({
        imei: '',
        marca: '',
        modelo: '',
        estado: '',
        fecha_ingreso: '',
        activo: '',
    })

    useEffect(() => {
        // if (imei) {
        //     axios.get(`http://localhost:5000/equipos/${imei}`)
        //         .then(response => setEquipo(response.data))
        //         .catch(error => alert(error))
        // }
    }, [])

    function handleOnChange(event, campo) {
        setEquipo({
            ...equipo,
            [campo]: event.target.value
        })
    }

    function guardar(event) {

        event.preventDefault()
        event.stopPropagation()
        if (imei) {
            axios.put(`http://localhost:5000/equipos/${imei}`, equipo)
                .then(response => {
                    alert("se ha modificado el registro")
                    history.push("/equipos/")
                })
                .catch(error => alert(error))
        }
        else {
            axios.post("http://localhost:5000/equipos/", equipo)
                .then(response => {
                    alert("se ha agregado el registro")
                    history.push("/equipos/")
                }).catch(error => alert(error))
        }
    }

    return(
        <>
            <div className="container bg-white">

                {imei && <h1>Editando equipo</h1>}
                {!imei && <h1>Nuevo equipo</h1>}
                <form onSubmit={(event) => guardar(event)}>
                    <div className="form-group">
                        <label>Marca</label>
                        <input type="text" className="form-control" value={equipo.marca} onChange={(event) => handleOnChange(event, 'marca')} />
                    </div>
                    <div className="form-group">
                        <label>Modelo</label>
                        <input type="text" className="form-control" value={equipo.modelo} onChange={(event) => handleOnChange(event, 'modelo')} />
                    </div>
                    <div className="form-group">
                        <label>Estado</label>
                        <input type="text" className="form-control" value={equipo.estado} onChange={(event) => handleOnChange(event, 'estado')} />
                    </div>
                    <div className="form-group">
                        <label>Fecha de Ingreso</label>
                        <input type="text" className="form-control" value={equipo.fecha_ingreso} onChange={(event) => handleOnChange(event, 'fecha_ingreso')} />
                    </div>

                    <div className="float-right">
                        <button type="submit" className="btn btn-primary mr-2">Aceptar</button>
                        <button onClick={() => history.push("/equipos/")} className="btn btn-primary">Cancelar</button>
                    </div>
                </form>
            </div>
        </>
    )
}