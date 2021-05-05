import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import axios from 'axios';

var clientep ={
    id: 1,
    nombre: 'Pedro Palomino',
    direccion: 'Av. Crespo 1072',
    sexo: 'Masculino',
    edad: 26,
    fecha_ingreso: '16/06/1996',
    activo: 'True'
}

export default function ClienteFicha(){
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

    const sexos = [
        'Masculino',
        'Femenino'
    ]

    useEffect(() => {
        // if (id) {
        //     axios.get(`http://localhost:5000/clientes/${id}`)
        //         .then(response => setCliente(response.data))
        //         .catch(error => alert(error))
        // }
        setCliente(clientep)
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
            <div className="container bg-white py-3">
                <div className="row px-2">
                    <div className="card col-3" style={{width: 18 + 'rem'}}>
                        <img src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png" class="card-img-top" alt="..."/>
                        <div className="card-body">
                            <h5 className="card-title">{cliente.nombre}</h5>
                            <p className="card-text">{cliente.edad} años</p>
                            <p className="card-text">{cliente.direccion}</p>
                            <p className="card-text">{cliente.sexo}</p>
                        </div>
                    </div>
                    <table class="table table-sm col-9">
                        <thead>
                            <tr>
                            <th scope="col">#</th>
                            <th scope="col">First</th>
                            <th scope="col">Last</th>
                            <th scope="col">Handle</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                            <th scope="row">1</th>
                            <td>Mark</td>
                            <td>Otto</td>
                            <td>@mdo</td>
                            </tr>
                            <tr>
                            <th scope="row">2</th>
                            <td>Jacob</td>
                            <td>Thornton</td>
                            <td>@fat</td>
                            </tr>
                            <tr>
                            <th scope="row">3</th>
                            <td colspan="2">Larry the Bird</td>
                            <td>@twitter</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </>
    )
}
