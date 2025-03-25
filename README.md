# 🏋️‍♂️ Prueba - Flujopay API

Este proyecto es una API REST construida con **Django 5**, **Django REST Framework**, **PostgreSQL** y **JWT**, que permite a los usuarios:

- Registrarse e iniciar sesión
- Crear rutinas de ejercicio asociadas a días y horas
- Asociar ejercicios a rutinas
- Visualizar sus rutinas y ejercicios relacionados

## 🛠️ Tecnologías

- Django 5.0
- Django REST Framework
- PostgreSQL (via Docker)
- JWT (`djangorestframework-simplejwt`)
- Docker + Docker Compose

## 🚀 Instalación

1. Clonar el proyecto:

```bash
git clone https://github.com/rcasanova27/gym_routine.git
cd gym_routine
```

2. Crear el .env: 
```bash
POSTGRES_DB=gymdb
POSTGRES_USER=gymuser
POSTGRES_PASSWORD=gympass
```
3. Levantar el entorno 
```bash
docker compose up --build
```
4. Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

6. Acceder al panel de administración
URL: http://localhost:8000/admin/