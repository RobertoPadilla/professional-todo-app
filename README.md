# <center>TODO NOTES APP</center>

## Descripción

Práctica para crear un pipeline de CI/CD para desarrollo de una sencilla aplicación de notas.

**Requerimientos:**

- Contar con una base de datos dummy en la cual se puedan crear nuevos registros y ademas contemos con los principales casos de uso (de fallos y de éxito).
- Tener una base de tests unitarios y de integración cuya cobertura sea **buena**.
- Crear entorno de desarrollo en docker con base de datos mysql, frontend en react y backend en fastapi (python)
- Crear CD para subir la imagen con el tag de la versión a DockerHub

**Casos de uso:**

- Se puede registrar un nuevo usuario
- El usuario puede cambiar su nombre
- El usuario puede elegir y cambiar su avatar
- El usuario puede crear un nuevo grupo de tareas
- El usuario puede crear una tarea dentro de un grupo (no deben existir tareas sin grupos)
- El usuario puede marcar/desmarcar una tarea como terminada/no-terminada 
- El usuario puede eliminar una tarea (arrojandole una advertencia primero)
- El usuario puede eliminar un grupo aún con tareas dentro (arrojandole una advertencia primero)

**Entidad Relacion:**

~~~mermaid
erDiagram
    users ||--o{ groups : has 
    groups ||--o{ tasks : has
~~~