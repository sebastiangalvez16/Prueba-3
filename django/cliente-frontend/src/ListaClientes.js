import React, { useState, useEffect } from "react";
import { obtenerClientes } from "./api/clientes";
import "./ListaClientes.css";

const ListaClientes = () => {
    const [clientes, setClientes] = useState([]);
    const [clientesFiltrados, setClientesFiltrados] = useState([]);
    const [error, setError] = useState(null);

    // Estados para filtros
    const [estado, setEstado] = useState("");
    const [genero, setGenero] = useState("");
    const [rangoSaldo, setRangoSaldo] = useState([0, Infinity]);
    const [rangoEdad, setRangoEdad] = useState([0, 100]); // Edad entre 0 y 100
    const [nivelSatisfaccion, setNivelSatisfaccion] = useState("");

    useEffect(() => {
        const fetchClientes = async () => {
            try {
                const data = await obtenerClientes();
                setClientes(data);
                setClientesFiltrados(data);
            } catch (err) {
                setError("No se pudo cargar la lista de clientes");
            }
        };
        fetchClientes();
    }, []);

    // Manejador para aplicar filtros
    const aplicarFiltros = () => {
        let filtrados = [...clientes];

        // Filtrar por estado (Activo/Inactivo)
        if (estado !== "") {
            filtrados = filtrados.filter((cliente) =>
                estado === "Activo" ? cliente.active : !cliente.active
            );
        }

        // Filtrar por género
        if (genero !== "") {
            filtrados = filtrados.filter(
                (cliente) => cliente.genero.toLowerCase() === genero.toLowerCase()
            );
        }

        // Filtrar por rango de saldo
        filtrados = filtrados.filter(
            (cliente) => cliente.saldo >= rangoSaldo[0] && cliente.saldo <= rangoSaldo[1]
        );

        // Filtrar por rango de edad
        filtrados = filtrados.filter(
            (cliente) => cliente.edad >= rangoEdad[0] && cliente.edad <= rangoEdad[1]
        );

        // Filtrar por nivel de satisfacción
        if (nivelSatisfaccion !== "") {
            filtrados = filtrados.filter(
                (cliente) => cliente.nivel_de_satisfaccion === parseInt(nivelSatisfaccion)
            );
        }

        setClientesFiltrados(filtrados);
    };

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h1>Listado de Clientes</h1>

            {/* Filtros */}
            <div className="filtros">
                <label>
                    Estado:
                    <select
                        value={estado}
                        onChange={(e) => setEstado(e.target.value)}
                    >
                        <option value="">Todos</option>
                        <option value="Activo">Activo</option>
                        <option value="Inactivo">Inactivo</option>
                    </select>
                </label>
                <label>
                    Género:
                    <select
                        value={genero}
                        onChange={(e) => setGenero(e.target.value)}
                    >
                        <option value="">Todos</option>
                        <option value="Masculino">Masculino</option>
                        <option value="Femenino">Femenino</option>
                    </select>
                </label>
                <label>
                    Rango de Saldo:
                    <input
                        type="number"
                        placeholder="Mínimo"
                        onChange={(e) =>
                            setRangoSaldo([+e.target.value || 0, rangoSaldo[1]])
                        }
                    />
                    <input
                        type="number"
                        placeholder="Máximo"
                        onChange={(e) =>
                            setRangoSaldo([rangoSaldo[0], +e.target.value || Infinity])
                        }
                    />
                </label>
                <label>
                    Rango de Edad:
                    <input
                        type="number"
                        placeholder="Mínimo"
                        onChange={(e) =>
                            setRangoEdad([+e.target.value || 0, rangoEdad[1]])
                        }
                    />
                    <input
                        type="number"
                        placeholder="Máximo"
                        onChange={(e) =>
                            setRangoEdad([rangoEdad[0], +e.target.value || 100])
                        }
                    />
                </label>
                <label>
                    Nivel de Satisfacción:
                    <select
                        value={nivelSatisfaccion}
                        onChange={(e) => setNivelSatisfaccion(e.target.value)}
                    >
                        <option value="">Todos</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                </label>
                <button onClick={aplicarFiltros}>Aplicar Filtros</button>
            </div>

            {/* Tabla */}
            <table border="1">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Edad</th>
                        <th>Género</th>
                        <th>Saldo</th>
                        <th>Activo</th>
                        <th>Satisfacción</th>
                    </tr>
                </thead>
                <tbody>
                    {clientesFiltrados.map((cliente) => (
                        <tr key={cliente.id}>
                            <td>{cliente.cliente_id}</td>
                            <td>{cliente.edad}</td>
                            <td>{cliente.genero}</td>
                            <td>{cliente.saldo}</td>
                            <td>{cliente.active ? "Sí" : "No"}</td>
                            <td>{cliente.nivel_de_satisfaccion}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ListaClientes;