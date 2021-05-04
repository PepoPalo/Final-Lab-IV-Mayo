import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import axios from 'axios';

export default function PlanForm(){
    const history = useHistory()
    const { id } = useParams()
    const [plan, setPlan] = useState({
        id: '',
        nombre: '',
        costo_por_mes: '',
        cant_llamadas: '',
        cant_mensajes: '',
        cant_gigas: '',
        tipo: '',
        estaActivo: '',
    })

    useEffect(() => {
        // if (id) {
        //     axios.get(`http://localhost:5000/plans/${id}`)
        //         .then(response => setPlan(response.data))
        //         .catch(error => alert(error))
        // }
    }, [])

    function handleOnChange(event, campo) {
        setPlan({
            ...plan,
            [campo]: event.target.value
        })
    }

    function guardar(event) {

        event.preventDefault()
        event.stopPropagation()
        if (id) {
            axios.put(`http://localhost:5000/plans/${id}`, plan)
                .then(response => {
                    alert("se ha modificado el registro")
                    history.push("/plans/")
                })
                .catch(error => alert(error))
        }
        else {
            axios.post("http://localhost:5000/plans/", plan)
                .then(response => {
                    alert("se ha agregado el registro")
                    history.push("/plans/")
                }).catch(error => alert(error))
        }
    }

    return(
        <>
            <div className="container bg-white">

                {id && <h1>Editando plan</h1>}
                {!id && <h1>Nuevo plan</h1>}
                <form onSubmit={(event) => guardar(event)}>
                    <div className="form-group">
                        <label>Nombre</label>
                        <input type="text" className="form-control" value={plan.nombre} onChange={(event) => handleOnChange(event, 'nombre')} />
                    </div>
                    <div className="form-group">
                        <label>Costo por mes</label>
                        <input type="text" className="form-control" value={plan.costo_por_mes} onChange={(event) => handleOnChange(event, 'costo_por_mes')} />
                    </div>
                    <div className="form-group">
                        <label>Cantidad de llamadas</label>
                        <input type="text" className="form-control" value={plan.cant_llamadas} onChange={(event) => handleOnChange(event, 'cant_llamadas')} />
                    </div>
                    <div className="form-group">
                        <label>Cantidad de mensajes</label>
                        <input type="text" className="form-control" value={plan.cant_mensajes} onChange={(event) => handleOnChange(event, 'cant_mensajes')} />
                    </div>
                    <div className="form-group">
                        <label>Cantidad de gigas</label>
                        <input type="text" className="form-control" value={plan.cant_gigas} onChange={(event) => handleOnChange(event, 'cant_gigas')} />
                    </div>
                    <div className="form-group">
                        <label>Tipo</label>
                        <input type="text" className="form-control" value={plan.tipo} onChange={(event) => handleOnChange(event, 'tipo')} />
                    </div>

                    <div className="float-right">
                        <button type="submit" className="btn btn-primary mr-2">Aceptar</button>
                        <button onClick={() => history.push("/plans/")} className="btn btn-primary">Cancelar</button>
                    </div>
                </form>
            </div>
        </>
    )
}