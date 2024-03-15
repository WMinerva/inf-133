import requests

query = """ 
{
    # estudiantes {
    #     nombre
    #     apellido
    # }
    # estudiantePorNombreYApellido(nombre: "Pedrito", apellido: "García") {
    # nombre
    # apellido
    # carrera
    # }
    # estudiantesPorCarrera(carrera: "Ingeniería de Sistemas") {
    #     nombre
    #     apellido
    # }
    mutation {
        crearEstudiante(nombre: "Juan", apellido: "García", carrera: "Arquitectura") {
            estudiante {
              id
                nombre
                apellido
                carrera
            }
        }
        crearEstudiante(nombre: "Pedro", apellido: "García", carrera: "Arquitectura") {
            estudiante {
            id
            nombre
            apellido
            carrera
            }
        }
        crearEstudiante(nombre: "Jose", apellido: "Lopez", carrera: "Arquitectura") {
            estudiante {
            id
            nombre
            apellido
            carrera
            }
        }
    }
    estudiantesPorCarrera(carrera: "Arquitectura") {
        nombre
        apellido
    }
    updateEstudiante(id: 2) {
        estudiante {
            nombre
            apellido
        }
    }
}
"""

url = "http://localhost:8000/graphql"

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={"query": query})
print(response.text)
