# Gym Tracker

## Qué es
App web para llevar el registro de tus entrenamientos y tu peso corporal, y ver cómo progresas con el tiempo. El backend está hecho con Django y entrega los datos por una API, para conectarle después una interfaz en React.

## Qué hace
- Perfil de cada usuario (altura, fecha de nacimiento, género)
- Registro del peso corporal con fecha automática
- Registro de entrenamientos (fecha, duración, intensidad)
- Series de cada entrenamiento (ejercicio, repeticiones, peso levantado, descanso)
- Panel de administración para cargar y revisar los datos
- API de lectura en formato JSON

## API
Todas las direcciones responden a pedidos `GET`.

| Dirección | Qué devuelve |
|-----------|--------------|
| `/api/pesos/` | Registros de peso corporal |
| `/api/entrenamientos/` | Entrenamientos |
| `/api/series/` | Series de cada entrenamiento |

## Próximamente
- Crear datos desde la API
- Login con token, para que cada usuario vea solo lo suyo
- Interfaz en React
- Gráficos de progreso
- Entrenador personal con IA que use tu historial
- PostgreSQL, Docker y GitHub Actions

## Tecnologías
- Python
- Django
- Django REST Framework
- SQLite

## Cómo correrlo
1. Clona el repositorio y entra a la carpeta.
2. Crea y activa un entorno virtual: `python -m venv venv` y luego `source venv/bin/activate` (en fish: `source venv/bin/activate.fish`).
3. Instala las dependencias: `pip install django djangorestframework`.
4. Crea la base de datos: `python manage.py migrate`.
5. Crea un superusuario: `python manage.py createsuperuser`.
6. Levanta el servidor: `python manage.py runserver`.
7. Abre `http://127.0.0.1:8000/admin` para cargar datos y `http://127.0.0.1:8000/api/pesos/` para ver la API.