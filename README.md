# flujo_rutinas


esta aplicacion permite a los usuarios autenticarse y gestionar sus rutinas de entrenamiento mediante ejercicios asociados, 
esta construida con Django + Django RestFramework + JWT + SQLite.

Tecnologías

**Python** 

**Django** 

**Django Rest Framework**

**SimpleJWT**

**SQLite**


## Proceso de inicio del proyecto

1. Clonar el repositorio
```
 git clone https://github.com/emmanuelnavas31/flujo_rutinas.git
```

2. Acceder al repositorio
```
cd flujo_rutinas
``` 

3. crea un entorno virtual y activarlo

```
python -m venv .venv
source .venv/bin/activate
```

4. Instala dependencias
```
pip install -r requirements.txt
```
5. Inicia la base de datos y crea el primer usuario
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
6. Inicia el proyecto
```
python manage.py runserver
```


7. Endpoints Disponibles


| Método | Ruta               | Descripción                       |
|--------|--------------------|-----------------------------------|
| POST   | /api/token/        | Obtener token JWT                 |
| POST   | /api/token/refresh | Refrescar token JWT               |
| GET    | /api/rutinas/      | Listar rutinas del usuario        |
| POST   | /api/rutinas/      | Crear rutina (con `exercise_ids`) |
| GET    | /api/ejercicios/   | Listar ejercicios                 |
| POST   | /api/ejercicios/   | Crear nuevo ejercicio             |

