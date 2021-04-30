import React from 'react';

export default function ClienteForm(){

    return(
        <>
            <h1>Formulario de Clientes</h1>
            <form>
                <div className="form-group">
                    <label>Nombre</label>
                    <input type="text" ></input>
                </div>
                <div className="form-group">
                    <label>Dirección</label>
                    <input type="text" ></input>
                </div>
                <div className="form-group">
                    <label>Sexo</label>
                    <input type="text" ></input>
                </div>
                <div className="form-group">
                    <label>Edad</label>
                    <input type="text" ></input>
                </div>

                <button type="submit" ></button>
            </form>
        </>
    )
}